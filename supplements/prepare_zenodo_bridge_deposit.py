"""Prepare a DOI-bearing publication edition; never run the mathematical codes."""
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
from html import escape
import ast
import json

ROOT = Path(__file__).resolve().parent
BRIDGE = ROOT / 'deliverables/DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1'
HUMAN = ROOT / 'deliverables/DYN-PAQUET_REVUE_HUMAINE_PONT_IDEAL_1_2_v0_1'
OUT = ROOT / 'deliverables/DYN-DEPOT_ZENODO_PONT_IDEAL_1_2_v0_2'
SUPP = ROOT / 'zenodo_bridge_build/SUPPLEMENTS_PONT_IDEAL_1_2_v0_2'
LICENCE = ROOT / 'zenodo_bridge_inputs/licence DEL.pdf'
DOI = '10.5281/zenodo.23188815'
PREVIOUS_DOI = '10.5281/zenodo.23110956'
PDF_NAME = '01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf'
SUPP_NAME = '02_SUPPLEMENTS_PONT_IDEAL_1_2_v0_2.zip'
LICENCE_NAME = '03_LICENCE_DEL.pdf'
TITLE = 'DYN-VALIDEX — Pont idéal déterministe sur [1,2] : partition exacte et encadrement rationnel d’une intégrale géométrique'

def identity(p):
    data = p.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}

def tree(p):
    return {f.relative_to(p).as_posix(): identity(f) for f in sorted(p.rglob('*')) if f.is_file()}

