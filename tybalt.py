# Work with Python 3.7
from discord import Game
from discord.ext.commands import Bot
import numpy as np

BOT_PREFIX = "!"
TOKEN = 'XXXXXXXXXXXXXXXXX'

client = Bot(command_prefix=BOT_PREFIX)

infoRandos = {
    "Alcôve de Courtilleracine": {
        "carte": "Le Bosquet",
        "tp": "Point de passage du Spéculateur",
        "chatCode": "[&BLsEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-gardenroot-alcove-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-gardenroot-alcove-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-gardenroot-alcove-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-gardenroot-alcove-guild-trek-3.jpg"]
    },
    "Alimentation en eau d'Orvanic": {
        "carte": "Marais de Lumillule",
        "tp": "Point de passage du Goulet de l'Océan",
        "chatCode": "[&BMkBAAA=]",
        "aide": "Vous devrez prendre le passage de tunnel pour arriver à la cascade supérieure, suivrez les flèches sur la carte.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-orvanic-sourcewaters-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-orvanic-sourcewaters-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-orvanic-sourcewaters-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-orvanic-sourcewaters-guild-trek-3.jpg"]
    },
    "Antre cachécailleux": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage de Feritas",
        "chatCode": "[&BJcDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-skalestash-hideaway-guild-trek1.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalestash-hideaway-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalestash-hideaway-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalestash-hideaway-guild-trek-4.jpg"]
    },
    "Antre de Hurleneige": {
        "carte": "Congères d'Antreneige",
        "tp": "Point de passage de la Terrasse du Faucon des neiges",
        "chatCode": "[&BL8AAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-snowhowl-den-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowhowl-den-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowhowl-den-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowhowl-den-guild-trek-3.jpg"]
    },
    "Autel d'Inondesel": {
        "carte": "Marais de Lumillule",
        "tp": "Point de passage d'Inondesel",
        "chatCode": "[&BMcBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-saltflood-altar-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-saltflood-altar-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-saltflood-altar-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-saltflood-altar-guild-trek-4.jpg"]
    },
    "Aveuglement de l'Erudit": {
        "carte": "Falaises de HanteDraguerre",
        "tp": "Point de passage de la Crevasse de Toran",
        "chatCode": "[&BFwCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-scholars-blind1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scholars-blind-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scholars-blind-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scholars-blind-guild-trek-2.jpg"]
    },
    "Balcon des délices": {
        "carte": "Saut de Malchor",
        "tp": "Point de passage de Pagga",
        "chatCode": "[&BKYCAAA=]",
        "aide": "Le balcon se situe tout en haut au sommet, vous pouvez y accéder via un petit jumping puzzle (il suffit de suivre les points blancs)",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-delights-balcony-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-delights-balcony-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-delights-balcony-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-delights-balcony-guild-trek.jpg"]
    },
    "Banc de Varech de Malméduse": {
        "carte": "Congères d'Antreneige",
        "tp": "Point de passage de l'Exil",
        "chatCode": "[&BLwAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-badjelly-kelpbed-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-badjelly-kelpbed-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-badjelly-kelpbed-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-badjelly-kelpbed-guild-trek-2.jpg"]
    },
    "Barrière de Bercebruyère": {
        "carte": "Fôret de Caledon",
        "tp": "Point de passage de la Spirale",
        "chatCode": "[&BDUBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-briarthorn-barrier-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-briarthorn-barrier-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-briarthorn-barrier-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-briarthorn-barrier-guild-trek.jpg"]
    },
    "Belvédère goutedo": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage de la Complainte",
        "chatCode": "[&BOoAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-steamscrap-overlook-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-steamscrap-overlook-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-steamscrap-overlook-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-steamscrap-overlook-guild-trek-3.jpg"]
    },
    "Bistrot rouport": {
        "carte": "Citadelle noire",
        "tp": "Point de passage des Terres du rassemblement",
        "chatCode": "[&BKUDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-wheelport-pub-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-wheelport-pub-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-wheelport-pub-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-wheelport-pub-guild-trek-3.jpg"]
    },
    "Bivouac du Lys": {
        "carte": "Montée de Flambecoeur",
        "tp": "Point de passage de la Pointe de glace",
        "chatCode": "[&BCACAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lilys-bivvy-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lilys-bivvy-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lilys-bivvy-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lilys-bivvy-guild-trek-4.jpg"]
    },
    "Bord de Valaigu": {
        "carte": "Les Steppes de la Strie Flamboyante",
        "tp": "Point de passage de Behem",
        "chatCode": "[&BP0BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-sharkhollows-edge-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sharkhollows-edge-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sharkhollows-edge-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sharkhollows-edge-guild-trek-3.jpg"]
    },
    "Bosquet de Tarstar": {
        "carte": "Montée de Flambecoeur",
        "tp": "Point de passage de l'Apostat",
        "chatCode": "[&BB0CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-tarstar-copse-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tarstar-copse-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tarstar-copse-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tarstar-copse-guild-trek-3.jpg"]
    },
    "Boucherie piègecayeux": {
        "carte": "Marais de fer",
        "tp": "Point de passage du Village d'Attrapécaille",
        "chatCode": "[&BOcBAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-skalecatch-bucher-shop-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalecatch-bucher-shop-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalecatch-bucher-shop-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skalecatch-bucher-shop-guild-trek-3.jpg"]
    },
    "Cache à miel de Boisecoeur": {
        "carte": "Vallée de la Reine",
        "tp": "Point de passage du Camp de la passe de Boisecœur",
        "chatCode": "[&BPUAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-heartwoods-honey-cache-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heartwoods-honey-cache-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heartwoods-honey-cache-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heartwoods-honey-cache-guild-trek-3.jpg"]
    },
    "Cache de l'Ours des cavernes": {
        "carte": "Congères d'Antreneige",
        "tp": "Point de passage de la Terrasse du Faucon des neiges",
        "chatCode": "[&BL8AAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cave-bear-cache-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-bear-cache-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-bear-cache-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-bear-cache-guild-trek-3.jpg"]
    },
    "Cache du fugitif": {
        "carte": "Rivage Maudit",
        "tp": "Point de passage de Caer Mande-Ombre",
        "chatCode": "[&BCEDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cache-of-the-pursued-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cache-of-the-pursued-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cache-of-the-pursued-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cache-of-the-pursued-guild-trek-3.jpg"]
    },
    "Réserve du marchand": {
        "carte": "Hoelbrak",
        "tp": "Point de passage de Peeta",
        "chatCode": "[&BI8DAAA=]",
        "aide": "Pour atteindre et emplacement, suivez les flèches rouges, vous ne pouvez pas y atteindre du point de passage de la Place du commerce.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-traders-stash-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-traders-stash-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-traders-stash-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-traders-stash-guild-trek-2.jpg"]
    },
    "Camp principal du gardien": {
        "carte": "Harathi Hinterlands",
        "tp": "Point de passage du Camp de la barricade",
        "chatCode": "[&BK0AAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-guardian-overwatch-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-guardian-overwatch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-guardian-overwatch-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-guardian-overwatch-guild-trek-2.jpg"]
    },
    "Canyons de Gallow": {
        "carte": "Terres Sauvages de Brisban",
        "tp": "Point de passage des Champs de la potence",
        "chatCode": "[&BGMAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/161731canyonsdegallow.png", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-2.jpg"]
    },
    "Carré de chou du bandit": {
        "carte": "Harathi Hinterlands",
        "tp": "Point de passage de Point de ralliement de Wynchona",
        "chatCode": "[&BKgAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-bandits-cabbage-patch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-bandits-cabbage-patch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-bandits-cabbage-patch-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-bandits-cabbage-patch-guild-trek-4.jpg"]
    },
    "Cavité de la cathédrale": {
        "carte": "Saut de Malchor",
        "tp": "Point de passage de Lyssa",
        "chatCode": "[&BCYDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cathedrals-cavity1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cathedrals-cavity-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cathedrals-cavity-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cathedrals-cavity-guild-trek-2.jpg"]
    },
    "Cavité du Contremaître": {
        "carte": "Falaises de HanteDraguerre",
        "tp": "Point de passage de Dociu",
        "chatCode": "[&BFgCAAA=]",
        "aide": "Notez que pour arriver à la marque, vous devez sauter sur deux ou trois rampes vu qu'elle est placée au sommet.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-foremans-recess-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-foremans-recess-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-foremans-recess-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-foremans-recess-guild-trek-3.jpg"]
    },
    "Cellier de la Garde du Lion": {
        "carte": "Contrefort du Voyageur",
        "tp": "Point de passage du Refuge de Doubléperon",
        "chatCode": "[&BH0BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lionguard-larder-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lionguard-larder-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lionguard-larder-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lionguard-larder-guild-trek-2.jpg"]
    },
    "Cellier du Lion Noir": {
        "carte": "Le Bosquet",
        "tp": "Point de passage du Spéculateur",
        "chatCode": "[&BLsEAAA=]",
        "aide": "Pour avoir accès au cercle d'or en bas, vous devez sauter de la rampe près du marchand du Lion Noir.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-black-lion-root-cellar-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-black-lion-root-cellar-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-black-lion-root-cellar.jpg", "http://androuw.e-monsite.com/medias/images/gw2-black-lion-root-cellar-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-black-lion-root-cellar-guild-trek.jpg"]
    },
    "Champ de Montesauvage": {
        "carte": "Côte de la Marée Sanglante",
        "tp": "Point de passage Remanda",
        "chatCode": "[&BKcBAAA=]",
        "aide": "La zone exacte de l'emplacement de la randonnée de guilde demeure inconnue à ce jour.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-risewild-green1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-risewild-green-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-risewild-green-guild-trek1.jpg"]
    },
    "Champ de force de la cinquième brasse": {
        "carte": "Détroit de la Dévastation",
        "tp": "Point de passage de la Cloche vespérale",
        "chatCode": "[&BPICAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-fathom-five-forcefield-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fathom-five-forcefield-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fathom-five-forcefield-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fathom-five-forcefield-guild-trek-4.jpg"]
    },
    "Châtiment de Bluup": {
        "carte": "Rata Sum",
        "tp": "",
        "chatCode": "[&BLgEAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-bluups-comeuppance-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-bluups-comeuppance-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-bluups-comeuppance-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-bluups-comeuppance-guild-trek-3.jpg"]
    },
    "Chute d'East End": {
        "carte": "Terres Sauvages de Brisban",
        "tp": "Point de passage de l'Extrêmité Est",
        "chatCode": "[&BGAAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-east-end-falls-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-end-falls-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-end-falls-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-end-falls-guild-trek-2.jpg"]
    },
    "Chutes de Gerbécaille": {
        "carte": "Chute de la Canopée",
        "tp": "Point de passage d'Okarinoo",
        "chatCode": "[&BEYCAAA=]",
        "aide": "L'emplacement du cercle d'or n'est pas encore connu.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-skalesplash-falls-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalesplash-falls-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalesplash-falls-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalesplash-falls-guild-trek-3.jpg"]
    },
    "Chutes de la Génitrice": {
        "carte": "Détroit des Gorges Glacées",
        "tp": "Point de passage de la Courbe du Yak",
        "chatCode": "[&BIQCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-broodmother-falls-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broodmother-falls-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broodmother-falls-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broodmother-falls-guild-trek-2.jpg"]
    },
    "Cisaillement interdit": {
        "carte": "Saut de Malchor",
        "tp": "Point de passage des Murmures",
        "chatCode": "[&BK8CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-forbidden-shear-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-forbidden-shear-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-forbidden-shear-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-forbidden-shear-guild-trek-3.jpg"]
    },
    "Coeur du flacon du fondateur": {
        "carte": "Champs de Ruines",
        "tp": "Point de passage de Kestrel",
        "chatCode": "[&BD0EAAA=]",
        "aide": "Notez que la marque à activer est dans une des pièces dans le premier étage.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-founders-flagon-hearth-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-founders-flagon-hearth-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-founders-flagon-hearth-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-founders-flagon-hearth-guild-trek-3.jpg"]
    },
    "Coffre-fort de Kevach": {
        "carte": "Contreforts du Voyageur",
        "tp": "",
        "chatCode": "[&BMEDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-kevachs-strongroom-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kevachs-strongroom-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kevachs-strongroom-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kevachs-strongroom-guild-trek-3.jpg"]
    },
    "Coin d'Anya": {
        "carte": "Plateau de Diessa",
        "tp": "Point de passage de Nolan",
        "chatCode": "[&BN4AAAA=]",
        "aide": "Vous devez faire un petit puzzle jump pour arriver à cet endroit. Si vous ne trouvez pas, aller voir cette <a href=\"https://www.youtube.com/watch?v=FFNbnMoEMiY\" data-lity>vidéo</a>",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-anyas-patch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-anyas-patch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-anyas-patch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-anyas-patch-guild-trek-3.jpg"]
    },
    "Coin de Castavall": {
        "carte": "Côte de la Marée Sanglante",
        "tp": "Point de passage de Castavall",
        "chatCode": "[&BK4BAAA=]",
        "aide": "Du point de passage, ne nagez pas en bas ou en haut. Au lieu de cela, prenez le tunnel qui est parallèle à vous.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-castavall-corner-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-castavall-corner-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-castavall-corner-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-castavall-corner-guild-trek-3.jpg"]
    },
    "Coin de Magièdre": {
        "carte": "Rata Sum",
        "tp": "Point de passage de la Cour métrique",
        "chatCode": "[&BBMEAAA=]",
        "aide": "L'emplacement de cercle d'or est actuellement inconnu.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-magihedron-corner-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-magihedron-corner-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-magihedron-corner-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-magihedron-corner-guild-trek-3.jpg"]
    },
    "Col des frères": {
        "carte": "Hoelbrak",
        "tp": "Point de passage de la Panthère des neiges",
        "chatCode": "[&BIcDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-brothers-notch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-brothers-notch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-brothers-notch-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-brothers-notch-guild-trek-4.jpg"]
    },
    "Col du Coeur criant": {
        "carte": "Montée de Flambecoeur",
        "tp": "Point de passage de l'Apostat",
        "chatCode": "[&BB0CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-heart-speaks-notch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heart-speaks-notch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heart-speaks-notch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-heart-speaks-notch-guild-trek-3.jpg"]
    },
    "Console de commande principale LIN39": {
        "carte": "Province de Metrica",
        "tp": "Point de passage du Campement des rescapés",
        "chatCode": "[&BEcAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-master-control-lin39-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-master-control-lin39-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-master-control-lin39-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-master-control-lin39-guild-trek-4.jpg"]
    },
    "Contrepoids d'Osenfold": {
        "carte": "Contrefort du Voyageur",
        "tp": "Point de passage d'Osenfold",
        "chatCode": "[&BAEEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-osenfold-counterweights-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-osenfold-counterweights-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-osenfold-counterweights-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-osenfold-counterweights-guild-trek-2.jpg"]
    },
    "Côte de Couvedrake": {
        "carte": "Plateau de Diessa",
        "tp": "Point de passage Brèchezeaux",
        "chatCode": "[&BGQBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-drakehatch-shore-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakehatch-shore-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakehatch-shore-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakehatch-shore-guild-trek-3.jpg"]
    },
    "Côte de Togatl": {
        "carte": "Collines de Kesse",
        "tp": "Point de passage de Viathan",
        "chatCode": "[&BBAAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-tagotl-shore-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tagotl-shore-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tagotl-shore-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tagotl-shore-guild-trek-3.jpg"]
    },
    "Cour de Chutes brisées": {
        "carte": "Citadelle Noire",
        "tp": "Point de passage des Ruines de Rin",
        "chatCode": "[&BKwDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-broken-falls-courtyard-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broken-falls-courtyard-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broken-falls-courtyard-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-broken-falls-courtyard-guild-trek-3.jpg"]
    },
    "Cour des Chutes de la Biche": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage de la Cité d'Ascalon",
        "chatCode": "[&BIcBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-doefalls-court-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-doefalls-court-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-doefalls-court-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-doefalls-court-guild-trek-3.jpg"]
    },
    "Crevasse du Gibier": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage de la Maison de Vangir",
        "chatCode": "[&BOUAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-venison-hollow-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-venison-hollow-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-venison-hollow-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-venison-hollow-guild-trek-2.jpg"]
    },
    "Crique d'Isenfell": {
        "carte": "Congères d'Antreneige",
        "tp": "",
        "chatCode": "[&BLgAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-isenfell-wash-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isenfell-wash-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isenfell-wash-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isenfell-wash-guild-trek-3.jpg"]
    },
    "Crique de Trouvécaille": {
        "carte": "Montée de Flambecoeur",
        "tp": "Point de passage du Poste de commandement de Tuyère",
        "chatCode": "[&BBgCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-skalefound-cove-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalefound-cove-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalefound-cove-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skalefound-cove-guild-trek-2.jpg"]
    },
    "Débarras d'Ulta": {
        "carte": "Terres Sauvages de Brisban",
        "tp": "Point de passage de la Métamagique d'Ulta",
        "chatCode": "[&BGUAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ulta-scraproom-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ulta-scraproom-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ulta-scraproom-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ulta-scraproom-guild-trek-2.jpg"]
    },
    "Dents de la corruption": {
        "carte": "Détroit des Gorges Glacées",
        "tp": "Point de passage de Drakkar",
        "chatCode": "[&BIYCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-corruptions-teeth-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-corruptions-teeth-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-corruptions-teeth-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-corruptions-teeth-guild-trek-3.jpg"]
    },
    "Désir de Pochtecatl": {
        "carte": "Côte de la marée sanglante",
        "tp": "",
        "chatCode": "[&BK8BAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-pochtecatls-desire-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-pochtecatls-desire-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-pochtecatls-desire-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-pochtecatls-desire-guild-trek-3.jpg"]
    },
    "Déversoir de Thaumanova": {
        "carte": "Province de Metrica",
        "tp": "Point de passage muridienne",
        "chatCode": "[&BEcAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-thaumanova-spillway-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-thaumanova-spillway-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-thaumanova-spillway-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-thaumanova-spillway-guild-trek-3.jpg"]
    },
    "Distillerie de la Chouette cachée": {
        "carte": "Congères d'Antreneige",
        "tp": "Point de passage de la Chouette",
        "chatCode": "[&BMEAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-hidden-owl-distillery-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-hidden-owl-distillery-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-hidden-owl-distillery-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-hidden-owl-distillery-guild-trek-4.jpg"]
    },
    "Dortoir du Hall de Skibo": {
        "carte": "Rata Sum",
        "tp": "Point de passage auxiliaire",
        "chatCode": "[&BLkEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-skibo-hall-dormitory-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skibo-hall-dormitory-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skibo-hall-dormitory-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skibo-hall-dormitory-guild-trek-3.jpg"]
    },
    "Échafaudage autoporteur": {
        "carte": "Citadelle Noire",
        "tp": "Point de passage des Ruines de Rin",
        "chatCode": "[&BKwDAAA=]",
        "aide": "Notez que le cercle d'or est placé au-dessus d'une sorte d'échafaudage sur lequel vous pouvez grimper.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-freestand-scaffold-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-freestand-scaffold-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-freestand-scaffold-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-freestand-scaffold-guild-trek-2.jpg"]
    },
    "Emplacement hanté": {
        "carte": "Saut de Malchor",
        "tp": "Point de passage des lumières",
        "chatCode": "[&BLICAAA=]",
        "aide": "Notez que aller à cet emplacement peut être un peu compliqué, regarder la vidéo ci-après pour plus d'infos. Essentiellement, vous devez aller au point de compétence au Nord-Ouest par le temple de Dwayna et faire un certain nombre de sauts de difficultés moyenne. <a href=\"http://youtu.be/3Z7Bda1LYWE\">voir la vidéo</a></span>",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-spectrehaunt-socket-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-spectrehaunt-socket-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-spectrehaunt-socket-guild-trek-6.jpg", "http://androuw.e-monsite.com/medias/images/gw2-spectrehaunt-socket-guild-trek-5.jpg"]
    },
    "Emprise agitée": {
        "carte": "Mont Maelström",
        "tp": "Point de passage de l'Ile du Méandre",
        "chatCode": "[&BNECAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-restless-footings-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-restless-footings-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-restless-footings-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-restless-footings-guild-trek-4.jpg"]
    },
    "Ermitage abandonné": {
        "carte": "Les Steppes de la Strie Flamboyante",
        "tp": "Point de passage de la Pierre gardienne",
        "chatCode": "[&BP8BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-vacant-hermitage-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-vacant-hermitage-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-vacant-hermitage-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-vacant-hermitage-guild-trek-2.jpg"]
    },
    "Escarpement du pêcheur": {
        "carte": "Province de Metrica",
        "tp": "Point de passage de la Vieille fonderie de golems",
        "chatCode": "[&BK4EAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-fishers-crag-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fishers-crag-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fishers-crag-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fishers-crag-guild-trek-4.jpg"]
    },
    "Etreinte de l'hymne": {
        "carte": "Rivage maudit",
        "tp": "",
        "chatCode": "[&BOQGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-anthems-hold-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-anthems-hold-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-anthems-hold-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-anthems-hold-guild-trek-4.jpg"]
    },
    "Excavation profanée": {
        "carte": "Collines de Kesse",
        "tp": "Point de passage de Sombreplaie",
        "chatCode": "[&BBEAAAA=]",
        "aide": "Le cercle d'or est dans la grotte.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-defiled-delve-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-defiled-delve-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-defiled-delve-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-defiled-delve-guild-trek-3.jpg"]
    },
    "Faille de Pouacregriffe": {
        "carte": "Marais de Fer",
        "tp": "Point de passage du Lac Pourprenage",
        "chatCode": "[&BOMBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-dirtclaw-cleft-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dirtclaw-cleft-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dirtclaw-cleft-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dirtclaw-cleft-guild-trek-4.jpg"]
    },
    "Fière tanière du jaguar": {
        "carte": "Province de Metrica",
        "tp": "Point de passage muridienne",
        "chatCode": "[&BEcAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-jaguar-pride-den-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-jaguar-pride-den-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-jaguar-pride-den-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-jaguar-pride-den-guild-trek-3.jpg"]
    },
    "Folie de Widd": {
        "carte": "Forêt de Caledon",
        "tp": "",
        "chatCode": "[&BDoBAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-widds-folly-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-widds-folly-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-widds-folly-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-widds-folly-guild-trek-3.jpg"]
    },
    "Fontaine de Verdance": {
        "carte": "Rivage Maudit",
        "tp": "Point de passage de Verdance",
        "chatCode": "[&BBsDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-verdance-font-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-verdance-font-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-verdance-font-guild-trek-3.jpg"]
    },
    "Fontaine des racines cachées": {
        "carte": "Le Bosquet",
        "tp": "Point de passage de la Terrasse commune supérieure",
        "chatCode": "[&BLoEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-backroot-foundtain-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-backroot-fountain-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-backroot-fountain-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-backroot-fountain-guild-trek.jpg"]
    },
    "Forage du nid de skelk": {
        "carte": "Détroit des Gorges Glacées",
        "tp": "Point de passage du Bourbier de la Mélancolie",
        "chatCode": "[&BHwCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-skelknest-borehole-guild-trek1.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skelknest-borehole-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-skelknest-borehole-guild-trek-2.jpg"]
    },
    "Fosse de Piègetroll": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage du Prieuré de Durmand",
        "chatCode": "[&BOkAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-trolltrap-pit-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-trolltrap-pit-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-trolltrap-pit-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-trolltrap-pit-guild-trek-2.jpg"]
    },
    "Fosse de la guivre des glaces": {
        "carte": "Détroit des Gorges Glacées",
        "tp": "Point de passage de Dimotiki",
        "chatCode": "[&BH8CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-icewurm-trench-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-icewurm-trench-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-icewurm-trench-guild-trek.jpg"]
    },
    "Fouilles de Stigmafrappe": {
        "carte": "Champs de Ruines",
        "tp": "Point de passage de la Mine d'Hellion",
        "chatCode": "[&BEsBAAA=]",
        "aide": "Le cercle d'or est dans une pièce cachée au rez-de-chaussée du puzzle jump de la Mine stigmatisé.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-brandstrike-dig-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-brandstrike-dig-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-brandstrike-dig-guild-trek-3.jpg"]
    },
    "Fouilleur de fumier": {
        "carte": "Falaises de HanteDraguerre",
        "tp": "Point de passage de Steelbrachen",
        "chatCode": "[&BFsCAAA=]",
        "aide": "Notez que l'entrée de la Mine de Dissun est localisée par la flèche rouge.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-foragers-midden-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-foragers-midden-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-foragers-midden-guild-trek-3.jpg"]
    },
    "Foyer de Kari": {
        "carte": "Collines de Kesse",
        "tp": "Point de passage de Cereboth",
        "chatCode": "[&BBIAAAA=]",
        "aide": "Il y a un trou dans le sol dans lequel on peut sauter pour accéder au Point chaud de Kari.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-karis-hot-spot-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-karis-hot-spot-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-karis-hot-spot-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-karis-hot-spot-guild-trek-3.jpg"]
    },
    "Frayère des drakes des récifs": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNUGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-reef-drake-den-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-reef-drake-den-guild-trek.jpg"]
    },
    "Fuite de Toxal": {
        "carte": "Terres Sauvages de Brisban",
        "tp": "Point de passage de Mirkrise",
        "chatCode": "[&BHYAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-8.jpg", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-6.jpg", "http://androuw.e-monsite.com/medias/images/gw2-toxal-spill-guild-trek-7.jpg"]
    },
    "Galerie du limon de sang": {
        "carte": "Côte de la Marée Sanglante",
        "tp": "Point de passage lugubre",
        "chatCode": "[&BK0BAAA=]",
        "aide": "L'obtention du cercle d'or est un peu délicate vu que c'est juste à côté du Limon Champion qui est assez dur à tuer. Une fois que vous êtes à l'intérieur de la caverne, vous devez monter et passer à travers un groupe de morts-vivants avant que vous ne puissiez arriver aux limons.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-blood-ooze-gallery1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blood-ooze-gallery-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blood-ooze-gallery-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blood-ooze-gallery-guild-trek-3.jpg"]
    },
    "Geôle de Provatum": {
        "carte": "Montée de Flambecoeur",
        "tp": "Point de passage du Gardien",
        "chatCode": "[&BCYCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-provatum-carcer-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-provatum-carcer-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-provatum-carcer-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-provatum-carcer-guild-trek-2.jpg"]
    },
    "Gouffre de Whitland": {
        "carte": "Mont Maelström",
        "tp": "Point de passage du Site du Vieux traîneau",
        "chatCode": "[&BNQCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-whitland-sinkhole-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-whitland-sinkhole-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-whitland-sinkhole-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-whitland-sinkhole-guild-trek-4.jpg"]
    },
    "Grenier effondré": {
        "carte": "Marais de Lumillule",
        "tp": "Point de passage de Fort Cadence",
        "chatCode": "[&BMUBAAA=]",
        "aide": "Le cercle d'or est placé au deuxième étage depuis le sommet dans le coin Sud-Est du bâtiment.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-shattered-loft-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-shattered-loft-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-shattered-loft-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-shattered-loft-guild-trek-3.jpg"]
    },
    "Griffure de l'éclat céleste": {
        "carte": "Hinterlands haratis",
        "tp": "Point de passage de Grey Gritta",
        "chatCode": "[&BKkAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-skyshrine-scratch-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skyshrine-scratch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skyshrine-scratch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-skyshrine-scratch-guild-trek-3.jpg"]
    },
    "Griffure invisible": {
        "carte": "Fôret de Caledon",
        "tp": "Point de passage de Mabon",
        "chatCode": "[&BDoBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-unseen-scratch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-unseen-scratch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-unseen-scratch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-unseen-scratch-guild-trek-3.jpg"]
    },
    "Grotte Oubliée": {
        "carte": "Les Steppes de la Strie Flamboyante",
        "tp": "Point de passage de Terra Carorunda",
        "chatCode": "[&BAECAAA=]",
        "aide": "Le cercle d'or se situe au milieu du jumping :",
        "images": ["http://www.youtube.com/watch?v=86KpGTIS9_Q&feature=share&list=PLZX6gnjnhlb15POrbjew3xWwGJGgz9Yqc"]
    },
    "Grotte d'Eaudefonte": {
        "carte": "Chute de la Canopée",
        "tp": "Point de passage de Fil d'Écaille",
        "chatCode": "[&BEgCAAA=]",
        "aide": "Le cercle d'or est sous l'eau à l'intérieur d'une grotte.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-meltwater-cave-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-meltwater-cave-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-meltwater-cave-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-meltwater-cave-guild-trek-3.jpg"]
    },
    "Grotte de Gorgetoile": {
        "carte": "Les Steppes de la Strie Flamboyante",
        "tp": "Point de passage du Glaive",
        "chatCode": "[&BAQCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-canyonweb-cave-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-canyonweb-cave-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-canyonweb-cave-guild-trek-3.jpg"]
    },
    "Grotte de Lawen": {
        "carte": "Champs de Gendarran",
        "tp": "Point de passage du Premier Refuge",
        "chatCode": "[&BIsBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lawen-grotto-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lawen-grotto-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lawen-grotto-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lawen-grotto-guild-trek-3.jpg"]
    },
    "Gué kraalétroi": {
        "carte": "Champs de Ruines",
        "tp": "",
        "chatCode": "[&BE8BAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-narrowkraal-crossing-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-narrowkraal-crossing-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-narrowkraal-crossing-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-narrowkraal-crossing-guild-trek-3.jpg"]
    },
    "Guet de la bagarre de barils": {
        "carte": "Hoelbrak",
        "tp": "Point de passage de la Boussole du Héros",
        "chatCode": "[&BJADAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-kegbrawl-watch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-kegbrawl-watch-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-kegbrawl-watch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-kegbrawl-watch-guild-trek-3.jpg"]
    },
    "Guet réverbérant": {
        "carte": "Contrefort du Voyageur",
        "tp": "Point de passage d'Écorchenuit",
        "chatCode": "[&BHUBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-reverberants-watch-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-reverberants-watch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-reverberants-watch-guild-trek-3.jpg"]
    },
    "Guivre des sables maraudeuse": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNUGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-sandwurm-prowl-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sandwurm-prowl-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sandwurm-prowl-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sandwurm-prowl-guild-trek-3.jpg"]
    },
    "Hall de Guilde du Destin": {
        "carte": "Vallée de la Reine",
        "tp": "Point de passage de Shaemoor",
        "chatCode": "[&BO8AAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-destinys-guildhall-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-destinys-guildhall-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-destinys-guildhall-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-destinys-guildhall-guild-trek-3.jpg"]
    },
    "Halte de Coupegorge": {
        "carte": "Champs de Gendarran",
        "tp": "Point de passage de Brigantine",
        "chatCode": "[&BM0DAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cutthroats-rest-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cutthroats-rest-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cutthroats-rest-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cutthroats-rest-guild-trek-3.jpg"]
    },
    "Halte de Soren Draa": {
        "carte": "Province de Metrica",
        "tp": "Point de passage de Soren Draa",
        "chatCode": "[&BEAAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-soren-draa-rest-shop-guild-trek-21.jpg", "http://androuw.e-monsite.com/medias/images/gw2-soren-draa-rest-shop-guild-trek-41.jpg", "http://androuw.e-monsite.com/medias/images/gw2-soren-draa-rest-shop-guild-trek-31.jpg"]
    },
    "Impasse du Gladiver": {
        "carte": "Rivage Maudit",
        "tp": "Point de passage R&amp;D",
        "chatCode": "[&BBgDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-winterknell-impasse-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-winterknell-impasse-guild-trek-3.jpg"]
    },
    "Jardin de Fortepatte": {
        "carte": "Plateau de Diessa",
        "tp": "Point de passage de Nageling",
        "chatCode": "[&BN0AAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-strongpaws-garden-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-strongpaws-garden-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-strongpaws-garden-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-strongpaws-garden-guild-trek-3.jpg"]
    },
    "Laboratoire de la taverne de Turai": {
        "carte": "Promontoire Divin",
        "tp": "Point de passage de Balthazar",
        "chatCode": "[&BCgDAAA=]",
        "aide": "Il est localisé dans le sous-sol de la taverne.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-turai-tavern-stillroom-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-turai-tavern-stillroom-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-turai-tavern-stillroom-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-turai-tavern-stillroom-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-turai-tavern-stillroom.jpg"]
    },
    "La sellette de Kaldar": {
        "carte": "Hoelbrak",
        "tp": "",
        "chatCode": "[&BI0DAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-kaldars-hot-seat-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kaldars-hot-seat-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kaldars-hot-seat-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-kaldars-hot-seat-guild-trek-4.jpg"]
    },
    "Le devoir de Morndottir": {
        "carte": "Hoelbrak",
        "tp": "Point de passage du Rocher de l'abri",
        "chatCode": "[&BIsDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-grimdottirs-duty-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grimdottirs-duty-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grimdottirs-duty-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grimdottirs-duty-guild-trek-3.jpg"]
    },
    "Le magasin des ouvriers": {
        "carte": "Falaises de HanteDraguerre",
        "tp": "Point de passage de la Route grise",
        "chatCode": "[&BFoCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-the-workers-stores-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-workers-stores-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-workers-stores-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-workers-stores-guild-trek-4.jpg"]
    },
    "Les Marches du Talus": {
        "carte": "Chute de la Canopée",
        "tp": "Point de passage de Talus",
        "chatCode": "[&BEQCAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-talus-steps-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-talus-steps-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-talus-steps-guild-trek-3.jpg"]
    },
    "Klub des Karkas": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNUGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-the-karka-club-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-the-karka-club-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-the-karka-club-guild-trek-3.jpg"]
    },
    "L'impasse du peuple": {
        "carte": "Détroit des Gorges Glacées",
        "tp": "Point de passage de Groznev",
        "chatCode": "[&BHkCAAA=]",
        "aide": "Pour aller à l'emplacement pour activer le marqueur, vous devez monter sur la rampe supérieure.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-the-peoples-deadlock.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-peoples-deadlock-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-peoples-deadlock-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-peoples-deadlock-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-the-peoples-deadlock-5.jpg"]
    },
    "Marche vaporeuses": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNIGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-steamy-steps-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-steamy-steps-guild-trek-2.jpg"]
    },
    "Mirador de Beetletun": {
        "carte": "La Vallée de la reine",
        "tp": "",
        "chatCode": "[&BPoAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-beetlestone-mirador-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-beetlestone-mirador-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-beetlestone-mirador-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-beetlestone-mirador-guild-trek-3.jpg"]
    },
    "Monument à l'ancien": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNgGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-monument-to-the-ancient-one-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-monument-to-the-ancient-one-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-monument-to-the-ancient-one-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-monument-to-the-ancient-one-guild-trek-3.jpg"]
    },
    "Motte de Lamenoire": {
        "carte": "Plateau de Diessa",
        "tp": "Point de passage de Lamenoire",
        "chatCode": "[&BEIEAAA=]",
        "aide": "Atteindre le Cercle d'Or est un peu délicat pour celui ci, vous aurez besoin de marcher le long d'un rebord étroit pour aller au sommet de cette coline.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-blackblade-butte-guild-trek2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blackblade-butte-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blackblade-butte-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blackblade-butte-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blackblade-butte-guild-trek-32.jpg"]
    },
    "Mouillage de Covington": {
        "carte": "Côte de la Marée Sanglante",
        "tp": "Point de passage de la Mouette rieuse",
        "chatCode": "[&BKgBAAA=]",
        "aide": "Le cercle d'or est situé tout au fond du bateau de pirate.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-covingtons-stowage-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-covingtons-stowage-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-covingtons-stowage-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-covingtons-stowage-guild-trek-4.jpg"]
    },
    "Mouillage du Capitaine": {
        "carte": "Saut de Malchor",
        "tp": "Point de passage des lumières",
        "chatCode": "[&BLICAAA=]",
        "aide": "On ne connaît pas encore l'emplacement exacte du cercle d'or. Il pourrait être quelque part sur le bateau submergé.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-captains-berth-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-captains-berth-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-captains-berth-guild-trek-3.jpg"]
    },
    "Mur d'enceinte de Claypool": {
        "carte": "Vallée de la Reine",
        "tp": "Point de passage de Claypool",
        "chatCode": "[&BPYAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-claypool-bailey-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-claypool-bailey-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-claypool-bailey-guild-trek.jpg"]
    },
    "Nid d'Araignée cavernicole": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage de l'Enclave du Pinacle",
        "chatCode": "[&BJgBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cave-spider-nidus-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-spider-nidus-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-spider-nidus-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cave-spider-nidus-guild-trek-3.jpg"]
    },
    "Nid du raptor": {
        "carte": "Marais de Fer",
        "tp": "Point de passage de la Ville de l'Etoile de Caninecol",
        "chatCode": "[&BOsBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-raptors-aerie1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-raptors-aerie-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-raptors-aerie-guild-trek-2.jpg"]
    },
    "Objets trouvés de l'Autorité du Port": {
        "carte": "Rata Sum",
        "tp": "Point de passage du port",
        "chatCode": "[&BAcFAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-port-authority-lost-and-found-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-port-authority-lost-and-found-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-port-authority-lost-and-found-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-port-authority-lost-and-found-guild-trek-3.jpg"]
    },
    "Oeil du Scorpion des mers": {
        "carte": "Rivages Maudits",
        "tp": "Point de passage de la Crête indiscrète",
        "chatCode": "[&BB4DAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-sea-scorpions-eye-guild-trek2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sea-scorpions-eye-guild-trek-31.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sea-scorpions-eye-guild-trek-5.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sea-scorpions-eye-guild-trek-41.jpg"]
    },
    "Œuvre d'Heidi": {
        "carte": "Hinterlands harathis",
        "tp": "",
        "chatCode": "[&BKcAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-heidis-showpiece-guild-trek1.jpg", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-heidis-showpiece-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-heidis-showpiece-guild-trek-3.jpg"]
    },
    "Paddock du moa vert": {
        "carte": "Fôret de Caledon",
        "tp": "Point de passage du Refuge de Caledon",
        "chatCode": "[&BDwBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-green-moa-paddock-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-green-moa-paddock-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-green-moa-paddock-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-green-moa-paddock-guild-trek-3.jpg"]
    },
    "Palan charmine": {
        "carte": "Montée de Flambecoeur",
        "tp": "",
        "chatCode": "[&BBcCAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-orecart-hoist-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-orecart-hoist-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-orecart-hoist-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-orecart-hoist-guild-trek-3.jpg"]
    },
    "Panorama de Phasmatis": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage du Chantier de Dockfer",
        "chatCode": "[&BIoBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-phasmatis-prospect-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-phasmatis-prospect-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-phasmatis-prospect-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-phasmatis-prospect-guild-trek-4.jpg"]
    },
    "Parapet des constellations": {
        "carte": "Le Bosquet",
        "tp": "Point de passage de la Terrasse commune supérieure",
        "chatCode": "[&BLoEAAA=]",
        "aide": "<span>Notez que le cercle d'or est en réalité à l'extérieur du bâtiment, on accède via une des plates-formes qui s'ouvre à l'extérieur. Du bas du bâtiment, prenez à droite sur la rampe pour avoir accès à une rampe alternative. De cette deuxième rampe, prenez à gauche.</span>",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-constellation-parapet1.jpg", "http://www.lebusmagique.fr/medias/images/gw2-constellation-parapet-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-constellation-parapet-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-constellation-parapet-guild-trek-2.jpg"]
    },
    "Pas de Tir de Mina": {
        "carte": "Promontoire Divin",
        "tp": "Point de passage du quartier populaire",
        "chatCode": "[&BCoDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-minas-target-shoot-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-minas-target-shoot-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-minas-target-shoot-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-minas-target-shoot-guild-trek-4.jpg"]
    },
    "Pavillon de Grenth": {
        "carte": "Promontoire Divin",
        "tp": "Point de passage de Grenth",
        "chatCode": "[&BCQDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-grenths-pavillion-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grenths-pavillion-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grenths-pavillion-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-grenths-pavillion-guild-trek-3.jpg"]
    },
    "Pavillon du Seigneur": {
        "carte": "Collines de Kesse",
        "tp": "Point de passage du seigneur",
        "chatCode": "[&BAQAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-overlord-lodge-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-overlord-lodge-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-overlord-lodge-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-overlord-lodge-guild-trek-3.jpg"]
    },
    "Perchoir Tubavapeur": {
        "carte": "Crique de Sud-Soleil",
        "tp": "",
        "chatCode": "[&BNUGAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-steampipe-perch-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-steampipe-perch-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-steampipe-perch-guild-trek-2.jpg"]
    },
    "Perchoir de Raptor": {
        "carte": "Champs de Gendarran",
        "tp": "Point de passage d'Aveugleneige.",
        "chatCode": "[&BMwDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-raptors-perch1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-raptors-perch-4.jpg", "https://i.imgur.com/ERrtcNM.jpg", "https://i.imgur.com/SK57vkG.jpg"]
    },
    "Perchoir de l'Ermite": {
        "carte": "Champs de Ruines",
        "tp": "Point de passage du Campement de Rosko",
        "chatCode": "[&BNgAAAA=]",
        "aide": "La zone exacte de l'emplacement de la randonnée de guilde demeure inconnue à ce jour.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-hermits-roost-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-hermits-roost-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-hermits-roost-guild-trek-3.jpg"]
    },
    "Perchoir d'œil-de-faucon": {
        "carte": "Chutes de la Canopée",
        "tp": "",
        "chatCode": "[&BEUCAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-hawkeye-perch-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-hawkeye-perch-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-hawkeye-perch-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-hawkeye-perch-guild-trek-3.jpg"]
    },
    "Pergola d'Aubeluit": {
        "carte": "Le Bosquet",
        "tp": "Point de passage de Ronan",
        "chatCode": "[&BLwEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-dawngleam-pergola-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dawngleam-pergola-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dawngleam-pergola-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-dawngleam-pergola-guild-trek-3.jpg"]
    },
    "Pic du Béliervédère": {
        "carte": "Falaises de HanteDraguerre",
        "tp": "Point de passage de Travelen",
        "chatCode": "[&BGQCAAA=]",
        "aide": "Notez que pour arriver au sommet où est le bélier de Champion, vous devrez monter sur les rochers près de l'emplacement indiqué par les flêches.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ramview-peak-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ramview-peak-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ramview-peak-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ramview-peak-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ramview-peak-guild-trek-41.jpg"]
    },
    "Place engloutie": {
        "carte": "Détroit de la Dévastation",
        "tp": "Point de passage du Forum Royal",
        "chatCode": "[&BPMCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-drowned-plaza-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drowned-plaza-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drowned-plaza-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drowned-plaza-guild-trek-3.jpg"]
    },
    "Plage nécrolithe": {
        "carte": "Le Bosquet",
        "tp": "",
        "chatCode": "[&BBIEAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-necrolith-landing-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-necrolith-landing-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-necrolith-landing-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-necrolith-landing-guild-trek-3.jpg"]
    },
    "Planche à dessin de Tekki": {
        "carte": "Terres sauvages de Brisban",
        "tp": "",
        "chatCode": "[&BGUAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-tekkis-drawing-board-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tekkis-drawing-board-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tekkis-drawing-board-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tekkis-drawing-board-guild-trek-4.jpg"]
    },
    "Plateau de Krallcamden": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage de la Tour de l'Escarpement",
        "chatCode": "[&BIgBAAA=]",
        "aide": "Le cercle d'or est localisé au sommet, on peut y accéder via un petit passage, suivez la ligne inférieur de points blanc sur le screen ci dessous.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cademkrall-overlook-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cademkrall-overlook-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cademkrall-overlook-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cademkrall-overlook-guild-trek-3.jpg"]
    },
    "Plongeur facebourbié": {
        "carte": "Mont Maelström",
        "tp": "",
        "chatCode": "[&BNECAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-deepmire-diver-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-deepmire-diver-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-deepmire-diver-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-deepmire-diver-guild-trek-3.jpg"]
    },
    "Poche de diablotin de feu": {
        "carte": "Mont Maelström",
        "tp": "Point de passage de Maelstrom",
        "chatCode": "[&BM0CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-flame-imp-pocket-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flame-imp-pocket-guild-trek-21.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flame-imp-pocket-guild-trek-41.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flame-imp-pocket-guild-trek-31.jpg"]
    },
    "Point de vue de Dockfer": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage du Chantier de Dockfer",
        "chatCode": "[&BIoBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-irondock-viewpoint-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-irondock-viewpoint-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-irondock-viewpoint-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-irondock-viewpoint-guild-trek-3.jpg"]
    },
    "Point de vue de Gnashar": {
        "carte": "Terres Sauvages de Brisban",
        "tp": "Point de passage de Wendon",
        "chatCode": "[&BF0AAAA=]",
        "aide": "Notez que le cercle d'or est placé en haut de la colline accessible via une série de marches en pierres.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-gnashars-viewpoint-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-gnashars-viewpoint-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-gnashars-viewpoint-guild-trek-3.jpg"]
    },
    "Point de vue de Rurik": {
        "carte": "Promontoire Divin",
        "tp": "Point de passage de Rurikton",
        "chatCode": "[&BCsDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ruriks-view-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ruriks-view-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ruriks-view-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ruriks-view-guild-trek-4.jpg"]
    },
    "Point de vue d'isgarren": {
        "carte": "Collines de Kesse",
        "tp": "",
        "chatCode": "[&BBEAAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-isgarren-viewpoint-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isgarren-viewpoint-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isgarren-viewpoint-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-isgarren-viewpoint-guild-trek-3.jpg"]
    },
    "Pont de Guet-du-feu": {
        "carte": "Marais de Fer",
        "tp": "Point de passage du Campement de Guet-du-feu",
        "chatCode": "[&BO0BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-firewatch-flybridge-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-firewatch-flybridge-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-firewatch-flybridge-guild-trek-3.jpg"]
    },
    "Porche de Fawcett": {
        "carte": "Harathi Hinterlands",
        "tp": "Point de passage d'Arca",
        "chatCode": "[&BLIAAAA=]",
        "aide": "Notez que le cercle d'or ne peut être atteint qu'en faisant le Jumping Puzzle <a href=\"https://www.youtube.com/watch?v=FFNbnMoEMiY\">Vengeance de Fawcett</a> entièrement (cliquez sur le nom pour la vidéo faites par la SaDo expédition).",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-fawcetts-porch-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fawcetts-porch-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fawcetts-porch-guild-trek-31.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fawcetts-porch-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-fawcetts-porch-guild-trek-41.jpg"]
    },
    "Porte de Droknah": {
        "carte": "Mont Maelström",
        "tp": "Point de passage du Site du Vieux traîneau",
        "chatCode": "[&BNQCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-droknahs-gate-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-droknahs-gate-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-droknahs-gate-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-droknahs-gate-guild-trek-2.jpg"]
    },
    "Porte de Wikk": {
        "carte": "Chute de la Canopée",
        "tp": "Point de passage du Tutorat de Valance",
        "chatCode": "[&BEwCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-wikks-gate-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-wikks-gate-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-wikks-gate-guild-trek-6.jpg"]
    },
    "Port extérieur du Vizir": {
        "carte": "Détroit de la Dévastation",
        "tp": "Point de passage du Poste isolé",
        "chatCode": "[&BPcCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-viziers-anteport.jpg", "http://androuw.e-monsite.com/medias/images/gw2-viziers-anteport-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-viziers-anteport-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-viziers-anteport-guild-trek-3.jpg"]
    },
    "Portique de Rata Pten": {
        "carte": "Mont Maelström",
        "tp": "Point de passage Criterion",
        "chatCode": "[&BMkCAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-rata-pten-portico-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-rata-pten-portico-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-rata-pten-portico-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-rata-pten-portico-guild-trek.jpg"]
    },
    "Poste de vigie de Décimus": {
        "carte": "Plaines d'Ashford",
        "tp": "Point de passage du Point de garde de Décimus",
        "chatCode": "[&BJgDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-watchpoint-decimus-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-watchpoint-decimus-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-watchpoint-decimus-guild-trek-7.jpg", "http://androuw.e-monsite.com/medias/images/gw2-watchpoint-decimus-guild-trek-6.jpg"]
    },
    "Préfecture de Lychcroft": {
        "carte": "Collines de Kesse",
        "tp": "Point de passage du Site d'Ombrecœur",
        "chatCode": "[&BAwAAAA=]",
        "aide": "Le cercle d'or est au sommet de la rampe, directement à côté du PNJ de coeur.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lychcroft-wardenship-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lychcroft-wardenship-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lychcroft-wardenship-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lychcroft-wardenship-guild-trek-3.jpg"]
    },
    "Prison de Taupvaquie": {
        "carte": "Contrefort du Voyageur",
        "tp": "Point de passage d'Halvaunt",
        "chatCode": "[&BHgBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-moleberia-prison-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-moleberia-prison-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-moleberia-prison-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-moleberia-prison-guild-trek-3.jpg"]
    },
    "Promontoire de Portmatt": {
        "carte": "Côte de la Marée Sanglante",
        "tp": "Point de passage des Lamentations",
        "chatCode": "[&BKQBAAA=]",
        "aide": "Le cercle d'or tout en haut du puzzle jump du Laboratoire du Professeur Portmatt près du coffre. Vous devez entrer dans l'ordre correct 14.xx.xx-49.xx-0.02xx dans le terminal pour arriver à la fin du puzzle. <a href=\"http://www.youtube.com/watch?v=gSnC10GJBI0\">Vidéo du Laboratoire du Professeur Portmatt</a></span>",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-portmatts-promontory-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-portmatts-promontory-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-portmatts-promontory-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-portmatts-promontory-guild-trek-2.jpg"]
    },
    "Quai de Lestepied": {
        "carte": "Détroit de la Dévastation",
        "tp": "Point de passage de Tonnecaboche",
        "chatCode": "[&BPACAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lightfoot-dock-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lightfoot-dock-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lightfoot-dock-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lightfoot-dock-guild-trek-5.jpg"]
    },
    "Recoin du Scriptorium": {
        "carte": "Citadelle Noire",
        "tp": "Point de passage du Factorium",
        "chatCode": "[&BKcDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-scriptorium-nook-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scriptorium-nook-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scriptorium-nook-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scriptorium-nook-guild-trek-2.jpg"]
    },
    "Recoin du corbeau": {
        "carte": "Hoelbrak",
        "tp": "Point de passage de Corbeau",
        "chatCode": "[&BIgDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ravens-nook-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ravens-nook-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ravens-nook-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ravens-nook-guild-trek-4.jpg"]
    },
    "Recoin lapidaire de Flakk": {
        "carte": "Rata Sum",
        "tp": "Point de passage de la Comptabilité",
        "chatCode": "[&BLYEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-flakks-lapidary-nook-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flakks-lapidary-nook-guild-trek-21.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flakks-lapidary-nook-guild-trek-41.jpg", "http://androuw.e-monsite.com/medias/images/gw2-flakks-lapidary-nook-guild-trek-31.jpg"]
    },
    "Refuge d'Antreneige": {
        "carte": "Congères d'Antreneige",
        "tp": "Point de passage du Refuge de la Congère",
        "chatCode": "[&BLkAAAA=]",
        "aide": "Il y a une entrée à cette petite pièce chambre si vous sautez en bas des murs",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-snowden-safehouse-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowden-safehouse-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowden-safehouse-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-snowden-safehouse-guild-trek-3.jpg"]
    },
    "Refuge de siamouth": {
        "carte": "Marais de Lumillule",
        "tp": "Point de passage d'Ondesaline",
        "chatCode": "[&BM4BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-siamoth-refuge-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-siamoth-refuge-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-siamoth-refuge-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-siamoth-refuge-guild-trek-3.jpg"]
    },
    "Refuge du Stentor": {
        "carte": "Détroit de la Dévastation",
        "tp": "Point de passage du Pic de Signal",
        "chatCode": "[&BO0CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-stentor-shelter-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-stentor-shelter-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-stentor-shelter-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-stentor-shelter-guild-trek-3.jpg"]
    },
    "Refuge percebul": {
        "carte": "Les Steppes de la Strie flamboyante",
        "tp": "",
        "chatCode": "[&BFIDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-burstbubble-blind-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-burstbubble-blind-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-burstbubble-blind-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-burstbubble-blind-guild-trek-3.jpg"]
    },
    "Repaire de Soufflettin": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage de la Gueule du démon",
        "chatCode": "[&BOYAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ettinbreath-lair-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ettinbreath-lair-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ettinbreath-lair-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ettinbreath-lair-guild-trek-3.jpg"]
    },
    "Repaire de l'Arctodus": {
        "carte": "Contrefort du Voyageur",
        "tp": "Point de passage de la Colonie de Vendrake",
        "chatCode": "[&BH4BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-arctodus-haunt-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-arctodus-haunt-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-arctodus-haunt-guild-trek-3.jpg"]
    },
    "Repère de l'Autel du Ruisseau": {
        "carte": "Vallée de la Reine",
        "tp": "Point de passage du Carrefour",
        "chatCode": "[&BPIAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-altar-brook-lair-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-altar-brook-lair-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-altar-brook-lair-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-altar-brook-lair-guild-trek-4.jpg"]
    },
    "Repli stratégique": {
        "carte": "Rivage Maudit",
        "tp": "Point de passage du Rocher de l'épave",
        "chatCode": "[&BOQGAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-tactical-retreat-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tactical-retreat-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tactical-retreat-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-tactical-retreat-guild-trek-3.jpg"]
    },
    "Retraite Gelée": {
        "carte": "Chute de la Canopée",
        "tp": "Point de passage de Feuilleblanche",
        "chatCode": "[&BE8CAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-frozen-antrum-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-frozen-antrum-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-frozen-antrum-guild-trek-5.jpg", "http://androuw.e-monsite.com/medias/images/gw2-frozen-antrum-guild-trek-3.jpg"]
    },
    "Rotonde de Soggorsort": {
        "carte": "Fôret de Caledon",
        "tp": "Point de passage de l'Escalier du titan",
        "chatCode": "[&BD0BAAA=]",
        "aide": "Le cercle d'or est à l'intérieur d'une des maisons Quaggan.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-soggorsort-rotunda-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-soggorsort-rotunda-guild-trek-21.jpg", "http://androuw.e-monsite.com/medias/images/gw2-soggorsort-rotunda-guild-trek-41.jpg", "http://androuw.e-monsite.com/medias/images/gw2-soggorsort-rotunda-guild-trek-31.jpg"]
    },
    "Ruelle du vadrouilleur de l'est": {
        "carte": "Promontoire Divin",
        "tp": "Point de passage de Dwayna",
        "chatCode": "[&BCMDAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-east-lurk-alley-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-lurk-alley-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-lurk-alley-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-east-lurk-alley-guild-trek-4.jpg"]
    },
    "Salon d'Esparvent": {
        "carte": "Citadelle Noire",
        "tp": "Point de passage de l'Imperator",
        "chatCode": "[&BK0DAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-sparwinds-lounge-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sparwinds-lounge-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sparwinds-lounge-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sparwinds-lounge-guild-trek-2.jpg"]
    },
    "Salon de Wrelk": {
        "carte": "Champs de Gandarran",
        "tp": "",
        "chatCode": "[&BJQBAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-wrelks-salon-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-wrelks-salon-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-wrelks-salon-guild-trek-3.jpg"]
    },
    "Sanctuaire hanté par un diablotin": {
        "carte": "Fôret de Caledon",
        "tp": "Point de passage du Marais de Wychmire",
        "chatCode": "[&BEEBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-imphaunt-hallow-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-imphaunt-hallow-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-imphaunt-hallow-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-imphaunt-hallow-guild-trek.jpg"]
    },
    "Sanctuaire piersacrée": {
        "carte": "Plateau de Diessa",
        "tp": "",
        "chatCode": "[&BMUDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-holystone-sanctum-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-holystone-sanctum-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-holystone-sanctum-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-holystone-sanctum-guild-trek-2.jpg"]
    },
    "Saut de Drakefaille": {
        "carte": "Champs de Ruines",
        "tp": "Point de passage du Guet de Mordrage",
        "chatCode": "[&BEwBAAA=]",
        "aide": "Le cercle d'or est placé sur un rocher un peu haut au-dessus du sol. Tourner à gauche après être entré dans la grotte et vous trouverez une petite crevasse avec un rocher au sommet.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-drakecleft-shelf-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakecleft-shelf-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakecleft-shelf-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-drakecleft-shelf-guild-trek-5.jpg"]
    },
    "Saut de Mistriven": {
        "carte": "Passage de Lornar",
        "tp": "Point de passage de Mistriven",
        "chatCode": "[&BJkBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-mistriven-shelf-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-mistriven-shelf-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-mistriven-shelf-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-mistriven-shelf-guild-trek-3.jpg"]
    },
    "Saut de la conceptualisation": {
        "carte": "Rata Sum",
        "tp": "Point de passage de l'incubateur",
        "chatCode": "[&BLUEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-ideation-leap-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ideation-leap-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ideation-leap-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-ideation-leap-guild-trek-3.jpg"]
    },
    "Sentinelle Engloutie / Bassin de la Sentinelle": {
        "carte": "Marais de Fer",
        "tp": "Point de passage du Campement du Guet du stigmate",
        "chatCode": "[&BOkBAAA=]",
        "aide": "Le cercle d'or est placé à l'intérieur d'une caverne sous-marine accessible en allant au point localisé par la flèche rouge.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-sentinel-sink-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sentinel-sink-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-sentinel-sink-guild-trek-3.jpg"]
    },
    "Sépulcre azumière": {
        "carte": "Détroit de la Dévastation",
        "tp": "",
        "chatCode": "[&BNIEAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-sepulchre-skylight-guild-trek1.jpg", "http://www.lebusmagique.fr/medias/images/", "http://www.lebusmagique.fr/medias/images/gw2-sepulchre-skylight-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-sepulchre-skylight-guild-trek-2.jpg"]
    },
    "Sépulcre ravagé": {
        "carte": "Plateau de Diessa",
        "tp": "Point de passage des landes ravagées",
        "chatCode": "[&BNoAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-blasted-sepulchre-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blasted-sepulchre-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blasted-sepulchre-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-blasted-sepulchre-guild-trek-3.jpg"]
    },
    "Seuil d'Usharr": {
        "carte": "Marais de Lumillule",
        "tp": "",
        "chatCode": "[&BMsBAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-usharrs-threshold-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-usharrs-threshold-guild-trek-3.jpg", "http://www.lebusmagique.fr/medias/images/gw2-usharrs-threshold-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-usharrs-threshold-guild-trek-4.jpg"]
    },
    "Sommet de l'Epave": {
        "carte": "Citadelle Noire",
        "tp": "Point de passage des épaves",
        "chatCode": "[&BDcEAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-junkers-apex-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-junkers-apex-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-junkers-apex-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-junkers-apex-guild-trek-3.jpg"]
    },
    "Source de Brûlereinette": {
        "carte": "Marais de Lumillule",
        "tp": "Point de passage de Brûlereinette",
        "chatCode": "[&BMwBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-firefrog-springs-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-firefrog-springs-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-firefrog-springs-guild-trek-3.jpg"]
    },
    "Source de Melandru": {
        "carte": "Le Promontoire divin",
        "tp": "",
        "chatCode": "[&BCoDAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-dwaynas-fount-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-dwaynas-fount-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-dwaynas-fount-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-dwaynas-fount-guild-trek-3.jpg"]
    },
    "Source des lamentations": {
        "carte": "Détroit des georges glacées",
        "tp": "",
        "chatCode": "[&BIECAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-source-of-lament-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-source-of-lament-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-source-of-lament-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-source-of-lament-guild-trek-3.jpg"]
    },
    "Surprise d'Elise": {
        "carte": "Harathi Hinterlands",
        "tp": "Point de passage de Demetra",
        "chatCode": "[&BKsAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-elises-suprise-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-elises-suprise-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-elises-suprise-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-elises-suprise-guild-trek-2.jpg"]
    },
    "Surveillant de Folleflamme": {
        "carte": "Province de Metrica",
        "tp": "Point de passage de Soren Draa",
        "chatCode": "[&BEAAAAA=]",
        "aide": "Notez que la marque est au deuxième étage. Il y a des marches en pierre sur les côtés sur lesquelles vous pouver sauter pour atteindre le sommet.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-wildflame-monitor-guild-trek-2.jpg"]
    },
    "Terrasse de Wassa": {
        "carte": "Champs de Gendarran",
        "tp": "Point de passage du Premier Refuge",
        "chatCode": "[&BIsBAAA=]",
        "aide": "Le cercle d'or est placé en haut sur la tour la plus haute.",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-wassas-terrace-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-wassas-terrace-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-wassas-terrace-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-wassas-terrace-guild-trek-4.jpg"]
    },
    "Tour de guet de Mâchefléau": {
        "carte": "Marais de Fer",
        "tp": "Point de passage du camp de Doucepelisse",
        "chatCode": "[&BOgBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-scourgejaw-watchtower-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scourgejaw-watchtower-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scourgejaw-watchtower-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-scourgejaw-watchtower-guild-trek-2.jpg"]
    },
    "Tour de la tribulation": {
        "carte": "Falaises de Hantedraguerre",
        "tp": "",
        "chatCode": "[&BFYCAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-tower-of-tribulation-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tower-of-tribulation-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tower-of-tribulation-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-tower-of-tribulation-guild-trek-3.jpg"]
    },
    "Trou de tirailleur de Creusepierre": {
        "carte": "Champs de Gendarran",
        "tp": "Point de passage de Talajian",
        "chatCode": "[&BIwBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-stonebore-spiderhole-guild-trek1.jpg", "http://androuw.e-monsite.com/medias/images/gw2-stonebore-spiderhole-guild-trek-21.jpg", "http://androuw.e-monsite.com/medias/images/gw2-stonebore-spiderhole-guild-trek-41.jpg"]
    },
    "Tunnel de Bandacier": {
        "carte": "Les Steppes de la Strie Flamboyante",
        "tp": "Point de passage de Tumok",
        "chatCode": "[&BPsBAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-steelbands-tunnel-guild-trek2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-steelbands-tunnel-guild-trek-22.jpg", "http://androuw.e-monsite.com/medias/images/gw2-steelbands-tunnel-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-steelbands-tunnel-guild-trek-5.jpg"]
    },
    "Tunnel sous le lac": {
        "carte": "Vallée de la Reine",
        "tp": "Point de passage de la Scierie d'Ojon",
        "chatCode": "[&BPkAAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-lakebottom-underpass-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lakebottom-underpass-guild-trek-2.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lakebottom-underpass-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-lakebottom-underpass-guild-trek-3.jpg"]
    },
    "Upsilon Hyperboloïde": {
        "carte": "Saut de Malchor",
        "tp": "",
        "chatCode": "[&BKgCAAA=]",
        "aide": "",
        "images": ["http://www.lebusmagique.fr/medias/images/gw2-upsilon-hyperboloid-guild-trek.jpg", "http://www.lebusmagique.fr/medias/images/gw2-upsilon-hyperboloid-guild-trek-2.jpg", "http://www.lebusmagique.fr/medias/images/gw2-upsilon-hyperboloid-guild-trek-4.jpg", "http://www.lebusmagique.fr/medias/images/gw2-upsilon-hyperboloid-guild-trek-3.jpg"]
    },
    "Vallon de Cymbel": {
        "carte": "Champs de Ruines",
        "tp": "Point de passage de la Route de l'Ogre",
        "chatCode": "[&BE8BAAA=]",
        "aide": "",
        "images": ["http://androuw.e-monsite.com/medias/images/gw2-cymbels-glen-guild-trek.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cymbels-glen-guild-trek-4.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cymbels-glen-guild-trek-3.jpg", "http://androuw.e-monsite.com/medias/images/gw2-cymbels-glen-guild-trek-2.jpg"]
    }
}
infoPrimes = {
    '"Adjointe" Brooke':
        {'carte': "Congères d'Antreneige",
        'images': ['http://www.lebusmagique.fr/medias/images/brooke-description.jpg?fx=r_238_103', 'http://www.lebusmagique.fr/medias/images/adjointebrookeprime.jpg?fx=r_60_105', 'https://www.lebusmagique.fr/medias/images/gw2-de10.jpg']},
    'André "Sauvage" Douest':
        {'carte': 'Crique de Sud Soleil',
        'images': ['http://www.lebusmagique.fr/medias/images/gw542-compressed.jpg', 'http://www.lebusmagique.fr/medias/images/gw075-2.jpg?fx=r_43_104', 'https://www.lebusmagique.fr/medias/images/gw2-an12-1-1.jpg']},
    'Bwikki le Rat de bibliothèque':
        {'carte': 'Passage de Lornar',
        'images': ['http://www.lebusmagique.fr/medias/images/bwikkiratprime.jpg?fx=r_271_105', 'http://www.lebusmagique.fr/medias/images/gw081-5.jpg?fx=r_212_400', 'http://androuw.e-monsite.com/medias/images/gw2-bookworm-bwikki-guild-bounty-3.jpg?fx=r_668_668', 'https://www.lebusmagique.fr/medias/images/gw2-bo12.jpg?fx=r_116_300']},
    'Brekkabek le Skritt':
        {'carte': 'Hinterlands Harathis',
        'images': ['http://www.lebusmagique.fr/medias/images/primebrekkabek.jpg?fx=r_271_105', 'http://www.lebusmagique.fr/medias/images/primebrekkabek2.jpg?fx=r_55_105', 'https://www.lebusmagique.fr/medias/images/gw2-br10.jpg?fx=r_278_300']},
    'Chamane Arderus':
        {'carte': 'Montée de Flambecoeur',
        'images': ['http://www.lebusmagique.fr/medias/images/chamanearderusprime.jpg?fx=r_262_105', 'http://www.lebusmagique.fr/medias/images/gw104-compressed.jpg?fx=r_66_104', 'https://www.lebusmagique.fr/medias/images/gw2-shaman-arderus-guild-bounty.jpg?fx=r_505_600']},
    'Croisée Michèle':
        {'carte': 'Marais de Lumillule',
        'images': ['http://www.lebusmagique.fr/medias/images/michele-description.jpg', 'http://www.lebusmagique.fr/medias/images/gw088-6.jpg?fx=r_42_104', 'https://www.lebusmagique.fr/medias/images/gw2-cr11.jpg?fx=r_157_300']},
    'Félix Colairik':
        {'carte': 'Plateau de Diessa',
        'images': ['http://www.lebusmagique.fr/medias/images/gw651-1.jpg?fx=r_400_400', 'http://www.lebusmagique.fr/medias/images/gw108-1.jpg?fx=r_41_150', 'https://www.lebusmagique.fr/medias/images/gw2-short-fuse-felix-guild-bounty-diessa-plateau-map.jpg']},
    'Komali Micui':
        {'carte': 'Mont Maelström',
        'images': ['http://www.lebusmagique.fr/medias/images/primekomalimicui.jpg?fx=r_287_105', 'http://www.lebusmagique.fr/medias/images/gw095-5.jpg?fx=r_70_150', 'http://androuw.e-monsite.com/medias/images/gw2-half-baked-komali-fire-shield-thumb.jpg', 'https://www.lebusmagique.fr/medias/images/gw2-half-baked-komali-map.jpg']},
    'Mayana Imposant':
        {'carte': 'Marais de Lumillule',
        'images': ['http://www.lebusmagique.fr/medias/images/mayanaimposantprime.jpg?fx=r_292_105', 'http://www.lebusmagique.fr/medias/images/mayana.jpg', 'http://www.lebusmagique.fr/medias/images/gw2-big-mayana-guild-bounty-sparkfly-fen-2.jpg?fx=r_247_183', 'https://www.lebusmagique.fr/medias/images/gw2-big-mayana-guild-bounty-sparkfly-fen-map.jpg']},
    'Poobadoo':
        {'carte': 'Collines de Kessex',
        'images': ['http://www.lebusmagique.fr/medias/images/poobadooprime.jpg?fx=r_275_105', 'http://www.lebusmagique.fr/medias/images/primepoobadoo2.jpg?fx=r_287_105', 'https://www.lebusmagique.fr/medias/images/gw2-poobadoo-guild-bounty-kessex-hills-pathing-map.jpg']},
    'Prisonnier 1411':
        {'carte': 'Marais de Fer',
        'images': ['http://www.lebusmagique.fr/medias/images/prisonniere-description.jpg', 'http://www.lebusmagique.fr/medias/images/gw103-compressed.jpg?fx=r_102_150', 'https://www.lebusmagique.fr/medias/images/gw2-prisoner-1141-guild-bounty-pathing-map-3-resized.jpg?fx=r_217_400']},
    '6-RUS':
        {'carte': 'Chutes de la Canopée',
        'images': ['http://www.lebusmagique.fr/medias/images/6rus-description.jpg', 'http://www.lebusmagique.fr/medias/images/6rusprime.jpg?fx=r_79_105', 'https://www.lebusmagique.fr/medias/images/gw2-2-mult-guild-bounty-timberline-falls-pathing-map.jpg?fx=r_185_375']},
    'Sotzz le voyou':
        {'carte': 'Champs de Gendarran',
        'images': ['http://www.lebusmagique.fr/medias/images/sotzzlevoyonprime.jpg?fx=r_290_105', 'http://www.lebusmagique.fr/medias/images/primesotzzlevoyou2.jpg?fx=r_56_105', 'https://www.lebusmagique.fr/medias/images/gw2-sotzz-the-scallywag-guild-bounty-map-5.jpg']},
    'Tarban le Diplomate':
        {'carte': 'Terres sauvages de Brisban',
        'images': ['http://www.lebusmagique.fr/medias/images/gw650-2.jpg?fx=r_400_400', 'http://www.lebusmagique.fr/medias/images/gw093-4.jpg?fx=r_78_150', 'https://www.lebusmagique.fr/medias/images/gw2-di10.jpg']},
    'Teesa la Louche':
        {'carte': 'Détroit des gorges glacées',
        'images': ['http://www.lebusmagique.fr/medias/images/primeteesalalouche.jpg?fx=r_267_105', 'http://www.lebusmagique.fr/medias/images/primeteesalalouche2.jpg?fx=r_70_105', 'https://www.lebusmagique.fr/medias/images/gw2-de11.jpg']},
    'Trekksa la Rusée':
        {'carte': 'Steppes de la Stries Flamboyantes',
        'images': ['http://www.lebusmagique.fr/medias/images/trekksa-description.jpg?fx=r_382_150', 'http://www.lebusmagique.fr/medias/images/trekksa.jpg?fx=r_114_103', 'https://www.lebusmagique.fr/medias/images/gw2-curious-cow-guild-bounty-pathing-map-resized.jpg?fx=r_146_375']},
    'Trillia Mylieu':
        {'carte': 'Champs de ruines',
        'images': ['http://www.lebusmagique.fr/medias/images/primetrillianmylieu.jpg?fx=r_266_105', 'http://www.lebusmagique.fr/medias/images/primetrilliamylieu2.jpg?fx=r_56_105', 'https://www.lebusmagique.fr/medias/images/gw2-trillia-midwell-guild-bounty-fields-of-ruin-map.jpg?fx=r_167_275']},
    'Yanonka, la palefrenière de rats':
        {'carte': 'Champs de ruines',
        'images': ['http://www.lebusmagique.fr/medias/images/primeyanonka.jpg?fx=r_275_105', 'http://www.lebusmagique.fr/medias/images/yannonka-compressed.jpg', 'http://www.lebusmagique.fr/medias/images/gw2-yanonka-the-rat-wrangler-fields-of-ruin-map-2.jpg?fx=r_215_183', 'https://www.lebusmagique.fr/medias/images/gw2-yanonka-the-rat-wrangler-fields-of-ruin-map.jpg']}}

