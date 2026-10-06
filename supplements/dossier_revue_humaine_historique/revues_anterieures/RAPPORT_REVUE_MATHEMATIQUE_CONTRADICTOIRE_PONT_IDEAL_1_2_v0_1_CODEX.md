# Revue mathématique contradictoire — Pont idéal déterministe `[1,2]` v0.1

**Date de la revue :** 6 octobre 2026  
**Objet :** vérifier les revendications B01–B05 du dossier autonome
`DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1`, depuis les définitions sources, sans
RNG, échantillonnage, campagne ni promotion du registre global.  
**Nature de la revue :** revue contradictoire Codex, assistée par calcul exact.
Ce document n'est ni une revue humaine par les pairs, ni une formalisation dans
un assistant de preuve.

## 1. Décision synthétique

Sous les hypothèses précises énoncées à la section 2, les cinq revendications
sont **acceptées**. Aucune réfutation ni divergence mathématique bloquante n'a
été trouvée.

| Revendication | Décision | Portée et réserve déterminantes |
|---|---|---|
| B01 — rang et partition | **Acceptée** | Pour tous les paramètres réels admissibles, support spatial fermé. Les neuf cellules sont celles du plan auxiliaire `(r,q)` ; la partition complète en `(a,delta,s,beta)` est leur tiré-en-arrière par le rang et le repliement. |
| B02 — moyenne de phase `H` | **Acceptée** | Les deux extrêmes n'ont pas à être indépendants : seules leurs marges uniformes et la linéarité de l'espérance sont utilisées. |
| B03 — formule de `G` et réduction rectangulaire | **Acceptée** | Sous la loi produit continue idéale uniquement. Le conditionnement conserve l'uniformité de `beta`, puis de la phase repliée. |
| B04 — régularité, dérivées et Simpson | **Acceptée** | Les bornes analytiques `Ma=18021/16`, `Mt=536` et les bornes par jets `Ma=23189149`, `Mt=2452` sont valides ; les jets sont normalisés par `j!`, d'où le facteur `4!=24`. |
| B05 — encadrement rationnel | **Acceptée, conditionnellement au modèle idéal local** | L'encadrement exact est démontré par arithmétique rationnelle dirigée, et non par concordance flottante. Il ne donne aucune constante globale ou canonique. |

La conclusion numérique certifiée est strictement locale et non normalisée :

\[
  0.234689097597
  \;\le\;
  I_{[1,2]}=\int_1^2 a\,\mathbb E_{P_a}[c]\,da
  \;\le\;
  0.234689433430.
\]

Les deux décimaux sont des arrondis **vers l'extérieur** des bornes
rationnelles exactes. Ils ne sont pas un intervalle de confiance et ne
proviennent d'aucune observation aléatoire.

## 2. Hypothèses et définition effectivement vérifiées

Les conclusions valent sous les hypothèses suivantes, et seulement sous elles.

1. `a` est réel et `1 <= a <= 2`.
2. Les représentants sont
   \[
   0\le\delta<1/a,\qquad 0\le s<a,\qquad 0\le\beta<a,
   \]
   indépendants, avec lois uniformes continues.
3. À la ligne entière `k>=0`,
   \[
   d_k=\delta+\frac{k}{a},\qquad
   x_j=s+k\beta+ja\quad(j\in\mathbb Z).
   \]
   Les points retenus satisfont
   \[
   x_j\in[-\sqrt{2d_k},\sqrt{2d_k}],
   \]
   intervalle spatial **fermé** : les contacts sont inclus.
4. `k_*` est la première ligne contenant au moins un point. Si `x_min` et
   `x_max` sont les extrêmes de cette première ligne,
   \[
   c=d_{k_*}(x_{\max}-x_{\min})-\frac{x_{\max}^3-x_{\min}^3}{3};
   \]
   un singleton a donc `c=0`. Pour définir une moyenne auxiliaire de ligne,
   on prolonge également `c` par zéro sur une phase vide.
5. La quantité examinée est
   \[
   I_{[1,2]}=\int_1^2 a\,G(a)\,da,
   \qquad G(a)=\mathbb E_{P_a}[c].
   \]
   Elle est exprimée dans les unités idéales d'origine, sans facteur
   `6/pi^2` et sans normalisation canonique.

