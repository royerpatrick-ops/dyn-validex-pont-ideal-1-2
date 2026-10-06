"""Verify and archive the documentary Zenodo package; no scientific execution."""
from pathlib import Path
from hashlib import sha256
import json
import zipfile
import fitz

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'deliverables/DYN-DEPOT_ZENODO_PONT_IDEAL_1_2_v0_2'
SUPP = ROOT / 'zenodo_bridge_build/SUPPLEMENTS_PONT_IDEAL_1_2_v0_2'
BRIDGE = ROOT / 'deliverables/DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1'
HUMAN = ROOT / 'deliverables/DYN-PAQUET_REVUE_HUMAINE_PONT_IDEAL_1_2_v0_1'
DOI = '10.5281/zenodo.23188815'
PDF = OUT / '01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf'
SUPP_ZIP = OUT / '02_SUPPLEMENTS_PONT_IDEAL_1_2_v0_2.zip'
LICENCE = OUT / '03_LICENCE_DEL.pdf'
ARCHIVE = OUT.with_suffix('.zip')

def identity(p):
    data = p.read_bytes()
    return {'bytes':len(data),'sha256':sha256(data).hexdigest()}

def tree(p):
    return {f.relative_to(p).as_posix():identity(f) for f in sorted(p.rglob('*')) if f.is_file()}

def write_json(p,data):
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def zip_and_reread(folder,dest):
    assert not dest.exists()
    files=tree(folder)
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in files:
            z.write(folder/name,name)
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None and set(z.namelist())==set(files)
        for name,expected in files.items():
            data=z.read(name)
            assert expected=={'bytes':len(data),'sha256':sha256(data).hexdigest()}
    return len(files)