noms_randos = np.array(list(infoRandos.keys()))
noms_primes = np.array(list(infoPrimes.keys()))

def remove_accents(txt):
    spec_char = {'à': 'a', 'â': 'a','ç': 'c', 'é': 'e', 'è': 'e', 'ë': 'e', 'ê': 'e','î': 'i', 'ï': 'i', 'ô': 'o', 'œ': 'oe', 'ù': 'u', 'û':'u'}
    new_txt = txt.lower()
    for k, v in spec_char.items():
        new_txt = new_txt.replace(k, v)
    return new_txt

@client.event
async def on_message(message):
    if message.content.startswith('Tybalt,'):
        channel = message.channel
        reply = message.content.replace('Tybalt,', '')
        if reply.find('trek:') >= 0:
            arg = reply.replace('trek:', '')
            keywords = [remove_accents(x).strip().lower() for x in arg.split(',')]
            found = np.logical_or.reduce(np.array([[remove_accents(n).lower().find(k) != -1 for n in noms_randos] for k in keywords]))
            lieux_trouves = list(noms_randos[found])
            print(len(lieux_trouves))
            for n in lieux_trouves:
                msg = n + "\n" + infoRandos[n]['carte'] + "\n" + infoRandos[n]['chatCode'] + "\n" + infoRandos[n]['images'][-1]
                await channel.send(msg)
        elif reply.find('bounty:') >= 0:
            arg = reply.replace('bounty:', '')
            keywords = [remove_accents(x).strip().lower() for x in arg.split(',')]
            found = np.logical_or.reduce(np.array([[remove_accents(n).lower().find(k) != -1 for n in noms_primes] for k in keywords]))
            lieux_trouves = list(noms_primes[found])
            print(len(lieux_trouves))
            for n in lieux_trouves:
                msg = n + "\n" + infoPrimes[n]['carte'] + "\n" + infoPrimes[n]['images'][-1]
                await channel.send(msg)
        else:
            await channel.send("Je ne peux pas le faire! GRAAAAAAAAA!")            

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="avec la main gauche"))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