Pour `a` fixé, la densité de `delta` est `a`, et celles de `s` et `beta` sont
chacune `1/a`. La densité jointe relativement à `d delta ds d beta` vaut donc

\[
a\times\frac1a\times\frac1a=\frac1a.
\]

Il faut distinguer les domaines demi-ouverts des trois représentants et le
support **spatial** fermé des lignes. En particulier, à `a=2`, le point
`delta=1/a=1/2` n'est pas admissible, même si `1/2` appartient à la fermeture
topologique de l'intervalle des valeurs de `delta`.

Les sources normatives utilisées sont
`evidence/model_definition_PROTOCOLE_P2_FRUGAL_DESCRIPTIF.txt` (notamment les
lignes 84–85) et `evidence/model_definition_oracle_rational.py`. La preuve,
les résultats, les certificats et les relectures IA ont été traités comme des
objets à contrôler, non comme des autorités.

## 3. Pièces et opérations réellement examinées

### 3.1 Corpus principal

Ont été lus et confrontés :

- le PDF de huit pages `DYN-PONT_IDEAL_DETERMINISTE_1_2_v0_1.pdf`, rendu page
  par page et contrôlé visuellement ;
- `PREUVE_PONT_IDEAL_1_2_v0_1.txt` ;
- `PARTITION_EXACTE.json` et `BRIDGE_IDEAL_RESULTS.json` ;
- `certificates/CERTIFICATE_FRUGAL_ANALYTIC.json` et
  `certificates/CERTIFICATE_INTERVAL_TAYLOR.json` ;
- les trois programmes de `code/` ;
- `verification/PARTITION_CHECKS.json`, les deux revues indépendantes de
  formule et certificat, utilisées seulement comme éléments contradictoires ;
- la définition normative, l'oracle rationnel et le ledger gelé sous
  `evidence/` ;
- `README.txt`, `VALIDATION.json`, les identités d'entrée et le manifeste du
  dossier pour le contexte de provenance.

Le PDF et la preuve texte portent les mêmes formules centrales. Aucun élément
mathématique n'a été accepté sur la seule foi du statut `PASS` d'un JSON.

### 3.2 Intégrité et absence de mutation

Le dossier original sous `Downloads` a été utilisé en lecture seule. Une copie
de travail distincte a été créée. Une comparaison récursive SHA-256 des deux
arbres a trouvé **43 fichiers de chaque côté et zéro différence** après la
revue.

Le ledger gelé du pont et le ledger antérieur comparé ont le même SHA-256 :

```text
BADA7162048FEB6AA313FA2183F3634407ED1FB1493ED2E4978E54DC2D944705
```

Cela atteste l'identité des deux fichiers examinés ; cela ne prétend pas
observer des fichiers extérieurs au corpus.

### 3.3 Reproductions déterministes séparées

La série d'opérations a été nommée
`REPRODUCTION_DETERMINISTE_CODEX_PONT_1_2_2026-10-06`. Elle n'est pas qualifiée
de réplication scientifique P2. Les trois scripts ont d'abord été copiés dans
un dossier distinct ; leurs SHA-256 concordent octet pour octet avec les
sources :

```text
certify_bridge_frugal.py
BAD0985CB3B6329F76FAC89B6BB3C3D6F2CC73DF71871028616451033F4112FA

certify_bridge_interval.py
8357E83ABF79E9B56A4B92082927CCCF570E7E3B3BDA00D1F122A588A8245717

verify_bridge_partition.py
493E0A3D3EF643716FF0D790DCB37C540689C1806C515D9F32ECEAB30F45E8E0
```

La série finale consignée a été exécutée avec Python `-B`,
`PYTHONDONTWRITEBYTECODE=1` et `PYTHONHASHSEED=0` :

- partition : `PASS_EXACT_BRIDGE_PARTITION_CHECKS`, 810 cas géométriques,
  2 704 cas rang/contribution, 40 intégrales de phase et 65 contacts fermés ;
- certificat frugal : 6 561 nœuds, intervalle sortant
  `[0.234689037675, 0.234689488607]` ;
- certificat par intervalles : 132 225 nœuds, intervalle sortant à neuf places
  `[0.234689097, 0.234689434]`.