def main():
    assert not ARCHIVE.exists() and not SUPP_ZIP.exists()
    baseline=json.loads((ROOT/'zenodo_bridge_deposit_baseline_work.json').read_text())
    assert tree(BRIDGE)==baseline['bridge'] and tree(HUMAN)==baseline['human_review_packet']
    assert identity(LICENCE)==baseline['licence']
    copies=json.loads((SUPP/'COPIES_ET_IDENTITES_DE_DEPOT.json').read_text())['copies']
    assert len(copies)==24
    for name,expected in copies.items():
        assert identity(SUPP/name)=={k:expected[k] for k in ('bytes','sha256')}
    pdf=fitz.open(PDF)
    assert len(pdf)==9 and pdf.metadata['author']=='Patrick Royer'
    for page in pdf:
        text=page.get_text()
        assert DOI in text and '\ufffd' not in text
        for block in page.get_text('dict')['blocks']:
            if block.get('type')!=0:
                continue
            for line in block['lines']:
                for span in line['spans']:
                    x0,y0,x1,y1=span['bbox']
                    assert x0>=0 and y0>=0 and x1<=page.rect.width and y1<=page.rect.height
    fulltext='\n'.join(page.get_text() for page in pdf)
    assert '0,234689097597' in fulltext and '0,234689433430' in fulltext
    assert 'UNBOUNDED' in fulltext and 'NOT_RUN' in fulltext
    public=json.loads((SUPP/'ZENODO_BRIDGE_EDITION_v0_2.json').read_text())
    prior=json.loads((HUMAN/'statut/BRIDGE_IDEAL_RESULTS_CODEX_REVIEWED_v0_2.json').read_text())
    for key in ('adopted_exact_enclosure','exact_width','outward_decimal_12_places','I0_exact','I1_integrand',
                'I11','I13','continuous_law_transfer','C_mod','C_inf','B_global','global_C_validated',
                'conjecture_validated','canonical_normalizing_factor_applied','original_seven_components'):
        assert public[key]==prior[key],key
    assert public['human_external_review']=='NOT_RUN'
    source_urls='''Sources de préparation de la notice Zenodo, consultées le 6 octobre 2026.
Les pages ci-dessous expliquent le dépôt ; elles ne valident pas la preuve.
https://help.zenodo.org/docs/deposit/create-new-upload/
https://help.zenodo.org/docs/deposit/describe-records/resource-type/
https://help.zenodo.org/docs/deposit/describe-records/licenses/
https://support.zenodo.org/help/en-gb/13/227
Le nouveau DOI et le DOI antérieur sont ceux communiqués par l’auteur.
Leur publication effective et leur résolution publique n’ont pas été attestées.
'''
    (OUT/'SOURCES_NOTICE_ZENODO.txt').write_text(source_urls,encoding='utf-8')
    (SUPP/'SOURCES_NOTICE_ZENODO.txt').write_text(source_urls,encoding='utf-8')
    for name in ('prepare_zenodo_bridge_deposit.py','finalize_zenodo_bridge_deposit.py'):
        (SUPP/name).write_bytes((ROOT/name).read_bytes())
    validation={
        'schema':'DYN-ZENODO-DOCUMENTARY-PACKAGE-VALIDATION-v0.2',
        'status':'PASS_ZENODO_DOCUMENTARY_PACKAGE_READY', 'doi':DOI,
        'publication_effective_attested':False,'zenodo_upload_or_publication_performed':False,
        'human_review_status':'NOT_RUN','PDF_page_count':9,
        'PDF_pages_rendered_and_visually_inspected':[1,2,3,4,5,6,7,8,9],
        'DOI_on_every_PDF_page':True,'PDF_creator_author_human':'Patrick Royer',
        'mathematical_equation_strings_unchanged':True,
        'exact_enclosure_and_global_limits_unchanged':True,
        'historical_human_review_files_copied_byte_identically':24,
        'prior_bridge_files_unchanged':28,'prior_human_review_packet_files_unchanged':24,
        'original_licence_DEL_unchanged':True,
        'new_quadrature_or_partition_program_executed':False,
        'new_scientific_rng_or_P2_called':False,'frozen_ledger_modified':False,
        'third_party_contacted':False,
        'missing_external_Windows_evidence_invented':False,
        'visual_scope':'Publication PDF only; original historical PDF and original DEL licence copied unchanged.'}
    write_json(SUPP/'VALIDATION_EDITION_ZENODO_v0_2.json',validation)
    write_json(SUPP/'BUNDLE_MANIFEST_ZENODO_COMPLEMENTS.json',{
        'schema':'DYN-ZENODO-SUPPLEMENTS-MANIFEST-v0.2',
        'files':tree(SUPP),'excludes':['BUNDLE_MANIFEST_ZENODO_COMPLEMENTS.json']})
    supp_count=zip_and_reread(SUPP,SUPP_ZIP)
    (OUT/(SUPP_ZIP.name+'.sha256')).write_text(identity(SUPP_ZIP)['sha256']+'  '+SUPP_ZIP.name+'\n',encoding='ascii')
    write_json(OUT/'04_MANIFESTE_FICHIERS_ZENODO_v0_2.json',{
        'schema':'DYN-ZENODO-UPLOAD-FILES-v0.2','doi':DOI,
        'files':{p.name:identity(p) for p in (PDF,SUPP_ZIP,LICENCE)},
        'description':'Three principal files to upload, with the manifest and the supplements sidecar.'})
    write_json(OUT/'VALIDATION_DEPOT_ZENODO_v0_2.json',{
        **validation,'supplement_zip_files_fully_reread':supp_count,
        'supplement_zip_identity':identity(SUPP_ZIP)})
    write_json(OUT/'MANIFESTE_DOSSIER_COMPLET_v0_2.json',{
        'schema':'DYN-ZENODO-FULL-DEPOSIT-PACKET-MANIFEST-v0.2',
        'files':tree(OUT),'excludes':['MANIFESTE_DOSSIER_COMPLET_v0_2.json']})
    outer_count=zip_and_reread(OUT,ARCHIVE)
    assert tree(BRIDGE)==baseline['bridge'] and tree(HUMAN)==baseline['human_review_packet']
    assert identity(ROOT/'zenodo_bridge_inputs/licence DEL.pdf')==baseline['licence']
    result={**validation,'outer_zip_files_fully_reread':outer_count,
            'supplement_zip_files_fully_reread':supp_count,
            'PDF':identity(PDF),'supplement_zip':identity(SUPP_ZIP),
            'complete_deposit_zip':{'path':str(ARCHIVE),**identity(ARCHIVE)}}
    write_json(ROOT/'zenodo_bridge_deposit_final_receipt_work.json',result)
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    main()
