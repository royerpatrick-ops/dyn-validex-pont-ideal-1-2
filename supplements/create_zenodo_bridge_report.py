"""Author the self-contained ideal-bridge PDF; no model, sampler or RNG imports."""
from pathlib import Path
from html import escape
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE=Path(__file__).resolve().parent
OUT=BASE.parent/'deliverables/DYN-DEPOT_ZENODO_PONT_IDEAL_1_2_v0_2'
OUT.mkdir(parents=True,exist_ok=True)
for name,file in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleB',fontName='DVB',fontSize=23,leading=28,textColor=colors.HexColor('#172f45'),spaceAfter=15))
styles.add(ParagraphStyle(name='HeadB',fontName='DVB',fontSize=15,leading=19,textColor=colors.HexColor('#007c91'),spaceAfter=10))
styles.add(ParagraphStyle(name='BodyB',fontName='DV',fontSize=9.3,leading=13.6,spaceAfter=8))
styles.add(ParagraphStyle(name='MathB',fontName='DV',fontSize=9.7,leading=15,spaceAfter=10,backColor=colors.HexColor('#eef4f6'),borderPadding=8))
styles.add(ParagraphStyle(name='SmallB',fontName='DV',fontSize=8,leading=11.5,spaceAfter=7,textColor=colors.HexColor('#485864')))
styles.add(ParagraphStyle(name='CellB',fontName='DV',fontSize=8.1,leading=11.4))
styles.add(ParagraphStyle(name='CellHeadB',fontName='DVB',fontSize=8.1,leading=11.4,textColor=colors.white))
story=[]
def para(t,style='BodyB',markup=False):
    story.append(Paragraph(t if markup else escape(t),styles[style]))
