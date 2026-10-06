# Journal — REPRODUCTION_DETERMINISTE_CODEX_PONT_1_2_2026-10-06

## Qualification

Contrôle déterministe séparé du pont idéal local `[1,2]`. Ce travail n'est ni
une réplication scientifique P2, ni une campagne, ni un rééchantillonnage.
Aucune API RNG ni aucun flux scientifique/modèle n'a été appelé. Aucun sampler,
worker, `run_p2`, wrapper ou ledger n'a été appelé ou modifié. La nuance du
secret de hachage CPython et sa neutralisation dans la série finale sont
consignées ci-dessous.

Les trois programmes fournis ont été copiés dans ce dossier avant exécution.
Leur SHA-256 est identique, octet pour octet, à celui des scripts de la copie de
travail en lecture seule :

- `certify_bridge_frugal.py` — `BAD0985CB3B6329F76FAC89B6BB3C3D6F2CC73DF71871028616451033F4112FA`
- `certify_bridge_interval.py` — `8357E83ABF79E9B56A4B92082927CCCF570E7E3B3BDA00D1F122A588A8245717`
- `verify_bridge_partition.py` — `493E0A3D3EF643716FF0D790DCB37C540689C1806C515D9F32ECEAB30F45E8E0`

## Opérations exécutées

Environnement de la série finale : Python embarqué Codex, option `-B`,
`PYTHONDONTWRITEBYTECODE=1` et `PYTHONHASHSEED=0`.

1. `python -B certify_bridge_frugal.py`
   - statut : `RATIONAL_ENCLOSURE_CONDITIONAL_ON_COMPANION_PROOF` ;
   - 6 561 nœuds ;
   - intervalle décimal sortant :
     `[0.234689037675, 0.234689488607]`.
2. `python -B certify_bridge_interval.py --output CERTIFICATE_INTERVAL_REPRODUCED.json`
   - statut : `PASS_RATIONAL_IDEAL_BRIDGE_ENCLOSURE` ;
   - grille `1024 x 128`, 132 225 nœuds ;
   - intervalle décimal sortant à 9 places :
     `[0.234689097, 0.234689434]`.
3. `python -B verify_bridge_partition.py`
   - statut : `PASS_EXACT_BRIDGE_PARTITION_CHECKS` ;
   - 810 cas géométriques ;
   - 2 704 cas de rang et contribution ;
   - 40 intégrales de phase ;
   - 65 contacts fermés.
4. `python -B verify_certificate_relationships_codex.py`
   - statut : `PASS` ;
   - 20 contrôles exacts vrais ;
   - calcul uniquement par entiers, `fractions.Fraction`, comparaison JSON et
     SHA-256 ; aucune décision par flottant.

Les durées renvoyées par `time.monotonic()` ou `time.perf_counter()` ne
participent à aucun calcul d'encadrement et sont les seuls champs volontairement
ignorés lors de la comparaison des deux certificats reproduits avec les
originaux. La sortie de partition est identique comme arbre JSON à l'original ;
sa représentation octet peut différer par les fins de ligne.

Les premiers lancements techniques n'avaient pas fixé `PYTHONHASHSEED` ; le
démarrage de CPython pouvait donc lire de l'entropie système pour son secret
interne de hachage. Aucune API RNG ni aucun flux scientifique/modèle n'a été
appelé, et aucun tel octet n'entre dans les calculs. Toute la série finale a été
réexécutée avec `PYTHONHASHSEED=0` ; les résultats exacts sont inchangés hors
durées diagnostiques.

## Résultats du contre-contrôle exact

Les 20 assertions suivantes ont été vérifiées :

- identité SHA-256 des trois scripts copiés ;
- identité des deux certificats avec leurs originaux, hors durée diagnostique ;
- identité sémantique de la sortie de partition ;
- comptes de nœuds `(N+1)^2` et `(Na+1)(Nt+1)` ;
- deux formules exactes de reste Simpson ;
- conversion des coefficients de jet d'ordre 4 par `4! = 24` vers
  `Ma = 23189149` et `Mt = 2452` ;
- encadrement de `I0` par comparaison rationnelle et élévation au carré exacte ;
- inclusion stricte du certificat par intervalles dans le certificat frugal ;
- identité de l'intervalle adopté avec le certificat par intervalles ;
- exactitude de la largeur rationnelle ;
- planchers/plafonds décimaux sortants à 9 et 12 places ;
- exactitude de la largeur affichée à 12 places ;
- cohérence des drapeaux d'absence de RNG, campagne, P2 et promotion de ledger.

Le détail machine lisible se trouve dans
`CERTIFICATE_RELATIONSHIPS_CODEX.json`.

## Intégrité des sources

La comparaison SHA-256 récursive entre le dossier original sous `Downloads` et
la copie de travail a porté sur 43 fichiers de chaque côté : zéro différence.
Les deux ledgers comparés ont le même SHA-256 :
`BADA7162048FEB6AA313FA2183F3634407ED1FB1493ED2E4978E54DC2D944705`.