Un quatrième programme indépendant, écrit pour cette revue, a ensuite testé
20 relations par entiers et `fractions.Fraction` : égalité des sorties hors
temps diagnostique, restes, jets, inclusion, radical exact, largeurs et
arrondis dirigés. Les 20 assertions sont vraies. Son résultat est conservé
dans `reproductions_bridge_ideal_1_2_codex/CERTIFICATE_RELATIONSHIPS_CODEX.json`.

Les seules valeurs flottantes émises par les programmes sont des durées
diagnostiques de `time.monotonic()` ou `time.perf_counter()` ; elles n'entrent
dans aucune décision d'encadrement.

Aucune API RNG, aucun sampler, worker, `run_p2`, wrapper, flux `PCG64`,
`SeedSequence`, campagne, resampling ou tirage scientifique n'a été importé,
instancié ou appelé par les codes examinés. Les premiers lancements techniques
n'avaient pas fixé `PYTHONHASHSEED` ; CPython pouvait donc lire de l'entropie
système pour son seul secret interne de hachage. Aucun octet correspondant
n'entre dans les calculs, certificats ou mots P2. La série finale a été refaite
avec `PYTHONHASHSEED=0` et a produit les mêmes résultats exacts hors temps
diagnostique. Aucun original, certificat original ou ledger n'a été modifié.

## 4. Vérification détaillée des neuf points

### 4.1 Point 1 — densité, support, rang, contacts et repliement

Posons

\[
h=\frac{a^2}{8},\qquad r_0=\sqrt{2\delta}.
\]

Si `delta<h`, alors `r0<a/2`. À la ligne 0, la phase est `q0=s` et la ligne
est occupée exactement sur

\[
[0,r_0]\cup[a-r_0,a).
\]

Elle est donc vide exactement lorsque

\[
r_0<s<a-r_0.
\]

Les inégalités sont strictes parce que les deux contacts `s=r0` et
`s=a-r0` appartiennent au support spatial fermé. Si `delta>=h`, alors
`r0>=a/2` et les deux arcs couvrent toutes les phases : la ligne 0 est toujours
occupée.

Lorsque la ligne 0 est vide, le rayon de la ligne suivante satisfait

\[
r_1^2=2\left(\delta+\frac1a\right)
\ge\frac2a\ge\frac{a^2}{4},
\]

la dernière inégalité équivalant à `a^3<=8`. Toute phase de la ligne 1 est
alors occupée. Ainsi, pour tous les paramètres admissibles,

\[
k_*\in\{0,1\}.
\]

La phase de la ligne 1 est le repliement

\[
q_1=(s+\beta)\bmod a=
\begin{cases}
s+\beta,&0\le\beta<a-s,\\
s+\beta-a,&a-s\le\beta<a.
\end{cases}
\]

Pour `s>0`, le contact `beta=a-s` est dans la seconde branche et donne
`q1=0`. Pour `s=0`, ce contact demanderait `beta=a`, valeur exclue.

Au bord `a=2`, on a `h=1/a=1/2`, mais la valeur supérieure de `delta` est
exclue. Pour `delta=0,s=0`, le premier rang est 0 ; pour
`delta=0,0<s<2`, il est 1. Dans ce dernier cas `r1=a/2`, et seule la phase
`q1=a/2` contient les deux contacts ; toutes les autres phases contiennent un
singleton.

**Décision du point 1 : acceptée.**

### 4.2 Point 2 — neuf cellules, seuils et trois points au plus

Pour une ligne de rayon `r` et de phase `q in [0,a)`, les indices présents sont

\[
j_{\min}=\left\lceil\frac{-r-q}{a}\right\rceil,
\qquad
j_{\max}=\left\lfloor\frac{r-q}{a}\right\rfloor.
\]

La table suivante est disjointe et exhaustive pour `0<=r<3a/2`. Les bornes
fermées sont celles dictées par le support fermé.

