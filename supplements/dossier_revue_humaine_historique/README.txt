DYN-VALIDEX — PAQUET DE REVUE HUMAINE DU PONT IDÉAL [1,2] v0.1
6 octobre 2026
Statut du paquet : READY_FOR_HUMAN_REVIEW.
Statut de la revue humaine : NOT_RUN ; aucun destinataire ni envoi enregistré.

OBJET
Ce dossier autonome demande un examen mathématique humain de B01–B05 pour
le seul modèle idéal continu explicitement défini dans la preuve. Il rassemble
la preuve, son PDF inchangé, la partition, les certificats rationnels, trois
programmes déterministes et les éléments de la revue Codex déjà reçue.
La préparation de ce dossier n'ajoute aucune preuve ou évaluation scientifique.

ORDRE DE LECTURE PROPOSÉ
1. NOTE_TRANSMISSION_REVUE_HUMAINE_v0_1.txt : objet, hypothèses et limites.
2. preuve/PREUVE_PONT_IDEAL_1_2_v0_1.txt, ou le PDF de même dossier.
3. CHECKLIST_REVUE_HUMAINE_v0_1.txt, puis preuve/PARTITION_EXACTE.json,
   certificats/ et code/ pour les points demandant une vérification détaillée.
4. revues_anterieures/ et statut/ après une première appréciation personnelle.
   Ces verdicts Codex apportent une contrelecture documentée, sans constituer
   une revue humaine ni une formalisation par assistant de preuve.
5. Renseigner une copie de FORMULAIRE_VERDICT_REVUE_HUMAINE_v0_1.txt.

GUIDE DES PIÈCES
preuve/ : texte mathématique complet, PDF et partition rationnelle.
certificats/ : deux encadrements exacts et résultats de contrôles finis.
code/ : trois scripts autonomes utilisant la bibliothèque standard Python.
modele/ : oracle rationnel fourni à titre de référence de coordonnées ; il
          n'importe pas le sampler et ne certifie aucune loi d'implémentation.
statut/ : registre distinct de la revue Codex, avec les limites globales.
revues_anterieures/ : rapport, journal et contre-contrôles reçus/confrontés.
STATUT_REVUE_HUMAINE_v0_1.json : état initial sans verdict humain renseigné.
COPIES_ET_PROVENANCE.json : origine et empreinte de chaque copie inchangée.
VALIDATION_DOCUMENTAIRE.json : contrôles de préparation du paquet.
BUNDLE_MANIFEST.json : tailles et SHA-256 du contenu, sauf ce manifeste.

LES STATUTS HISTORIQUES
Le texte/PDF de la preuve porte encore son statut antérieur de revue extérieure
NOT_RUN. Il est conservé tel quel. Le registre distinct dans statut/ et la note
d'intégration consignent la revue Codex reçue ensuite. La revue humaine reste
NOT_RUN dans ce nouveau paquet ; aucun ledger gelé n'est modifié.
Les renvois historiques vers verification/ concernent les contrelectures IA
internes du dossier source ; elles ne sont pas requises pour lire la preuve
autonome et ne sont pas dupliquées dans ce paquet minimal. Le code frugal nommé
bridge_expectation_derivation_work.py dans le texte est fourni ici sous son
nom de livraison code/certify_bridge_frugal.py.

REPRODUCTION DÉTERMINISTE FACULTATIVE
Une lecture de preuve peut suffire ; aucune exécution n'est requise par ce
dossier. Si le relecteur choisit de reproduire les trois calculs, copier d'abord
les trois scripts de code/ dans un dossier de travail neuf séparé, puis y fixer
PYTHONHASHSEED=0 et PYTHONDONTWRITEBYTECODE=1 dans l'environnement de Python.
Depuis ce dossier de copies, utiliser son interpréteur Python avec :
  python -B certify_bridge_frugal.py
  python -B certify_bridge_interval.py --output CERTIFICATE_INTERVAL_REPRODUCED.json
  python -B verify_bridge_partition.py
Le premier écrit certify_bridge_frugal.json à côté de sa copie ; le troisième
écrit bridge_partition_checks_work.json dans le répertoire courant. Les durées
sont diagnostiques et peuvent varier ; comparer les arbres JSON sans le champ
elapsed_seconds_diagnostic du certificat frugal et sans le champ
compute_elapsed_seconds_diagnostic du certificat par intervalles. Aucun quatrième script
de la revue Windows n'est fourni : sa source et les trois sorties reproduites
externes n'ont pas été reçues. Les sorties jointes sont les certificats et
contrôles originaux, pas ces copies de reproduction externes.
Ces scripts ne sont pas des procédures P2. Aucun n'a été relancé pour préparer
ce paquet. Aucun accès à un dossier Windows ou à une archive P2 n'est nécessaire.

Après réception d'un rapport humain, conserver ce paquet intact et rédiger un
complément distinct mentionnant le périmètre effectivement examiné, l'identité
du relecteur, la date et les éventuelles réserves. Aucune acceptation ne se
déduit de la seule absence de réponse.