def heading(t):para(t,'HeadB')
def equation(t):para(t,'MathB',True)
def page():story.append(PageBreak())
def table(head,rows,widths):
    values=[[Paragraph(escape(str(x)),styles['CellHeadB']) for x in head]]
    values += [[Paragraph(escape(str(x)),styles['CellB']) for x in row] for row in rows]
    obj=Table(values,colWidths=widths,repeatRows=1,hAlign='LEFT')
    obj.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#172f45')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#eef4f6')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),
        ('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story.append(obj);story.append(Spacer(1,10))

para('DYN-VALIDEX<br/>Pont déterministe idéal [1,2]','TitleB',True)
para('Édition de dépôt 0.2 - 6 octobre 2026 | DOI : 10.5281/zenodo.23188815','SmallB')
heading('Un compact traité entièrement par calcul déterministe')
para('La partition du premier rang et des extrêmes est complète sur 1 ≤ a ≤ 2. Le rang vaut 0 ou 1 et le premier support contient au plus trois points. L’espérance est réduite analytiquement avant la quadrature ; aucun échantillonnage, aucune statistique ni flux RNG scientifique ne sont employés.')
equation('I<sub>[1,2]</sub> = ∫<sub>1</sub><sup>2</sup> a G(a) da<br/><b>0,234689097597 ≤ I<sub>[1,2]</sub> ≤ 0,234689433430</b>')
para('Les décimales sont arrondies vers l’extérieur. La largeur de cet intervalle affiché vaut 0,000000335833, soit moins de 3,36 × 10⁻⁷. Les bornes rationnelles exactes sont conservées dans le dossier. Il s’agit des unités de l’intégrale idéale non normalisée, sans facteur 6/π².')
table(['Résultat','Justification','Portée'],[
 ['Partition exacte','Neuf cellules auxiliaires (r,q), rang et modulo','Tiré-en-arrière sur toutes coordonnées admissibles de [1,2]'],
 ['Espérance G(a)','Moyenne uniforme des extrêmes et conditionnement','Loi idéale continue Pₐ'],
 ['Encadrement du pont','Deux codes rationnels, reste de Simpson borné','Compact idéal [1,2]'],
 ['Registre global','Sept UNKNOWN/null conservés','Aucun C global ou raccord canonique']],[104,187,184])
heading('Statut de validation')
para('Dérivations indépendantes et contrelecture IA interne achevées. L’encadrement dépend des définitions du modèle et des preuves de réduction et de dérivées données ici. La revue Codex reçue accepte B01–B05 sous ces hypothèses. La revue humaine extérieure reste à effectuer ; aucune certification par assistant de preuve formelle n’est revendiquée.')
para('Projet : Patrick Royer, chercheur indépendant non affilié. Développement, vérification et intégration finale avec ChatGPT/Codex et relectures IA distinctes. Outils libres employés : Python, fractions.Fraction, math.isqrt, ReportLab et Poppler.','SmallB')

page();heading('1. Modèle et partition du premier rang')
equation('1 ≤ a ≤ 2 ; 0 ≤ δ &lt; 1/a ; 0 ≤ s, β &lt; a.<br/>d<sub>k</sub> = δ + k/a ; Λ<sub>k</sub> = s + kβ + aℤ.<br/>Occupation : Λ<sub>k</sub> ∩ [−√(2d<sub>k</sub>), √(2d<sub>k</sub>)] ≠ ∅.')
para('Sous Pₐ, les trois coordonnées sont indépendantes et uniformes ; la boîte a un volume a et une densité conjointe 1/a. Le premier rang occupé k* détermine d et les extrêmes x₁ ≤ x₂. On pose c = d(x₂−x₁) − (x₂³−x₁³)/3 ; cette formule est nulle pour un seul point. G(a) = Eₚₐ[c]. Le support est fermé.')
equation('h = a²/8 ; r<sub>0</sub> = √(2δ).<br/><b>k* = 1 ⇔ δ &lt; h et r<sub>0</sub> &lt; s &lt; a − r<sub>0</sub>.</b><br/>k* = 0 dans tous les autres cas.')
para('Si δ < h, le support 0 est plus court que la maille et ses phases occupées sont [0,r₀] et [a−r₀,a), avec un point unique. Les contacts s=r₀ et s=a−r₀ appartiennent au rang 0. Si δ ≥ h, le support a une longueur au moins a, donc toute phase est occupée au rang 0.')
para('La ligne 1 est toujours occupée car 2δ+2/a ≥ 2/a ≥ a²/4 pour a ≤ 2. Si la ligne 0 est vide, le rang suivant est donc exactement 1. À δ=h, s=a/2 donne deux points et c=a³/24 ; les autres phases donnent un seul point. Ce contact est conservé dans la partition.')
heading('Phase et repliement')
equation('q = s pour k*=0.<br/>q = s+β si β &lt; a−s, et q = s+β−a si β ≥ a−s, pour k*=1.')
para('Dans tous les cas q ∈ [0,a). Le contact β=a−s donne q=0 dans la seconde branche ; pour s=0, cette branche est vide. Ces deux branches, la condition de rang et la table suivante donnent une partition complète dans (a,δ,s,β).')
para('À a=2, h=1/a est la borne supérieure exclue de δ : la branche δ≥h est vide. À a=2, δ=0 et s≠0, le rang vaut 1 et son rayon vaut a/2. La phase q=a/2 donne deux points ; toute autre phase donne un seul point.','SmallB')

page();heading('2. Les neuf cellules auxiliaires, contacts inclus')
para('Les neuf cellules partitionnent le plan auxiliaire (r,q). Leur composition avec le choix du rang et les branches du modulo donne la partition complète. Les points d’une ligne sont q+ja ; tout premier support satisfait 0 ≤ r < 3a/2. Les indices ci-dessous sont relatifs au représentant q ∈ [0,a). Une ligne vide ne peut pas être le premier support.')
table(['Régime du rayon','Phase q','Indices j inclus'],[
 ['0 ≤ r < a/2','0 ≤ q ≤ r','{0}'],
 ['0 ≤ r < a/2','r < q < a−r','∅'],
 ['0 ≤ r < a/2','a−r ≤ q < a','{−1}'],
 ['a/2 ≤ r < a','0 ≤ q < a−r','{0}'],
 ['a/2 ≤ r < a','a−r ≤ q ≤ r','{−1,0}'],
 ['a/2 ≤ r < a','r < q < a','{−1}'],
 ['a ≤ r < 3a/2','0 ≤ q ≤ r−a','{−1,0,1}'],
 ['a ≤ r < 3a/2','r−a < q < 2a−r','{−1,0}'],
 ['a ≤ r < 3a/2','2a−r ≤ q < a','{−2,−1,0}']],[139,187,149])
heading('Contributions polynomiales')
equation('{−1,0} : c = ad − aq² + a²q − a³/3.<br/>{−1,0,1} : c = 2ad − 2aq² − 2a³/3.<br/>{−2,−1,0} : c = 2ad − 2a(q−a)² − 2a³/3.')
para('Les branches à un point donnent c=0. À r=0, q=0 donne le point 0 ; la dernière cellule du premier régime est vide. À r=a/2, la cellule à deux points se réduit à q=a/2, avec c=a³/24. À r=a, q=0 donne {−1,0,1}, la dernière cellule est vide et 0<q<a donne {−1,0}.')
para('Au rang 0, (r₀/a)² < 2/a³ ≤ 2 < 9/4. Au rang 1 utilisé, δ<h, donc (r₁/a)² < 1/4+2/a³ ≤ 9/4. Ainsi r<3a/2 strictement : aucun premier support n’a quatre points. Le contact r=3a/2 exigerait a=1 et δ=h au rang 1, ce qui contredit la condition de rang.','SmallB')
para('Le seuil r₀=a est δ=a²/2, admissible seulement si a<∛2. Au rang 1, r₁=a correspond à δ=a²/2−1/a : ce seuil est négatif avant ∛2, nul à ∛2, intérieur à [0,h) entre ∛2 et ∛(8/3), puis exclu pour a≥∛(8/3).','SmallB')

page();heading('3. Moyenne de phase et espérance exacte')
para('Noter H(d,a) la moyenne de c sur q uniforme dans [0,a), en prenant c=0 pour une ligne vide. Si r=√(2d)<a/2, chaque ligne possède zéro ou un point : H=0. Si r≥a/2, chaque phase est occupée.')
para('Pour une phase uniforme, l’extrême droit est uniforme sur [r−a,r] et l’extrême gauche sur [−r,−r+a], à des contacts de mesure nulle près. Les extrêmes peuvent être corrélés. La linéarité et l’imparité de f_d(x)=d·x−x³/3 suffisent pour moyenner leur différence.')
equation('H(d,a) = (2/a) ∫<sub>r−a</sub><sup>r</sup> (d·x − x³/3) dx<br/>= (2/3)dr + ad − (2/3)a²r + a³/6<br/>= (2r−a)(r²+2ar−a²)/6, pour r ≥ a/2.')
para('Cette formule demeure valable quand r≥a et aux changements du nombre de points. À r=a/2, elle vaut 0 malgré la phase exceptionnelle à deux points : le singleton a une mesure continue nulle. Les contacts sont conservés dans la partition ; seule leur contribution à une intégrale continue est nulle.')
para('Lorsque δ<h, une ligne 0 occupée donne c=0. Son ensemble de phases vides a une longueur a−2√(2δ). Pour chaque s fixé, β uniforme rend (s+β) modulo a uniforme ; cela reste vrai après conditionnement sur la vacuité de la ligne 0, qui ne dépend pas de β.')
equation('G(a) = G<sub>0</sub>(a) + G<sub>1</sub>(a), h=a²/8.<br/>G<sub>0</sub>(a) = a ∫<sub>h</sub><sup>1/a</sup> H(d,a) dd.<br/>G<sub>1</sub>(a) = a ∫<sub>0</sub><sup>h</sup> (1−2√(2δ)/a) H(δ+1/a,a) dδ.')
para('Le facteur a est la densité marginale de δ. À a=2, la première intégrale est vide. La mesurabilité et la borne locale de c permettent les conditionnements et changements d’ordre d’intégration. Ces identités portent sur la loi idéale continue ; aucun résultat P2 n’intervient.')

page();heading('4. Une partie exacte, une intégrale lisse')
equation('Q(d,a) = (4√2/15)d<sup>5/2</sup> + (a/2)d²<br/>− (4√2/9)a²d<sup>3/2</sup> + (a³/6)d.')
para('La dérivation terme à terme donne ∂Q/∂d=H dans d≥h, et Q(h,a)=17a⁵/5760. La première branche de G devient donc explicite :')
equation('G<sub>0</sub>(a) = (4√2/15)a<sup>−3/2</sup> + 1/2<br/>− (4√2/9)a<sup>3/2</sup> + a³/6 − 17a⁶/5760.')
para('L’intégration exacte de aG₀ entre 1 et 2 fournit I₀. Pour la seconde branche, le changement δ=(a²/8)t² élimine la racine de δ à la frontière et fixe le domaine d’intégration.')
equation('I<sub>[1,2]</sub> = I<sub>0</sub> + I<sub>1</sub> ; I<sub>0</sub> = 233591/322560 − 128√2/315.<br/>I<sub>1</sub> = ∫<sub>1</sub><sup>2</sup> ∫<sub>0</sub><sup>1</sup> F(a,t) dt da.<br/>z = √(t²/4 + 2/a³),<br/>F = (a⁷/24)t(1−t)(2z−1)(z²+2z−1).')
para('Le radicand de z est au moins 1/4 ; l’intégrande est lisse sur un voisinage du rectangle fermé. Une seconde écriture, linéaire en une racine et utilisée par le code frugal, facilite les encadrements aux nœuds rationnels :')
equation('r = √(2/a + a²t²/4), w=t(1−t).<br/>F = w(Br+P),<br/>B = a³/6 + a⁶(t²−8)/48,<br/>P = a⁴/4 + a⁷(1+3t²/4)/24.')
para('I₀ ne demande que l’encadrement de √2. Les deux expressions de F sont algébriquement identiques : r=az. La première est évaluée par intervalles génériques dans un code ; la seconde par une combinaison affine de bornes de racine dans l’autre code.','SmallB')

page();heading('5. Bornes analytiques des dérivées quatrièmes')
para('Les coefficients normalisés sont vⱼ=(∂ʲv/∂xʲ)/j!, donc les produits se calculent par convolution sans coefficient binomial. Pour r²=q, r₁=q₁/(2r), puis rₙ=(qₙ−Σᵢ₌₁ⁿ⁻¹rᵢrₙ₋ᵢ)/(2r). Ici 1≤r≤3/2 sur le rectangle.')
heading('Selon a, t étant fixé')
table(['j','Majorant |rⱼ|','Majorant |Bⱼ|'],[
 [0,'3/2','12'],[1,'1','34'],[2,'9/8','41'],[3,'25/16','161/6'],[4,'277/128','10']],[50,190,235])
para('Ces bornes suivent des coefficients de q=2/a+a²t²/4 : q₁∈[−2,1], q₂∈[1/4,9/4], q₃∈[−2,−1/8], q₄∈[1/16,2]. Le coefficient 4 de P est borné par 1/4+245/12. La convolution donne |(Br+P)₄|≤6007/32 ; avec w≤1/4 et 4!=24 :')
equation('<b>|∂<sub>a</sub><sup>4</sup>F| ≤ 18021/16.</b>')
heading('Selon t, a étant fixé')
para('Poser A=2/a∈[1,2], D=a²/4∈[1/4,1]. Les majorants de |rⱼ| pour j=0,…,4 sont (3/2,1,1/2,1/2,1/2). En particulier r₂=AD/(2r³)≤D/(2√A)≤1/2, puisque r²≥A. Les coefficients de B vérifient |B₀|≤28/3, |B₁|≤8/3, |B₂|≤4/3, les suivants étant nuls.')
para('Pour T=Br : |T₂|≤28/3, |T₃|≤22/3, |T₄|≤20/3. Les coefficients de w=t−t² sont bornés par 1/4,1,1. Le coefficient 4 de wT est donc borné par 55/3. Celui de wP vaut −a⁷/32, de module ≤4. D’où :')
equation('<b>|∂<sub>t</sub><sup>4</sup>F| ≤ 24(55/3+4) = 536.</b>')
para('La preuve détaillée de chaque intervalle et convolution figure dans PREUVE_PONT_IDEAL_1_2_v0_1.txt. La contrelecture a recalculé ces tableaux ; les bornes ne sont pas estimées par une grille de dérivées.','SmallB')

page();heading('6. Deux certificats de quadrature rationnelle')
equation('|I<sub>1</sub> − S<sub>Na</sub><sup>a</sup>S<sub>Nt</sub><sup>t</sup>F|<br/>≤ M<sub>a</sub>/(180Na⁴) + M<sub>t</sub>/(180Nt⁴).')
para('Na et Nt sont des nombres pairs de sous-intervalles, chaque axe ayant une longueur 1. La borne est celle de Simpson composite appliquée à chaque axe. Une décomposition télescopique utilise les poids positifs, de somme 1, pour additionner les deux erreurs sans dérivée mixte supplémentaire.')
table(['Certificat','Calcul','Encadrement extérieur'],[
 ['Frugal analytique','Na=Nt=80 ; 6561 nœuds ; Ma=18021/16, Mt=536','[0,234689037675 ; 0,234689488607]'],
 ['Contre-vérification par intervalles de Taylor','Na=1024, Nt=128 ; 132225 nœuds ; Ma=23189149, Mt=2452','[0,234689097597 ; 0,234689433430]']],[102,209,164])
para('Le second code calcule les bornes de dérivées par jets d’intervalles d’ordre 4 sur tout le rectangle, avec convolutions, inverse et racine positive ; le coefficient 4 est multiplié par 24. Ses majorants sont plus grossiers, compensés par une grille plus fine. La dérivation de G est commune : il s’agit de deux implémentations arithmétiques de vérification, pas de deux preuves indépendantes du modèle.')
para('Aux nœuds rationnels, n=isqrt(floor(qD²)) fournit n/D≤√q≤(n+1)/D, avec égalité si le carré est exact. Le code frugal utilise D=10¹⁶ ; l’autre D=2⁶⁴. Les calculs de bornes utilisent uniquement entiers et fractions exactes. Les bornes sur les racines sont propagées avant l’ajout du reste de Simpson.')
para('Les intervalles rationnels se recouvrent ; celui de la contre-vérification est entièrement contenu dans le certificat frugal. L’intervalle adopté est leur intersection, identique au second. Le temps observé est inférieur à une seconde pour le code frugal et environ 14 secondes pour la contre-vérification ; ces durées sont des diagnostics de ce poste, sans portée scientifique.')
equation('<b>0,234689097597 ≤ I<sub>[1,2]</sub> ≤ 0,234689433430.</b><br/>Largeur extérieure affichée : 0,000000335833.')

page();heading('7. Vérifications, limites et revue reçue')
table(['Contrôle déterministe','Résultat'],[
 ['Table de phase contre énumération rationnelle','810 cas conformes'],
 ['Premier rang et contribution','2704 cas conformes'],
 ['Intégration polynomiale de phase contre H','40 intégrales exactes concordantes'],
 ['Contacts fermés explicitement enregistrés','65 contacts conformes'],
 ['Coefficients de Q(h) et I₀','17/5760 ; 233591/322560 ; −128/315'],
 ['Contrelectures des preuves et des codes','PASS interne ; revue Codex reçue, sous les hypothèses idéales']],[268,207])
para('Les cas finis accompagnent les preuves géométriques et algébriques ; ils ne les remplacent pas. Ce sont des configurations rationnelles construites pour contrôler la partition, sans mots bruts ni tirages archivés et sans ajout aux fixtures gelées P2. Aucun sampler, wrapper, enfant P2, PCG64, SeedSequence ou réplication scientifique n’est appelé.')
heading('Portée maintenue')
para('Ce pont établit un encadrement local pour la loi idéale continue écrite. Il ne rattache pas l’intégrale au modèle canonique, à C_mod ou au facteur 6/π². Il ne transporte aucune observation P2 vers le continu. Le transfert de loi reste UNBOUNDED ; I11/I13 restent INCONCLUSIVE ; les sept composantes et leurs bornes globales restent UNKNOWN/null.')
para('Les sources, les rapports antérieurs, les reçus P2 et le ledger gelé restent inchangés. Le registre de dépôt ZENODO_BRIDGE_EDITION_v0_2.json est distinct des registres historiques. Aucune valeur globale C, coefficient asymptotique ou conjecture n’est validé.')
heading('Dossier autonome pour la revue humaine')
para('Les compléments contiennent la preuve détaillée, la partition JSON, les trois scripts, les deux certificats, les contrôles de contacts et les documents de revue Codex. La revue humaine demandée porte sur les frontières, la densité, le conditionnement, I₀, les dérivées et le reste de Simpson ; ses verdicts sont à renseigner.')
para('Les hypothèses normatives du présent résultat sont définies à la section 1. La preuve historique intégrale, la partition et l’oracle rationnel sont joints. Le pont repose sur ses propres preuves, indépendamment des résultats descriptifs P2 ; aucune conformité du sampler ni normalisation canonique n’est ajoutée.','SmallB')


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

def footer(c,doc):
    c.saveState();c.setStrokeColor(colors.HexColor('#d5e1e7'));c.line(60,42,535,42)
    c.setFont('DV',7.5);c.setFillColor(colors.HexColor('#485864'))
    c.drawString(60,29,'Pont idéal [1,2] v0.2 | DOI : 10.5281/zenodo.23188815')
    c.drawRightString(535,29,str(doc.page));c.restoreState()

doc=SimpleDocTemplate(str(OUT/'01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf'),pagesize=(595.276,841.89),
    rightMargin=60,leftMargin=60,topMargin=57,bottomMargin=59,
    title='DYN-VALIDEX - Pont idéal [1,2] - DOI 10.5281/zenodo.23188815',author='Patrick Royer')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'pdf':str(OUT/'01_PONT_IDEAL_1_2_DOI_23188815_v0_2.pdf')}))