| Régime | Phase | Indices occupés | Contribution |
|---|---|---|---|
| `0<=r<a/2` | `0<=q<=r` | `{0}` | `0` |
|  | `r<q<a-r` | aucun | `0` par convention auxiliaire |
|  | `a-r<=q<a` | `{-1}` | `0` |
| `a/2<=r<a` | `0<=q<a-r` | `{0}` | `0` |
|  | `a-r<=q<=r` | `{-1,0}` | `ad-aq^2+a^2q-a^3/3` |
|  | `r<q<a` | `{-1}` | `0` |
| `a<=r<3a/2` | `0<=q<=r-a` | `{-1,0,1}` | `2ad-2aq^2-2a^3/3` |
|  | `r-a<q<2a-r` | `{-1,0}` | `ad-aq^2+a^2q-a^3/3` |
|  | `2a-r<=q<a` | `{-2,-1,0}` | `2ad-2a(q-a)^2-2a^3/3` |

Les trois polynômes ont été recalculés directement depuis les deux extrêmes.
Deux contacts sensibles donnent bien :

\[
r=\frac a2,\ q=\frac a2:\qquad c=\frac{a^3}{24},
\]

et

\[
r=a,\ q=0:\qquad \{-1,0,1\},\qquad c=\frac{a^3}{3}.
\]

Le rayon du premier support reste strictement inférieur à `3a/2` :

\[
\left(\frac{r_0}{a}\right)^2
 =\frac{2\delta}{a^2}<\frac2{a^3}\le2<\frac94,
\]

et, au rang 1 effectivement utilisé, `delta<h`, donc

\[
\left(\frac{r_1}{a}\right)^2
 <\frac14+\frac2{a^3}\le\frac94.
\]

La conclusion `(r1/a)^2<9/4` reste stricte même à `a=1` : la seconde
inégalité y devient une égalité, mais la première reste stricte parce que
`delta<h`. Quatre points sont donc impossibles au premier rang.

Les seuils sont exacts :

- rang 0 : `r0=a` équivaut à `delta=a^2/2`, admissible exactement lorsque
  `a<cuberoot(2)` ; à l'égalité `a=cuberoot(2)`, on tombe sur la borne exclue
  `delta=1/a` ;
- rang 1 : `r1=a` équivaut à
  \[
  \delta=b(a)=\frac{a^2}{2}-\frac1a.
  \]
  `b<0` avant `cuberoot(2)`, `b=0` à ce seuil, `0<b<h` jusqu'à
  `cuberoot(8/3)`, `b=h` à ce second seuil — donc valeur exclue au rang 1 —,
  puis `b>h`.

**Clarification :** « neuf cellules » désigne cette partition en `(r,q)`, et
non neuf sous-ensembles globaux de l'espace à quatre paramètres. Après choix du
rang et repliement de `q1`, leur tiré-en-arrière fournit bien tous les cas du
modèle.

**Décision du point 2 : acceptée avec cette clarification de vocabulaire.**

### 4.3 Point 3 — moyenne `H` sans indépendance des extrêmes

Soit

\[
F_d(x)=dx-\frac{x^3}{3}.
\]

Pour `r>=a/2`, toute phase est occupée. Lorsque `q` est uniforme sur `[0,a)`,
l'extrême droit est uniforme sur `(r-a,r]` et l'extrême gauche sur
`[-r,-r+a)`. Ces variables peuvent être dépendantes : la preuve utilise
uniquement

\[
\mathbb E[F_d(x_{\max})-F_d(x_{\min})]
=\mathbb E[F_d(x_{\max})]-\mathbb E[F_d(x_{\min})].
\]

Comme `F_d` est impaire,

\[
H(d,a)=\frac2a\int_{r-a}^{r}F_d(x)\,dx
=\frac23dr+ad-\frac23a^2r+\frac{a^3}{6}.
\]

Dans le domaine du pont, cette dérivation couvre notamment `a<=r<3a/2` et les
phases à trois points ; l'argument marginal vaut plus généralement pour tout
`r>=a/2`. À `r=a/2`, la phase isolée `q=a/2` a une contribution non nulle,
mais elle est de mesure continue nulle ; la formule donne bien `H=0`. À `r=a`,
elle donne `H=a^3/3`. Pour `r<a/2`, toutes les phases sont vides ou singletons,
donc `H=0` sous la convention auxiliaire.

En posant `z=r/a`, on obtient aussi

\[
H=a^3p(z),\qquad
p(z)=\frac{2z^3+3z^2-4z+1}{6}
=\frac{(2z-1)(z^2+2z-1)}{6}.
\]

**Décision du point 3 / B02 : acceptée.**

### 4.4 Point 4 — conditionnement, facteur de vacuité et formule de `G`