def write_json(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

ABSTRACT_FR = '''Ce dossier présente un résultat mathématique conditionnel au modèle idéal continu explicitement défini. Pour a dans [1,2], les coordonnées delta, s et beta sont indépendantes et uniformes sur [0,1/a), [0,a) et [0,a). Les points de la ligne k appartiennent à s+k*beta+a*Z et au support fermé [-sqrt(2*(delta+k/a)),sqrt(2*(delta+k/a))]. Le premier support occupé détermine les extrêmes et la contribution c.

Une partition exacte montre que le premier rang vaut 0 ou 1 et que le premier support possède au plus trois points. Neuf cellules du plan auxiliaire (r,q), composées avec le choix de rang et les branches du modulo, décrivent les configurations admissibles et leurs contacts. La moyenne de phase et le conditionnement sont calculés analytiquement, puis l’intégrale locale I_[1,2]=integrale_1^2 a*E_Pa[c] da est réduite à une partie exacte et une intégrale lisse sur un rectangle.

Deux implémentations utilisant des fractions rationnelles, des bornes dirigées de racines carrées et un reste de Simpson tensoriel justifié donnent l’encadrement affiché vers l’extérieur : 0.234689097597 <= I_[1,2] <= 0.234689433430. Les bornes rationnelles exactes, sources et preuves des majorants de dérivées sont fournies. Les contrôles finis accompagnent les preuves universelles ; ils ne les remplacent pas.

La revue contradictoire Codex reçue accepte B01–B05 sous les hypothèses strictes de ce modèle. Une revue mathématique humaine indépendante est sollicitée et n’a pas encore été effectuée ; aucune formalisation par assistant de preuve n’est revendiquée. Le résultat est local, idéal et non normalisé : aucun facteur 6/pi^2, raccord C_mod, coefficient asymptotique, transfert de loi P2 ou constante globale n’est établi. Les sept composantes gelées restent UNKNOWN/null. Aucun nouveau flux RNG scientifique, calcul de quadrature ou run P2 n’a été lancé pour préparer cette édition documentaire.'''

ABSTRACT_EN = '''This deposit presents a mathematical result conditional on an explicitly defined ideal continuous model. For a in [1,2], delta, s and beta are independent and uniform on [0,1/a), [0,a) and [0,a). Row k consists of points in s+k*beta+a*Z inside the closed interval [-sqrt(2*(delta+k/a)),sqrt(2*(delta+k/a))]. The first occupied row determines its extrema and the contribution c.

An exact partition shows that the first occupied rank is 0 or 1 and contains at most three points. Nine cells in the auxiliary (r,q) plane, pulled back through rank selection and modulo branches, describe all admissible configurations and their contacts. Phase averaging and conditioning are derived analytically. The local integral I_[1,2]=integral_1^2 a*E_Pa[c] da is then reduced to an exact term and a smooth integral over a rectangle.

Two implementations based on rational arithmetic, outward square-root bounds and a justified tensor-product Simpson remainder yield the outward displayed enclosure 0.234689097597 <= I_[1,2] <= 0.234689433430. Exact rational endpoints, source code and derivative-bound proofs are included. Finite checks accompany the universal proofs and do not replace them.

The supplied Codex critical review accepts B01–B05 under the strict ideal-model assumptions. Independent human mathematical review is requested and has not yet taken place; no proof-assistant formalization is claimed. The result is local, ideal and unnormalized. No 6/pi^2 factor, C_mod identification, asymptotic coefficient, P2 law transfer or global constant is established. The seven frozen components remain UNKNOWN/null. No new scientific RNG stream, quadrature calculation or P2 run was launched to prepare this documentary edition.'''

DISCLOSURE = '''Patrick Royer est le porteur du projet et l’auteur humain du dépôt, chercheur indépendant non affilié. Le programme est conduit au moyen de questions, de protocoles, de décisions de périmètre et de dossiers de résultats successifs. L’assistance de ChatGPT/Codex est substantielle : dérivations mathématiques, rédaction, génération de code, vérifications exactes, contrelectures IA et intégration finale du dossier. La revue Codex jointe est identifiée comme une revue IA ; elle n’est pas une revue humaine extérieure. Aucune vérification personnelle de chaque démonstration par un humain mathématicien n’est attestée dans ce dossier. L’auteur du dépôt demeure responsable de son contenu. Les modèles et versions exactes non consignés dans les pièces ne sont pas inventés.

Les outils gratuits utilisés pour le calcul et les documents sont Python et sa bibliothèque standard (fractions.Fraction, math.isqrt), ReportLab, Poppler, ainsi que PyMuPDF et pypdf pour la préparation documentaire. ChatGPT/Codex sont cités comme assistants et outils, sans être présentés comme des outils nécessairement gratuits ou comme des auteurs/contributeurs des métadonnées Zenodo.'''

DESCRIPTION_HTML = '<h2>Résumé</h2>' + ''.join('<p>'+escape(p)+'</p>' for p in ABSTRACT_FR.split('\n\n'))
DESCRIPTION_HTML += '<h2>Abstract</h2>' + ''.join('<p>'+escape(p)+'</p>' for p in ABSTRACT_EN.split('\n\n'))
DESCRIPTION_HTML += '<h2>Assistance des IA et responsabilité</h2>' + ''.join('<p>'+escape(p)+'</p>' for p in DISCLOSURE.split('\n\n'))
DESCRIPTION_HTML += '<h2>Licence et revue demandée</h2><p>Licence personnalisée Dynagénèse Éthique (DEL), texte fourni sans modification dans '+LICENCE_NAME+'. Les documents sont soumis à une revue mathématique humaine ciblée de B01–B05 ; la checklist et le formulaire de retour sont inclus dans les compléments. Le DOI '+DOI+' a été communiqué pour ce dépôt ; cette préparation n’atteste pas sa publication effective.</p>'

def main():
    assert not OUT.exists() and not SUPP.exists()
    baseline = {'bridge': tree(BRIDGE), 'human_review_packet': tree(HUMAN), 'licence': identity(LICENCE)}
    for base, key in ((BRIDGE, 'bridge'), (HUMAN, 'human_review_packet')):
        m = json.loads((base / 'BUNDLE_MANIFEST.json').read_text(encoding='utf-8'))
        assert set(baseline[key]) == set(m['files']) | {'BUNDLE_MANIFEST.json'}
        assert all(baseline[key][name] == value for name, value in m['files'].items())
    OUT.mkdir(parents=True)
    SUPP.mkdir(parents=True)
    copies = {}
    for p in sorted(HUMAN.rglob('*')):
        if p.is_file():
            rel = p.relative_to(HUMAN)
            target = SUPP / 'dossier_revue_humaine_historique' / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(p.read_bytes())
            assert identity(target) == identity(p)
            copies[target.relative_to(SUPP).as_posix()] = {'source': str(p.relative_to(ROOT)), **identity(p)}
    (OUT / LICENCE_NAME).write_bytes(LICENCE.read_bytes())
    source = (BRIDGE / 'reproduction_sources/create_bridge_report.py').read_text(encoding='utf-8')
    edition = source
    replacements = []
    def change(old, new):
        nonlocal edition
        assert edition.count(old) == 1, old[:80]
        edition = edition.replace(old, new)
        replacements.append({'old': old, 'new': new})
    change("OUT=BASE/'deliverables/DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1'", "OUT=BASE.parent/'deliverables/DYN-DEPOT_ZENODO_PONT_IDEAL_1_2_v0_2'")
    change("para('Version 0.1 - 6 octobre 2026','SmallB')", "para('Édition de dépôt 0.2 - 6 octobre 2026 | DOI : "+DOI+"','SmallB')")
    change('aucun échantillonnage, aucune statistique ni consommation de RNG ne sont employés.', 'aucun échantillonnage, aucune statistique ni flux RNG scientifique ne sont employés.')
    change("['Partition exacte','Neuf cellules de phase et contacts fermés','Toutes coordonnées réelles admissibles sur [1,2]']", "['Partition exacte','Neuf cellules auxiliaires (r,q), rang et modulo','Tiré-en-arrière sur toutes coordonnées admissibles de [1,2]']")
    change('Une revue extérieure de ce nouveau pont reste à effectuer ; aucune certification par assistant de preuve formelle n’est revendiquée.', 'La revue Codex reçue accepte B01–B05 sous ces hypothèses. La revue humaine extérieure reste à effectuer ; aucune certification par assistant de preuve formelle n’est revendiquée.')
    change("heading('2. Les neuf cellules de phase, contacts inclus')", "heading('2. Les neuf cellules auxiliaires, contacts inclus')")
    change('Les points d’une ligne sont q+ja. Pour tout premier support possible, 0 ≤ r < 3a/2.', 'Les neuf cellules partitionnent le plan auxiliaire (r,q). Leur composition avec le choix du rang et les branches du modulo donne la partition complète. Les points d’une ligne sont q+ja ; tout premier support satisfait 0 ≤ r < 3a/2.')
    change("page();heading('7. Vérifications, limites et prochaine revue')", "page();heading('7. Vérifications, limites et revue reçue')")
    change("['Contrelecture des preuves et des deux codes','PASS interne sous les définitions du modèle']", "['Contrelectures des preuves et des codes','PASS interne ; revue Codex reçue, sous les hypothèses idéales']")
    change('Le nouveau registre BRIDGE_IDEAL_RESULTS.json est distinct.', 'Le registre de dépôt ZENODO_BRIDGE_EDITION_v0_2.json est distinct des registres historiques.')
    change("heading('Dossier autonome pour la revue extérieure')", "heading('Dossier autonome pour la revue humaine')")
    change('Le ZIP contient la preuve détaillée, la partition JSON, les deux codes et leurs certificats rationnels, les contrôles de contacts, les relectures internes et un prompt de revue contradictoire. Cette nouvelle revue doit contrôler les frontières, la densité, le conditionnement de phase, I₀, les dérivées et le reste de Simpson avant toute adoption au-delà du registre idéal local.', 'Les compléments contiennent la preuve détaillée, la partition JSON, les trois scripts, les deux certificats, les contrôles de contacts et les documents de revue Codex. La revue humaine demandée porte sur les frontières, la densité, le conditionnement, I₀, les dérivées et le reste de Simpson ; ses verdicts sont à renseigner.')
    change('Sources normatives : protocole descriptif P2, sections du modèle et de la fenêtre ; oracle rationnel pour la définition de c ; théorèmes idéaux et revue post-P2 du 6 octobre 2026. Le pont ajoute ses propres preuves, indépendamment des résultats descriptifs de la campagne.', 'Les hypothèses normatives du présent résultat sont définies à la section 1. La preuve historique intégrale, la partition et l’oracle rationnel sont joints. Le pont repose sur ses propres preuves, indépendamment des résultats descriptifs P2 ; aucune conformité du sampler ni normalisation canonique n’est ajoutée.')
    change("'DYN - Pont idéal [1,2] v0.1 | 6 octobre 2026'", "'Pont idéal [1,2] v0.2 | DOI : "+DOI+"'")
    # Both final path occurrences have the same literal, so replace as one logged transformation.
    if 'DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1.pdf' in edition:
        count = edition.count('DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1.pdf')
        edition = edition.replace('DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1.pdf', PDF_NAME)
        replacements.append({'old': 'DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1.pdf', 'new': PDF_NAME, 'occurrences': count})
    change("title='DYN-VALIDEX - Pont déterministe idéal [1,2] v0.1',author='Patrick Royer ; assistance et intégration ChatGPT/Codex'", "title='DYN-VALIDEX - Pont idéal [1,2] - DOI "+DOI+"',author='Patrick Royer'")
    annex = '''
page();heading('8. Provenance, licence et appel à relecture')
para('DOI de cette édition : 10.5281/zenodo.23188815. DOI communiqué par l’auteur pour son nouveau dépôt ; la préparation documentaire n’atteste pas la publication effective. Édition 0.2 du 6 octobre 2026, sans nouveau calcul scientifique.','SmallB')
heading('Ce qui a été examiné et ce qui reste déclaré')
para('Le rapport contradictoire Codex joint accepte B01–B05 sous les hypothèses strictes du modèle idéal continu. Son journal déclare 20 contrôles exacts PASS et 43 fichiers Windows identiques. Les trois sorties reproduites, la source du quatrième vérificateur et l’inventaire des 43 fichiers n’ont pas été joints. La confrontation locale a vérifié séparément les 28 fichiers du paquet source et recalculé 15 relations rationnelles accessibles ; ces périmètres ne sont pas assimilés.')
para('Les premiers démarrages CPython de la revue reçue pouvaient lire de l’entropie pour le secret de hachage ; le journal consigne une série finale PYTHONHASHSEED=0. Aucun flux RNG scientifique n’est rapporté. Ce constat ne constitue pas une attestation d’absence de toute entropie système au démarrage du runtime.')
para('L’oracle rationnel accepte beta sans garde explicite 0<=beta<a ; le modèle idéal impose cet intervalle. Des représentants signés sont utilisés par le canal ciblé historique. Ajouter n*a à beta décale les indices entiers de la maille au rang k ; la géométrie demeure identique. Cette équivalence ne démontre ni une loi de tirage ni un raccord numérique-continu.')
heading('Auteur, assistance et outils')
para('Patrick Royer est l’auteur humain du dépôt et le porteur du projet, chercheur indépendant non affilié. ChatGPT/Codex ont apporté une assistance substantielle aux dérivations, à la rédaction, au code, aux vérifications exactes, aux contrelectures IA et à l’intégration finale. Aucune revue mathématique humaine indépendante n’est attestée. La déclaration détaillée d’assistance est jointe aux compléments.')
para('Outils gratuits : Python et sa bibliothèque standard, ReportLab, Poppler, PyMuPDF et pypdf. Les services d’IA sont distingués de ces outils ; leur gratuité n’est pas revendiquée. Les IA ne figurent pas comme auteurs des métadonnées.','SmallB')
heading('Licence et retour humain demandé')
para('Licence personnalisée Dynagénèse Éthique (DEL) : texte original fourni sans modification dans 03_LICENCE_DEL.pdf. La présente édition ne réécrit pas cette licence.')
para('La checklist propose neuf contrôles couvrant B01–B05. Le formulaire demande les pièces examinées, les hypothèses, les outils éventuels, les réserves et les verdicts motivés. La revue humaine reste NOT_RUN, sans destinataire ni envoi attesté. Un avis reçu sera intégré dans un complément distinct, avec sa portée réelle.')
para('Citation : Royer, Patrick (2026). DYN-VALIDEX — Pont idéal déterministe sur [1,2] : partition exacte et encadrement rationnel d’une intégrale géométrique. Édition 0.2. DOI : 10.5281/zenodo.23188815.','SmallB')
'''
    change('\ndef footer(c,doc):', '\n'+annex+'\ndef footer(c,doc):')
    def equations(text):
        nodes = [n for n in ast.walk(ast.parse(text)) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'equation']
        return [ast.literal_eval(n.args[0]) for n in sorted(nodes, key=lambda n:n.lineno)]
    assert equations(source) == equations(edition)
    # Keep the nine index rows and all three polynomial contributions unchanged.
    table_rows = ["['0 ≤ r < a/2'", "['a/2 ≤ r < a'", "['a ≤ r < 3a/2'"]
    for row in table_rows:
        assert source.count(row) == edition.count(row) == 3
    generator = ROOT / 'zenodo_bridge_build/create_zenodo_bridge_report.py'
    generator.write_text(edition, encoding='utf-8')
    (SUPP / 'create_zenodo_bridge_report.py').write_bytes(generator.read_bytes())
    write_json(SUPP / 'MODIFICATIONS_EDITORIALES.json', {'schema':'DYN-ZENODO-EDITORIAL-CHANGES-v0.2',
        'original_generator_identity':identity(BRIDGE / 'reproduction_sources/create_bridge_report.py'),
        'publication_generator_identity':identity(generator), 'equation_strings_unchanged':True,
        'equation_string_count':len(equations(source)), 'changes':replacements,
        'mathematical_certificates_and_sources_modified':False})
    current = json.loads((HUMAN / 'statut/BRIDGE_IDEAL_RESULTS_CODEX_REVIEWED_v0_2.json').read_text(encoding='utf-8'))
    publication = deepcopy(current)
    publication.update({'schema':'DYN-ZENODO-IDEAL-BRIDGE-EDITION-v0.2',
        'edition':'0.2','doi':DOI,'doi_status':'USER_PROVIDED_FOR_NEW_DEPOSIT_PUBLICATION_NOT_ATTESTED',
        'status':'READY_FOR_ZENODO_MANUAL_UPLOAD', 'human_external_review':'NOT_RUN',
        'new_quadrature_or_partition_run_for_this_edition':False, 'new_scientific_rng_or_P2_called':False,
        'author':{'name':'Patrick Royer','affiliation':None,'description':'Chercheur indépendant non affilié'},
        'license':{'title':'Licence Dynagénèse Éthique (DEL)','file':LICENCE_NAME,'source_text_modified':False}})
    write_json(SUPP / 'ZENODO_BRIDGE_EDITION_v0_2.json', publication)
    write_json(SUPP / 'COPIES_ET_IDENTITES_DE_DEPOT.json', {'copies':copies,'licence':identity(LICENCE),
        'doi':DOI,'historical_source_files_modified':False})
    (SUPP / 'DECLARATION_ASSISTANCE_IA_ET_OUTILS.txt').write_text(DISCLOSURE+'\n',encoding='utf-8')
    (SUPP / 'RESUMES_FR_EN.txt').write_text('RÉSUMÉ\n\n'+ABSTRACT_FR+'\n\nABSTRACT\n\n'+ABSTRACT_EN+'\n',encoding='utf-8')
    (SUPP / 'README_COMPLEMENTS.txt').write_text('''Compléments de l’édition Zenodo 0.2 du pont idéal [1,2].
DOI communiqué : '''+DOI+'''.
Le dossier_revue_humaine_historique/ est la copie exacte du paquet autonome
préparé avant l’attribution de ce DOI. Ses 24 fichiers, son manifeste et les
statuts historiques sont conservés tels quels. Le registre courant propre au
dépôt est ZENODO_BRIDGE_EDITION_v0_2.json. Le générateur du PDF ne relance
aucun code mathématique ; il utilise ReportLab et les polices DejaVu.
La licence originale est fournie séparément sous '''+LICENCE_NAME+'''.
Le résultat demeure idéal local, non normalisé et conditionnel au modèle.
Les pièces de reproduction externes manquantes sont décrites sans être inventées.
La revue humaine demeure NOT_RUN ; aucun message n’a été envoyé à un tiers.
''',encoding='utf-8')
    citation = 'Royer, Patrick (2026). '+TITLE+'. Édition 0.2. Zenodo. https://doi.org/'+DOI+'. Prépublication ; revue humaine indépendante non effectuée.\n'
    (OUT / 'CITATION_DEPOT_v0_2.txt').write_text(citation,encoding='utf-8')
    (OUT / 'DESCRIPTION_ZENODO_FR_EN_v0_2.html').write_text(DESCRIPTION_HTML+'\n',encoding='utf-8')
    metadata = '''MÉTADONNÉES ZENODO — À SAISIR DANS LE BROUILLON EXISTANT
DOI communiqué pour ce dépôt : '''+DOI+'''

Conserver le brouillon où ce DOI a été réservé. Il appartient à ce dépôt.
La préparation des fichiers ne signifie pas que le dépôt a été publié.

TITRE
'''+TITLE+'''

AUTEUR / CRÉATEUR
Nom de famille : Royer
Prénom : Patrick
Statut : chercheur indépendant non affilié ; ne pas ajouter une institution.
ORCID : aucun identifiant fourni ; laisser vide si vous n’en avez pas.
Les IA sont déclarées dans la description, hors liste des auteurs/contributeurs.

TYPE ET VERSION
Type proposé : Publication / Preprint (prépublication).
Version : 0.2, édition documentaire de dépôt du pont idéal 0.1.
Langue principale : français ; résumé anglais inclus.
Date proposée : 2026-10-06 ; utiliser la date effective de mise à disposition.
Accès : public, conformément à votre choix de dépôt public.

LICENCE
Licence personnalisée : Licence Dynagénèse Éthique (DEL).
Texte original inchangé : '''+LICENCE_NAME+'''.
Dans le champ licence, utiliser Add custom et indiquer ce titre.
Description de licence : « Texte intégral de la licence DEL fourni avec le dépôt
sous '''+LICENCE_NAME+'''. » Ne pas ajouter en parallèle une licence standard
CC-BY ou MIT à ces mêmes fichiers : ce dossier conserve votre choix DEL.

MOTS-CLÉS PROPOSÉS
ideal continuous model ; exact partition ; lattice geometry ; phase averaging ;
rational arithmetic ; validated quadrature ; tensor-product Simpson rule ;
interval Taylor jets ; independent mathematical review ; DYN-VALIDEX.

LIEN AU DÉPÔT ANTÉRIEUR
DOI antérieur communiqué dans le programme : '''+PREVIOUS_DOI+'''.
Relation proposée : References / cite (référence bibliographique), et non
IsNewVersionOf : ce dossier est un résultat autonome complémentaire.
La disponibilité publique du dépôt antérieur n’est pas attestée ici.

DESCRIPTION — VERSION TEXTE À COPIER
'''+ABSTRACT_FR+'\n\nABSTRACT\n'+ABSTRACT_EN+'\n\nASSISTANCE DES IA ET OUTILS\n'+DISCLOSURE+'''

Licence personnalisée DEL jointe. Revue humaine indépendante sollicitée,
non effectuée. Le PDF et les compléments portent le DOI communiqué ci-dessus.
La version HTML de cette même description est jointe dans
DESCRIPTION_ZENODO_FR_EN_v0_2.html ; elle n’est pas un fichier scientifique à
téléverser séparément si la description a été copiée dans le formulaire.
'''
    (OUT / 'METADONNEES_ZENODO_v0_2.txt').write_text(metadata,encoding='utf-8')
    guide = '''MODE D’EMPLOI — DÉPÔT ZENODO DU PONT IDÉAL [1,2]
DOI communiqué : '''+DOI+'''

Ce dossier prépare votre brouillon existant. Il n’a pas été publié depuis
cette session, et la résolution publique du DOI n’est pas attestée ici.

FICHIERS À TÉLÉVERSER DANS ZENODO
1. '''+PDF_NAME+''' : article principal portant le DOI, 0.2.
2. '''+SUPP_NAME+''' : preuve historique, scripts, certificats,
   registre de dépôt, revues Codex, checklist et formulaire humain vierge.
3. '''+LICENCE_NAME+''' : votre texte DEL original, sans modification.
4. 04_MANIFESTE_FICHIERS_ZENODO_v0_2.json : SHA-256 et tailles de ces trois fichiers.
5. '''+SUPP_NAME+'''.sha256 : empreinte du ZIP des compléments.

Le dossier complet DYN-DEPOT_ZENODO_PONT_IDEAL_1_2_v0_2.zip est un transport
pour vous ; l’extraire pour sélectionner les cinq fichiers ci-dessus.
Il contient aussi les métadonnées, la citation et le présent guide.

SAISIE
Ouvrir le brouillon où le DOI a été réservé. Copier les champs du fichier
METADONNEES_ZENODO_v0_2.txt et la description FR/EN. Choisir la licence
personnalisée DEL et le type prépublication. Définir le PDF comme fichier
de prévisualisation du dépôt. Prévisualiser la notice, puis utiliser Publish
lorsque vous décidez de mettre ce dossier à disposition.

CONTENU SCIENTIFIQUE
Les équations et tableaux mathématiques, les scripts et les certificats sont
ceux du pont déjà examiné. Cette édition ajoute DOI, auteur humain, provenance
et statut de revue actualisé, sans nouvelle campagne ni nouveau calcul.
Le texte/PDF historique et le ledger gelé restent intacts. La revue humaine
reste NOT_RUN et aucun résultat global ne reçoit de promotion.

Après publication, transmettre l’adresse https://doi.org/'''+DOI+'''
avec la demande ciblée de relecture ; la checklist figure dans les compléments.
'''
    (OUT / '00_MODE_EMPLOI_DEPOT_ZENODO.txt').write_text(guide,encoding='utf-8')
    write_json(ROOT / 'zenodo_bridge_deposit_baseline_work.json', baseline)
    assert tree(BRIDGE) == baseline['bridge'] and tree(HUMAN) == baseline['human_review_packet']
    assert identity(LICENCE) == baseline['licence']
    print(json.dumps({'edition_directory':str(OUT),'supplements_directory':str(SUPP),
        'historical_files_copied':len(copies),'equation_strings_unchanged':True,
        'pdf_generator':str(generator),'doi':DOI}))

if __name__ == '__main__':
    main()