Pour `delta<h`, la ligne 0 est vide sur un intervalle de phases `s` de longueur
`a-2r0`. Ainsi

\[
\Pr(\text{ligne 0 vide}\mid\delta)
=1-\frac{2\sqrt{2\delta}}a.
\]

L'événement de vacuité dépend de `s` et `delta`, mais pas de `beta`.
Conditionnellement à cet événement et à chaque `s` fixé, `beta` reste uniforme ;
la translation modulo `a`

\[
q_1=(s+\beta)\bmod a
\]

est donc uniforme sur `[0,a)`. C'est la justification exacte de l'emploi de
`H(delta+1/a,a)` au rang 1.

En tenant compte de la densité marginale `a` de `delta`, on obtient

\[
G(a)=G_0(a)+G_1(a),
\]

\[
G_0(a)=a\int_h^{1/a}H(\delta,a)\,d\delta,
\]

\[
G_1(a)=a\int_0^h
\left(1-\frac{2\sqrt{2\delta}}a\right)
H\!\left(\delta+\frac1a,a\right)d\delta.
\]

À `a=2`, la première intégrale est vide. Aucun contact n'est supprimé dans la
classification ; les ensembles de contacts disparaissent seulement ensuite
des intégrales parce qu'ils ont mesure continue nulle.

Sous le changement de variable

\[
\delta=\frac{a^2t^2}{8},\qquad 0\le t\le1,
\]

on a

\[
d\delta=\frac{a^2}{4}t\,dt,\qquad
1-\frac{2\sqrt{2\delta}}a=1-t,
\]

et

\[
z=\frac{r_1}{a}=\sqrt{\frac{t^2}{4}+\frac2{a^3}}.
\]

Par conséquent,

\[
G_1(a)=\frac{a^6}{4}\int_0^1 t(1-t)p(z)\,dt.
\]

**Décision du point 4 : acceptée.**

### 4.5 Point 5 — primitive `Q`, coefficient `17/5760` et `I0`

Une primitive en `d` de `H` est

\[
Q(d,a)=\frac{4\sqrt2}{15}d^{5/2}
+\frac a2d^2
-\frac{4\sqrt2}{9}a^2d^{3/2}
+\frac{a^3}{6}d.
\]

La dérivation terme à terme redonne `H`. À `h=a^2/8`, les quatre coefficients
rationnels sont

\[
\frac1{480}+\frac1{128}-\frac1{36}+\frac1{48}
=\frac{17}{5760},
\]

d'où `Q(h,a)=17a^5/5760` et

\[
G_0(a)=
\frac{4\sqrt2}{15}a^{-3/2}
+\frac12
-\frac{4\sqrt2}{9}a^{3/2}
+\frac{a^3}{6}
-\frac{17a^6}{5760}.
\]

Une primitive de `aG0(a)` est

\[
T(a)=\frac{8\sqrt2}{15}\sqrt a+\frac{a^2}{4}
-\frac{8\sqrt2}{63}a^{7/2}+\frac{a^5}{30}
-\frac{17a^8}{46080}.
\]

L'évaluation exacte donne

\[
I_0=T(2)-T(1)
=\frac{233591}{322560}-\frac{128\sqrt2}{315}.
\]

Ces identités ont été recalculées par arithmétique rationnelle ; aucune valeur
approchée de `sqrt(2)` n'est nécessaire pour les établir.

**Décision du point 5 : acceptée.**

### 4.6 Point 6 — deux formes de `F`, lissité et bornes analytiques

La partie rectangulaire est

\[
I_1=\int_1^2\int_0^1 F(a,t)\,dt\,da,
\]

avec

\[
F(a,t)=\frac{a^7}{24}t(1-t)(2z-1)(z^2+2z-1),
\quad z=\sqrt{\frac{t^2}{4}+\frac2{a^3}}.
\]

Posons

\[
r=az=\sqrt{\frac2a+\frac{a^2t^2}{4}},\qquad w=t(1-t).
\]

L'expansion donne d'abord

\[
F=w\left(\frac{a^4r^3}{12}+\frac{a^5r^2}{8}
-\frac{a^6r}{6}+\frac{a^7}{24}\right).
\]

En remplaçant `r^2` par `2/a+a^2t^2/4`, on obtient exactement

\[
F=w(Br+P),
\]

\[
B=\frac{a^3}{6}+\frac{a^6(t^2-8)}{48},
\qquad
P=\frac{a^4}{4}+\frac{a^7(1+3t^2/4)}{24}.
\]

Les deux écritures sont donc identiques.

Sur `[1,2]x[0,1]`, le radicand de `z` est au moins `1/4`, et celui de `r` est
compris entre `1` et `9/4`. La racine positive est analytique sur un voisinage
ouvert du rectangle fermé ; `F` y est donc analytique.

Les calculs de dérivées utilisent des coefficients de jets normalisés

\[
X_j=\frac1{j!}\partial^jX.
\]

Pour les dérivées en `a`, les bornes contrôlées sont

\[
(|r_0|,\ldots,|r_4|)
\le\left(\frac32,1,\frac98,\frac{25}{16},\frac{277}{128}\right),
\]

\[
(|B_0|,\ldots,|B_4|)
\le\left(12,34,41,\frac{161}{6},10\right).
\]

La borne utilisée pour le dernier terme est

\[
|P_4|\le\frac14+\frac{245}{12}.
\]

La convolution de Leibniz donne alors

\[
|(Br+P)_4|\le\frac{6007}{32}.
\]

Comme `0<=w<=1/4`,

\[
|F_4|\le\frac{6007}{128},
\qquad
|\partial_a^4F|\le4!\,\frac{6007}{128}
=\frac{18021}{16}.
\]

Pour les dérivées en `t`, les coefficients de `r` vérifient

\[
(|r_0|,\ldots,|r_4|)
\le\left(\frac32,1,\frac12,\frac12,\frac12\right).
\]

En notant `V=Br`, les bornes recalculées sont

\[
|V_2|\le\frac{28}{3},\quad
|V_3|\le\frac{22}{3},\quad
|V_4|\le\frac{20}{3}.
\]

Les coefficients normalisés de `w=t-t^2` ont les modules `1/4,1,1` aux
ordres utiles. Ils donnent `|(wV)_4|<=55/3`, tandis que
`|(wP)_4|<=4`. Ainsi

\[
|F_4|\le\frac{67}{3},
\qquad
|\partial_t^4F|\le4!\,\frac{67}{3}=536.
\]

Le facteur `4!=24` n'est donc ni optionnel ni doublement compté : les tableaux
bornent les coefficients normalisés, puis la règle de Simpson demande la
dérivée quatrième.

**Décision du point 6 : acceptée.**

### 4.7 Point 7 — jets d'intervalles et reste de Simpson

Le second code propage des intervalles rationnels et des séries tronquées
normalisées jusqu'à l'ordre 4. Le contre-calcul retrouve exactement

\[
(F_{a,4})\subset
\left[-\frac{23189149}{24},\frac{146820241}{192}\right],
\]

\[
(F_{t,4})\subset
\left[-\frac{613}{6},\frac{206}{3}\right].
\]

Après multiplication par `24`, les maxima des modules donnent

\[
M_a=23189149,\qquad M_t=2452.
\]

Pour un rationnel positif `x` et une échelle entière `D`, les codes calculent

\[
n=\operatorname{isqrt}\!\left(\left\lfloor xD^2\right\rfloor\right),
\]

puis utilisent `n/D` comme borne inférieure et `(n+1)/D` comme borne
supérieure, sauf si le carré est exact. Les assertions

\[
(n/D)^2\le x\le((n+1)/D)^2
\]

sont exactes. Le code frugal prend `D=10^16`; le code par intervalles prend une
échelle dyadique de 64 bits. Le signe de `B` est explicitement pris en compte
avant de multiplier l'intervalle de racine.

Pour Simpson composite sur `[0,1]` avec `N` pair,

\[
\left|\int_0^1f-S_Nf\right|
\le\frac{\max|f^{(4)}|}{180N^4}.
\]

La décomposition

\[
I_aI_t-S_aS_t=(I_a-S_a)I_t+S_a(I_t-S_t)
\]

et la positivité des poids normalisés de `S_a`, dont la somme vaut 1, donnent
sans terme mixte supplémentaire

\[
|I_1-S_{N_a,N_t}F|
\le\frac{M_a}{180N_a^4}+\frac{M_t}{180N_t^4}.
\]

Pour le certificat par intervalles,

\[
N_a=1024,\quad N_t=128,
\]

\[
e_a=\frac{23189149}{197912092999680},\qquad
e_t=\frac{613}{12079595520},
\]

\[
e_a+e_t=\frac{33232541}{197912092999680}.
\]

Le nombre de nœuds est

\[
(1024+1)(128+1)=132225.
\]

Pour le certificat frugal, `Na=Nt=80`, soit `81^2=6561` nœuds, et

\[
\frac{18021/16+536}{180\,80^4}
=\frac{26597}{117964800000}.
\]

Toutes les sommes de nœuds, bornes de racine et erreurs sont rationnelles.
Il n'existe aucun reste statistique.

**Décision du point 7 / B04 : acceptée.**

### 4.8 Point 8 — bornes rationnelles, inclusion et arrondis sortants

Le certificat par intervalles donne les deux bornes exactes suivantes :

```text
L =
882375542249540499823008261517811277366489157054732244055081165950402356632514642162938379
/
3759763667257987014694689795989965551159448500027948743849907665312285797414752319029903360

U =
176475360979196894225673049899726102935532720274190975751429938289648246636377214254762603
/
751952733451597402938937959197993110231889700005589748769981533062457159482950463805980672
```

Le radical de `I0` a été encadré et contrôlé sans flottant : pour
`I0=A-B sqrt(2)`, avec `A=233591/322560` et `B=128/315`, les deux inégalités
ont été ramenées à des comparaisons de rationnels positifs puis élevées au
carré.

Les comparaisons exactes de fractions donnent la chaîne stricte

\[
L_{\rm frugal}<L<U<U_{\rm frugal}.
\]

Le second certificat est donc strictement contenu dans le premier. Les bornes
adoptées par `BRIDGE_IDEAL_RESULTS.json` sont exactement `L` et `U`, et leur
différence est exactement

```text
105220536997608779748998401603109264537026351886225172377124819906379114285759239553
/
313313638938165584557890816332497129263287375002329061987492305442690483117896026585825280
```

Enfin, le calcul entier vérifie

\[
\frac{\lfloor10^{12}L\rfloor}{10^{12}}
=0.234689097597\le L,
\]

\[
U\le
\frac{\lceil10^{12}U\rceil}{10^{12}}
=0.234689433430.
\]

La largeur affichée vaut exactement

\[
\frac{335833}{10^{12}}.
\]

Le JSON du certificat par intervalles affiche seulement neuf décimales, tandis
que le JSON de synthèse en affiche douze à partir des **mêmes fractions**. Il ne
s'agit pas d'un resserrement par valeur flottante.

**Décision du point 8 / B05 : acceptée.**

### 4.9 Point 9 — unités, ledger et limites de transfert

La quantité encadrée est exactement l'intégrale idéale locale non normalisée
`integral_1^2 a E_Pa[c] da`. Les pièces examinées :

- n'appliquent aucun facteur `6/pi^2` ;
- ne calculent ni `C_mod`, ni `C_inf`, ni `B_global` ;
- laissent `continuous_law_transfer` à `UNBOUNDED` ;
- laissent `I11` et `I13` à `INCONCLUSIVE` ;
- laissent les sept composantes historiques à `UNKNOWN/null` ;
- ne valident ni la conjecture générale, ni un coefficient asymptotique, ni
  une constante globale.

Le ledger copié dans le bundle est identique au ledger antérieur contrôlé. La
revue n'a effectué aucune promotion et n'en recommande aucune sur la base de ce
seul pont.

**Décision du point 9 : acceptée.**

## 5. Objections, divergences exactes et limites

### 5.1 Absence de divergence normative bloquante

Aucune formule utilisée sur le domaine admissible ne diverge entre le protocole
normatif, la preuve et l'oracle. Les deux écarts de présentation suivants
doivent néanmoins rester explicites.

1. **Validation de `beta` dans l'oracle.** Le protocole impose
   `0<=beta<a`. Dans `model_definition_oracle_rational.py`, `row_extrema`
   contrôle `a`, `delta` et `s`, mais ne rejette pas explicitement une valeur de
   `beta` hors domaine. C'est une lacune de validation d'entrée, pas une
   divergence de calcul sur les paramètres admissibles. Toutes les conclusions
   de ce rapport s'arrêtent si l'oracle est invoqué comme définition autonome
   hors de ce domaine.
2. **Portée des neuf cellules.** Elles forment la partition exhaustive en
   `(r,q)`. Une affirmation littérale selon laquelle l'espace complet
   `(a,delta,s,beta)` ne contiendrait que neuf cellules serait fausse ; il faut
   composer avec le rang et les branches du modulo.

L'oracle ne représente directement que des rationnels ou des flottants finis.
Les affirmations « pour tous réels admissibles » proviennent des inégalités et
identités analytiques ci-dessus, non de l'énumération finie.

### 5.2 Ce que les programmes prouvent — et ne prouvent pas

Les 810, 2 704, 40 et 65 contrôles exacts détectent efficacement des erreurs de
table, de signe et de contact, mais une grille finie n'est pas une preuve pour
tous les réels. L'exhaustivité réelle vient des formules de `j_min`, `j_max`,
des coupures analytiques et des inégalités strictes.

Le certificat frugal encode les deux bornes de dérivées analytiques ; son statut
est donc justement conditionnel à leur preuve compagnon. Le certificat par
jets les réencadre indépendamment par intervalles, mais il dépend encore de la
réduction mathématique de B01–B03 vers `F`. Cette réduction et les bornes ont été
revérifiées dans la présente revue.

Une valeur flottante ponctuelle concordante n'a joué aucun rôle. La preuve de
l'encadrement repose sur des inclusions rationnelles, des poids positifs, des
bornes de reste et des arrondis entiers dirigés.

### 5.3 Statut de revue

Le champ original
`external_mathematical_review_of_this_bridge: NOT_RUN` n'a pas été modifié.
La situation après ce travail est à décrire exactement ainsi :

- revue contradictoire Codex documentée : **EFFECTUÉE** ;
- revue scientifique humaine externe : **NON ÉTABLIE PAR CE DOSSIER** ;
- vérification par assistant de preuve : **NOT_RUN**.

Un accord de plusieurs passes IA n'est pas pris comme preuve. Les décisions de
ce rapport sont fondées sur les dérivations reproduites et les comparaisons
exactes consignées. Une revue scientifique extérieure humaine reste souhaitable
avant toute promotion institutionnelle.

## 6. Conclusion finale et portée exacte

Le dossier démontre, sous la loi continue idéale et les conventions de support
fermées indiquées, que le premier rang sur `a in [1,2]` vaut toujours 0 ou 1,
que sa géométrie est couverte par la partition annoncée, que la réduction
analytique vers `I0+I1` est exacte, et que les deux quadratures déterministes
fournissent des encadrements rationnels compatibles dont le second est
strictement inclus dans le premier.

La seule conclusion quantitative autorisée est

\[
\boxed{
I_{[1,2]}\in[0.234689097597,\ 0.234689433430]
}
\]

avec arrondis vers l'extérieur.

Cette conclusion ne se transfère ni aux flux numériques P2, ni à une loi
dyadique, ni à une campagne archivée, ni à l'intégrale idéale globale. Elle ne
justifie aucun `6/pi^2`, aucun `C_mod`, aucun `C_inf`, aucun `B_global`, aucune
conjecture générale et aucune mise à jour du ledger scientifique global.

## 7. Artefacts produits par cette revue

- `RAPPORT_REVUE_MATHEMATIQUE_CONTRADICTOIRE_PONT_IDEAL_1_2_v0_1_CODEX.md`
  — présent rapport ;
- `reproductions_bridge_ideal_1_2_codex/REPRODUCTION_LOG.md` — journal séparé
  des opérations déterministes ;
- `reproductions_bridge_ideal_1_2_codex/CERTIFICATE_RELATIONSHIPS_CODEX.json`
  — résultat machine lisible des 20 comparaisons exactes ;
- `reproductions_bridge_ideal_1_2_codex/verify_certificate_relationships_codex.py`
  — source du quatrième contre-contrôle ;
- `reproductions_bridge_ideal_1_2_codex/certify_bridge_frugal.json`,
  `CERTIFICATE_INTERVAL_REPRODUCED.json` et
  `bridge_partition_checks_work.json` — trois sorties reproduites, distinctes
  de tous les originaux.
