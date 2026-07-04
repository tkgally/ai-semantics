#!/usr/bin/env python3
"""Build + certify + freeze the dative information-structure stimuli — POWERED re-run.

This is a fresh, DISJOINT, POWERED item set on the SAME frozen instrument as v1/v2
(2026-06-20-dative-information-structure{,-v2}) and the SAME ratified operationalization
(decisions/resolved/dative-anchor-and-indicator, ADOPT MODIFIED). No design change, no new
decision: every scenario (subjects, recipients, themes, discourse contexts) is newly authored
and shares no (subject, recipient, theme) item and no context sentence with v1 or v2. The
point is POWER: attach a magnitude+interval to claim/dative-information-structure-givenness
(PROTOCOL §4, program A2a "dative information-structure [ ]"), exactly as session 169's
136-item CC powered re-run attached a magnitude to the CC claim. N: 100 main + 12 control
(the ~100-150 powered floor of PROTOCOL §4; the PRIMARY estimate is over the 100 main items,
so the main arm is what is powered; the 12-item control arm is the same end-weight dissociation
check as v1/v2, kept at its certified minimum rather than scaled, because it is a robustness
check, not the powered magnitude).

DESIGN (byte-identical to v1/v2). The givenness manipulation lives in the *discourse context*,
never in the NPs: the SAME double-object (DOC) / prepositional-dative (PD) phrasing pair —
identical words, identical recipient/theme lengths, identical animacy — is rated under different
prior contexts that establish which referent is discourse-GIVEN. The primary measure is the
WITHIN-ITEM preference shift across contexts:

    shift(item) = pref(DOC | recipient-given) - pref(DOC | theme-given)

Human prediction: shift > 0 (given-before-new: a given recipient -> DOC; a given theme -> PD).
Because every surface feature of the test sentence is held identical across an item's two
contexts, ANY reader whose output depends only on the test sentence (its lengths, its A/B order,
an always-DOC/always-PD bias, a shorter-first / longer-first end-weight rule) produces the SAME
score in both contexts -> shift = 0 -> at chance on the contrast. Only a reader that uses the
prior context (tracks givenness) can move the shift off zero. The certification below (identical
to v1/v2) proves this for an enumerated shortcut-reader family; condition (a) (within-pair
length variance = 0) holds by construction.

Arms:
  - MAIN (100 items): recipient and theme of equal word length (3/3), rated in recipient-given,
    theme-given, and both-new (neutral baseline) contexts.
  - CONTROL (12 items, condition (b)): a large recipient/theme length gap, so in the dissociating
    context information structure predicts the LONGER constituent first while end-weight
    (short-before-long) predicts the shorter first -> OPPOSITE absolute orderings. 6 are
    long-recipient (recipient-given dissociates) and 6 long-theme (theme-given dissociates). The
    control item ids are clong1..6 / tlong1..6 because analyze.py (frozen, reused verbatim)
    hardcodes INANIMATE_REC_ITEMS = {tlong1..tlong6} for the SECONDARY corpus-gradient's
    conservative animacy coding of the institutional long-theme recipients.

Outputs: stimuli.json (frozen, sha-pinned in PREREG), and a printed certification report.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def wc(s: str) -> int:
    """Word count of an NP (the corpus's LengthOf* unit: whitespace tokens)."""
    return len(s.split())


# ---------------------------------------------------------------------------
# MAIN items (100). Each: verb (past, canonical alternating dative), subject NP, recipient NP
# (animate, definite, 3 words), theme NP (inanimate, indefinite, 3 words), and three prior
# contexts establishing givenness by PRIOR MENTION (no dative phrasing / no item-verb inside a
# context -> no answer leakage). The test-sentence NPs are IDENTICAL across the three contexts.
#   rec_given : prior sentence names the recipient referent (recipient = discourse-given)
#   thm_given : prior sentence names the theme referent      (theme     = discourse-given)
#   neutral   : a scene-setter naming neither referent        (both new) -> baseline
# All 100 main items are newly authored; none appears in v1 or v2. Drafted across four domains
# (business/finance, education/arts, sports/travel/hospitality, medical/domestic/civic) and
# hand-screened; exact-duplicate themes deduped (see p046/p082/p095).
# ---------------------------------------------------------------------------

MAIN = [
    dict(id="p001", verb="offered", subj="The manager", rec="the night auditor", thm="a signed contract",
         rec_given="The night auditor had worked alone since midnight.",
         thm_given="A signed contract sat in the folder unread.",
         neutral="The building's lobby stayed quiet after hours."),
    dict(id="p002", verb="paid", subj="The store owner", rec="the head cashier", thm="a crisp banknote",
         rec_given="The head cashier had balanced every till that week.",
         thm_given="A crisp banknote lay flat on the counter.",
         neutral="The shop's shelves gleamed under new lighting."),
    dict(id="p003", verb="showed", subj="The supervisor", rec="the sales intern", thm="a quarterly forecast",
         rec_given="The sales intern arrived early for the meeting.",
         thm_given="A quarterly forecast covered the entire whiteboard.",
         neutral="The conference room smelled of fresh coffee."),
    dict(id="p004", verb="handed", subj="The customer", rec="the branch teller", thm="a printed paycheck",
         rec_given="The branch teller smiled at the next person.",
         thm_given="A printed paycheck needed a countersignature first.",
         neutral="The bank's floor buzzed near closing time."),
    dict(id="p005", verb="sent", subj="The director", rec="the floor manager", thm="a revised schedule",
         rec_given="The floor manager oversaw two dozen staff.",
         thm_given="A revised schedule changed everyone's Monday shift.",
         neutral="The warehouse hummed with forklifts and pallets."),
    dict(id="p006", verb="owed", subj="The company", rec="the payroll clerk", thm="a back payment",
         rec_given="The payroll clerk flagged the error immediately.",
         thm_given="A back payment had been pending for weeks.",
         neutral="The finance office kept its blinds drawn."),
    dict(id="p007", verb="mailed", subj="The firm", rec="the legal secretary", thm="a sealed envelope",
         rec_given="The legal secretary logged every incoming file.",
         thm_given="A sealed envelope waited in the tray.",
         neutral="The office corridor was lined with framed diplomas."),
    dict(id="p008", verb="brought", subj="The courier", rec="the mailroom worker", thm="a padded package",
         rec_given="The mailroom worker sorted bins all morning.",
         thm_given="A padded package bore a fragile sticker.",
         neutral="The loading dock rattled under the summer heat."),
    dict(id="p009", verb="lent", subj="The colleague", rec="the store owner", thm="a spare ledger",
         rec_given="The store owner counted inventory late again.",
         thm_given="A spare ledger held last year's totals.",
         neutral="The stockroom smelled of cardboard and dust."),
    dict(id="p010", verb="promised", subj="The executive", rec="the shift supervisor", thm="a job offer",
         rec_given="The shift supervisor stayed past every closing.",
         thm_given="A job offer depended on the board's vote.",
         neutral="The break room clock ticked toward midnight."),
    dict(id="p011", verb="taught", subj="The mentor", rec="the new bookkeeper", thm="a handy macro",
         rec_given="The new bookkeeper studied the ledgers carefully.",
         thm_given="A handy macro sped the whole process up.",
         neutral="The accounting wing stayed lit past nine."),
    dict(id="p012", verb="granted", subj="The board", rec="the corporate recruiter", thm="an annual budget",
         rec_given="The corporate recruiter screened forty résumés today.",
         thm_given="An annual budget would fund three new hires.",
         neutral="The hiring floor was a maze of cubicles."),
    dict(id="p013", verb="wrote", subj="The auditor", rec="the account executive", thm="a stern memo",
         rec_given="The account executive lost the biggest client.",
         thm_given="A stern memo circulated by end of day.",
         neutral="The top floor overlooked the river below."),
    dict(id="p014", verb="sold", subj="The vendor", rec="the warehouse foreman", thm="a wooden crate",
         rec_given="The warehouse foreman checked each pallet twice.",
         thm_given="A wooden crate blocked the narrow aisle.",
         neutral="The depot's roll-up doors clanged open at dawn."),
    dict(id="p015", verb="passed", subj="The manager", rec="the office receptionist", thm="an expense claim",
         rec_given="The office receptionist greeted every visitor warmly.",
         thm_given="An expense claim needed one more signature.",
         neutral="The reception area featured fresh cut flowers."),
    dict(id="p016", verb="read", subj="The chair", rec="the district auditor", thm="an audit summary",
         rec_given="The district auditor questioned every line item.",
         thm_given="An audit summary ran to forty pages.",
         neutral="The boardroom's long table gleamed under spotlights."),
    dict(id="p017", verb="gave", subj="The partner", rec="the loan officer", thm="a rate quote",
         rec_given="The loan officer reviewed the application twice.",
         thm_given="A rate quote listed every closing cost.",
         neutral="The mortgage desk fielded calls all afternoon."),
    dict(id="p018", verb="told", subj="The regional head", rec="the retail cashier", thm="a plain truth",
         rec_given="The retail cashier had rung up the sale.",
         thm_given="A plain truth surfaced during the review.",
         neutral="The mall's food court echoed at noon."),
    dict(id="p019", verb="awarded", subj="The committee", rec="the compliance officer", thm="a merit citation",
         rec_given="The compliance officer flagged the missing filings.",
         thm_given="A merit citation honored the year's work.",
         neutral="The banquet hall filled with quiet applause."),
    dict(id="p020", verb="served", subj="The waiter", rec="the junior accountant", thm="a free lunch",
         rec_given="The junior accountant skipped every break today.",
         thm_given="A free lunch grew cold on the desk.",
         neutral="The office café rattled with the espresso machine."),
    dict(id="p021", verb="tossed", subj="The clerk", rec="the visiting auditor", thm="a stapled folder",
         rec_given="The visiting auditor toured each department briefly.",
         thm_given="A stapled folder held the quarter's receipts.",
         neutral="The records room overflowed with old binders."),
    dict(id="p022", verb="threw", subj="The stocker", rec="the produce vendor", thm="a plastic crate",
         rec_given="The produce vendor haggled with early shoppers.",
         thm_given="A plastic crate cracked along one edge.",
         neutral="The market stalls opened under grey skies."),
    dict(id="p023", verb="wired", subj="The company", rec="the counter clerk", thm="a holiday stipend",
         rec_given="The counter clerk closed out the register.",
         thm_given="A holiday stipend arrived earlier than usual.",
         neutral="The payroll system ran its nightly batch."),
    dict(id="p024", verb="offered", subj="The landlord", rec="the seasonal temp", thm="a draft lease",
         rec_given="The seasonal temp signed on through December.",
         thm_given="A draft lease covered just three months.",
         neutral="The rental office posted new listings weekly."),
    dict(id="p025", verb="paid", subj="The garage", rec="the parking attendant", thm="a nightly wage",
         rec_given="The parking attendant waved each car through.",
         thm_given="A nightly wage barely covered the rent.",
         neutral="The concrete ramp echoed with distant engines."),
    dict(id="p026", verb="lent", subj="The librarian", rec="the bewildered freshman", thm="an illustrated atlas",
         rec_given="The bewildered freshman wandered the unfamiliar corridors.",
         thm_given="An illustrated atlas lay open on the desk.",
         neutral="Dust motes drifted through the afternoon light."),
    dict(id="p027", verb="taught", subj="The composer", rec="the gifted cellist", thm="a tricky passage",
         rec_given="The gifted cellist practiced late into the night.",
         thm_given="A tricky passage stumped the whole orchestra.",
         neutral="The rehearsal hall echoed with tuning notes."),
    dict(id="p028", verb="handed", subj="The editor", rec="the unknown novelist", thm="a marked proof",
         rec_given="The unknown novelist waited by the office door.",
         thm_given="A marked proof carried red ink in every margin.",
         neutral="Deadlines loomed across the cluttered newsroom."),
    dict(id="p029", verb="showed", subj="The curator", rec="the aspiring painter", thm="a hidden canvas",
         rec_given="The aspiring painter sketched in the corner all morning.",
         thm_given="A hidden canvas leaned against the storeroom wall.",
         neutral="The gallery lights hummed above bare white walls."),
    dict(id="p030", verb="read", subj="The poet", rec="the drowsy audience", thm="a quiet verse",
         rec_given="The drowsy audience shifted in their velvet seats.",
         thm_given="A quiet verse suited the dim evening mood.",
         neutral="Candles flickered along the edge of the stage."),
    dict(id="p031", verb="mailed", subj="The registrar", rec="the puzzled sophomore", thm="a course schedule",
         rec_given="The puzzled sophomore checked the porch every morning.",
         thm_given="A course schedule listed every required seminar.",
         neutral="Autumn leaves gathered along the campus paths."),
    dict(id="p032", verb="awarded", subj="The dean", rec="the diligent postdoc", thm="a prestigious fellowship",
         rec_given="The diligent postdoc had published three papers already.",
         thm_given="A prestigious fellowship opened only once a decade.",
         neutral="The oak-paneled office overlooked the quiet quad."),
    dict(id="p033", verb="granted", subj="The board", rec="the earnest lecturer", thm="a summer stipend",
         rec_given="The earnest lecturer stayed after every evening class.",
         thm_given="A summer stipend covered the season's research costs.",
         neutral="Rain streaked the windows of the science building."),
    dict(id="p034", verb="offered", subj="The publisher", rec="the emerging poet", thm="a two-book contract",
         rec_given="The emerging poet had waited years for this.",
         thm_given="A two-book contract lay unsigned on the table.",
         neutral="Traffic murmured beyond the tall office windows."),
    dict(id="p035", verb="sold", subj="The dealer", rec="the talented violinist", thm="an antique bow",
         rec_given="The talented violinist had saved for months.",
         thm_given="An antique bow rested in the velvet case.",
         neutral="The shop smelled of resin and old wood."),
    dict(id="p036", verb="served", subj="The bookseller", rec="the quiet patron", thm="a spiced cider",
         rec_given="The quiet patron settled into the reading nook.",
         thm_given="A spiced cider steamed on the counter.",
         neutral="Jazz played softly through the crowded store."),
    dict(id="p037", verb="paid", subj="The theatre", rec="the lead actress", thm="a weekly wage",
         rec_given="The lead actress arrived early for every performance.",
         thm_given="A weekly wage barely covered her rent.",
         neutral="Stagehands adjusted ropes high above the stage."),
    dict(id="p038", verb="promised", subj="The director", rec="the promising dancer", thm="a leading part",
         rec_given="The promising dancer rehearsed alone every dawn.",
         thm_given="A leading part could change her career.",
         neutral="The theatre buzzed before opening night."),
    dict(id="p039", verb="told", subj="The novelist", rec="the rapt reader", thm="a strange rumor",
         rec_given="The rapt reader leaned closer to hear.",
         thm_given="A strange rumor had circulated for years.",
         neutral="The bookshop clock ticked toward closing time."),
    dict(id="p040", verb="wrote", subj="The mentor", rec="the jobless graduate", thm="a glowing reference",
         rec_given="The jobless graduate awaited news of the position.",
         thm_given="A glowing reference could open many doors.",
         neutral="Snow settled softly on the college rooftops."),
    dict(id="p041", verb="sent", subj="The agent", rec="the overworked screenwriter", thm="a revised outline",
         rec_given="The overworked screenwriter juggled three projects at once.",
         thm_given="A revised outline reworked the entire second act.",
         neutral="Los Angeles smog hung over the studio lot."),
    dict(id="p042", verb="brought", subj="The stagehand", rec="the celebrated tenor", thm="a chilled tonic",
         rec_given="The celebrated tenor waited nervously in the wings.",
         thm_given="A chilled tonic sat on the dressing table.",
         neutral="The orchestra pit filled with restless murmurs."),
    dict(id="p043", verb="passed", subj="The conductor", rec="the principal violinist", thm="a bound score",
         rec_given="The principal violinist tuned carefully before the concert.",
         thm_given="A bound score contained the evening's program.",
         neutral="The concert hall dimmed as latecomers hurried in."),
    dict(id="p044", verb="threw", subj="The drama teacher", rec="the trembling understudy", thm="a backup script",
         rec_given="The trembling understudy mouthed the lines silently.",
         thm_given="A backup script lay near the prompt corner.",
         neutral="The auditorium seats stretched into darkness."),
    dict(id="p045", verb="tossed", subj="The coach", rec="the marching drummer", thm="a rolled banner",
         rec_given="The marching drummer kept perfect time downfield.",
         thm_given="A rolled banner leaned against the bleachers.",
         neutral="The halftime crowd filed back to their seats."),
    dict(id="p046", verb="owed", subj="The department", rec="the adjunct instructor", thm="a term stipend",
         rec_given="The adjunct instructor covered four sections that semester.",
         thm_given="A term stipend had been delayed for months.",
         neutral="Fluorescent lights buzzed in the empty hallway."),
    dict(id="p047", verb="gave", subj="The choir master", rec="the timid soprano", thm="a solo part",
         rec_given="The timid soprano trembled before the audition.",
         thm_given="A solo part demanded years of training.",
         neutral="The chapel's stained glass glowed at sunset."),
    dict(id="p048", verb="wired", subj="The foundation", rec="the touring pianist", thm="an emergency advance",
         rec_given="The touring pianist performed in six cities weekly.",
         thm_given="An emergency advance kept the tour afloat.",
         neutral="The concert schedule sprawled across the whiteboard."),
    dict(id="p049", verb="fed", subj="The keeper", rec="the observant biologist", thm="a green fig",
         rec_given="The observant biologist recorded notes beside the enclosure.",
         thm_given="A green fig sat in the feeding tray.",
         neutral="The aviary echoed with unfamiliar birdsong."),
    dict(id="p050", verb="handed", subj="The archivist", rec="the amateur genealogist", thm="a fragile ledger",
         rec_given="The amateur genealogist visited the archive each Tuesday.",
         thm_given="A fragile ledger documented the town's early trade.",
         neutral="The vault kept a steady, cool temperature."),
    dict(id="p051", verb="offered", subj="The ranger", rec="the tired hiker", thm="a chilled towel",
         rec_given="The tired hiker slumped against a mossy boulder.",
         thm_given="A chilled towel waited in the cooler.",
         neutral="The trail climbed steeply toward the misty summit."),
    dict(id="p052", verb="tossed", subj="The river guide", rec="the lost kayaker", thm="a spare paddle",
         rec_given="The lost kayaker drifted near the tangled reeds.",
         thm_given="A spare paddle floated beside the wooden dock.",
         neutral="Fog settled thickly over the silent inlet."),
    dict(id="p053", verb="handed", subj="The night manager", rec="the cheerful bellhop", thm="a room key",
         rec_given="The cheerful bellhop whistled beside the brass elevator.",
         thm_given="A room key rested on the marble counter.",
         neutral="The lobby glowed under soft morning light."),
    dict(id="p054", verb="brought", subj="The beach waitress", rec="the sunburned surfer", thm="a cold lemonade",
         rec_given="The sunburned surfer collapsed onto a striped lounger.",
         thm_given="A cold lemonade sweated on the bamboo tray.",
         neutral="Waves rolled steadily along the golden shore."),
    dict(id="p055", verb="fed", subj="The camp cook", rec="the hungry climber", thm="a salty snack",
         rec_given="The hungry climber reached base camp utterly spent.",
         thm_given="A salty snack sat inside the mess tent.",
         neutral="Snow dusted the jagged peaks before dawn."),
    dict(id="p056", verb="showed", subj="The old traveler", rec="the polite concierge", thm="a brass compass",
         rec_given="The polite concierge greeted every arriving visitor warmly.",
         thm_given="A brass compass gleamed within the display case.",
         neutral="The grand hotel smelled of cedar and rain."),
    dict(id="p057", verb="served", subj="The poolside waiter", rec="the drenched cyclist", thm="a sports drink",
         rec_given="The drenched cyclist wobbled through the finish gate.",
         thm_given="A sports drink chilled in the icy bucket.",
         neutral="The afternoon heat shimmered above the pavement."),
    dict(id="p058", verb="gave", subj="The pro shop clerk", rec="the nervous caddie", thm="a golf scorecard",
         rec_given="The nervous caddie fidgeted near the first tee.",
         thm_given="A golf scorecard lay atop the counter.",
         neutral="Sprinklers hissed across the emerald fairways."),
    dict(id="p059", verb="lent", subj="The harbor master", rec="the seasoned skipper", thm="a life vest",
         rec_given="The seasoned skipper studied the darkening horizon.",
         thm_given="A life vest hung by the cabin door.",
         neutral="Gulls wheeled above the crowded marina."),
    dict(id="p060", verb="promised", subj="The front desk clerk", rec="the jetlagged guest", thm="a wake-up call",
         rec_given="The jetlagged guest yawned throughout the check-in.",
         thm_given="A wake-up call was scheduled for six sharp.",
         neutral="Rain streaked the tall windows overlooking the bay."),
    dict(id="p061", verb="awarded", subj="The league official", rec="the winning goalie", thm="a champion's cup",
         rec_given="The winning goalie pumped both fists triumphantly.",
         thm_given="A champion's cup glittered on the podium.",
         neutral="Confetti drifted across the roaring stadium."),
    dict(id="p062", verb="passed", subj="The camp warden", rec="the shivering camper", thm="a dry sleeping-bag",
         rec_given="The shivering camper huddled by the dying embers.",
         thm_given="A dry sleeping-bag lay rolled inside the truck.",
         neutral="A cold wind howled through the pine forest."),
    dict(id="p063", verb="threw", subj="The match steward", rec="the veteran referee", thm="a red whistle",
         rec_given="The veteran referee jogged onto the muddy pitch.",
         thm_given="A red whistle dangled from the hook.",
         neutral="Floodlights blazed above the packed terraces."),
    dict(id="p064", verb="brought", subj="The aid volunteer", rec="the parched runner", thm="a fresh water-bottle",
         rec_given="The parched runner staggered past the last marker.",
         thm_given="A fresh water-bottle stood on the folding stand.",
         neutral="Heat rose in waves from the long road."),
    dict(id="p065", verb="tossed", subj="The stadium vendor", rec="the rowdy fans", thm="a free pretzel",
         rec_given="The rowdy fans chanted from the upper deck.",
         thm_given="A free pretzel steamed under the warming lamp.",
         neutral="The scoreboard flickered above the restless crowd."),
    dict(id="p066", verb="sent", subj="The travel agent", rec="the calm pilot", thm="a printed itinerary",
         rec_given="The calm pilot reviewed the weather over coffee.",
         thm_given="A printed itinerary sat inside the folder.",
         neutral="The terminal buzzed with early-morning departures."),
    dict(id="p067", verb="gave", subj="The lodge keeper", rec="the patient instructor", thm="a wool scarf",
         rec_given="The patient instructor waited at the slope bottom.",
         thm_given="A wool scarf hung near the crackling fireplace.",
         neutral="Fresh powder blanketed the quiet mountainside."),
    dict(id="p068", verb="handed", subj="The stable hand", rec="the young jockey", thm="a numbered bib",
         rec_given="The young jockey checked the saddle one final time.",
         thm_given="A numbered bib waited on the tack rail.",
         neutral="The paddock buzzed before the afternoon race."),
    dict(id="p069", verb="sold", subj="The station agent", rec="the wandering backpacker", thm="a bus ticket",
         rec_given="The wandering backpacker paused at the station window.",
         thm_given="A bus ticket poked out of the machine.",
         neutral="Travelers hurried across the crowded concourse."),
    dict(id="p070", verb="offered", subj="The resort clerk", rec="the friendly innkeeper", thm="a free upgrade",
         rec_given="The friendly innkeeper chatted with newly arrived visitors.",
         thm_given="A free upgrade appeared in the booking system.",
         neutral="Palm trees swayed beside the sparkling pool."),
    dict(id="p071", verb="brought", subj="The dive master", rec="the certified diver", thm="an air tank",
         rec_given="The certified diver checked her gauges carefully.",
         thm_given="An air tank rested against the boat rail.",
         neutral="The reef shimmered beneath the clear blue water."),
    dict(id="p072", verb="lent", subj="The groundskeeper", rec="the quiet gardener", thm="a garden trowel",
         rec_given="The quiet gardener knelt among the rose beds.",
         thm_given="A garden trowel lay beside the potting bench.",
         neutral="Morning dew clung to the trimmed hedges."),
    dict(id="p073", verb="gave", subj="The valet", rec="the hotel porter", thm="a luggage cart",
         rec_given="The hotel porter waited beneath the wide awning.",
         thm_given="A luggage cart stood near the revolving door.",
         neutral="Taxis idled along the busy front driveway."),
    dict(id="p074", verb="brought", subj="The pastry chef", rec="the head hostess", thm="a warm cookie",
         rec_given="The head hostess reviewed the evening reservations.",
         thm_given="A warm cookie cooled on the wire rack.",
         neutral="Candlelight flickered across the linen tablecloths."),
    dict(id="p075", verb="tossed", subj="The head guard", rec="the brave lifeguard", thm="a rescue rope",
         rec_given="The brave lifeguard scanned the churning surf.",
         thm_given="A rescue rope coiled near the watchtower.",
         neutral="Red flags snapped in the stiff sea breeze."),
    dict(id="p076", verb="showed", subj="The vet tech", rec="the nervous kitten", thm="a soft toy",
         rec_given="The nervous kitten hid under the exam table.",
         thm_given="A soft toy lay in the carrier.",
         neutral="The clinic smelled faintly of antiseptic."),
    dict(id="p077", verb="handed", subj="The nurse", rec="the elderly patient", thm="a paper cup",
         rec_given="The elderly patient shifted on the gurney.",
         thm_given="A paper cup sat on the tray.",
         neutral="Monitors beeped down the quiet corridor."),
    dict(id="p078", verb="mailed", subj="The pharmacy", rec="the diabetic patient", thm="a refill notice",
         rec_given="The diabetic patient checked the porch each morning.",
         thm_given="A refill notice was overdue by a week.",
         neutral="Rain streaked the pharmacy windows all day."),
    dict(id="p079", verb="read", subj="The father", rec="the youngest child", thm="a bedtime story",
         rec_given="The youngest child begged to stay up late.",
         thm_given="A bedtime story waited on the nightstand.",
         neutral="The hallway light flickered before dinner."),
    dict(id="p080", verb="lent", subj="The neighbor", rec="the new tenant", thm="a spare key",
         rec_given="The new tenant had just moved in upstairs.",
         thm_given="A spare key hung by the door.",
         neutral="The stairwell echoed with footsteps at noon."),
    dict(id="p081", verb="granted", subj="The city clerk", rec="the small charity", thm="a modest permit",
         rec_given="The small charity had applied months ago.",
         thm_given="A modest permit was still pending review.",
         neutral="The town hall clock struck noon."),
    dict(id="p082", verb="paid", subj="The treasurer", rec="the road crew", thm="a lump sum",
         rec_given="The road crew had worked through the weekend.",
         thm_given="A lump sum was finally approved.",
         neutral="Orange cones lined the busy intersection."),
    dict(id="p083", verb="taught", subj="The professor", rec="the lab intern", thm="a new method",
         rec_given="The lab intern arrived early every morning.",
         thm_given="A new method promised faster results.",
         neutral="Fume hoods hummed along the back wall."),
    dict(id="p084", verb="sent", subj="The researcher", rec="the peer reviewer", thm="a revised draft",
         rec_given="The peer reviewer had requested more data.",
         thm_given="A revised draft sat in the queue.",
         neutral="The printer jammed twice before noon."),
    dict(id="p085", verb="fed", subj="The rancher", rec="the newborn calf", thm="a warm mash",
         rec_given="The newborn calf wobbled on shaky legs.",
         thm_given="A warm mash steamed in the bucket.",
         neutral="Dawn broke gray over the muddy paddock."),
    dict(id="p086", verb="threw", subj="The trainer", rec="the eager retriever", thm="a red ball",
         rec_given="The eager retriever bounded across the field.",
         thm_given="A red ball rolled into the grass.",
         neutral="The park gates opened at sunrise."),
    dict(id="p087", verb="offered", subj="The surgeon", rec="the frightened teen", thm="a calm word",
         rec_given="The frightened teen gripped the bed rail.",
         thm_given="A calm word could ease the wait.",
         neutral="Fluorescent lights buzzed over the scrub sink."),
    dict(id="p088", verb="told", subj="The counselor", rec="the grieving widow", thm="a hard truth",
         rec_given="The grieving widow sat quietly in the chair.",
         thm_given="A hard truth had to be spoken.",
         neutral="The office plant needed watering again."),
    dict(id="p089", verb="awarded", subj="The mayor", rec="the local firefighter", thm="a bronze medal",
         rec_given="The local firefighter had saved two families.",
         thm_given="A bronze medal gleamed on the podium.",
         neutral="Flags snapped in the afternoon breeze."),
    dict(id="p090", verb="wired", subj="The lab director", rec="the field assistant", thm="a small stipend",
         rec_given="The field assistant camped near the reef.",
         thm_given="A small stipend covered the travel costs.",
         neutral="The generator rumbled behind the tent."),
    dict(id="p091", verb="promised", subj="The mother", rec="the restless twins", thm="a fun outing",
         rec_given="The restless twins bounced on the couch.",
         thm_given="A fun outing depended on good weather.",
         neutral="The kitchen radio played softly all morning."),
    dict(id="p092", verb="brought", subj="The volunteer", rec="the injured hawk", thm="a fresh mouse",
         rec_given="The injured hawk perched warily in the cage.",
         thm_given="A fresh mouse waited in the cooler.",
         neutral="The rehab center opened before dawn."),
    dict(id="p093", verb="wrote", subj="The doctor", rec="the anxious intern", thm="a clear order",
         rec_given="The anxious intern paced outside the ward.",
         thm_given="A clear order avoided any confusion.",
         neutral="Charts stacked up at the nurses' station."),
    dict(id="p094", verb="passed", subj="The chemist", rec="the careful technician", thm="a sealed vial",
         rec_given="The careful technician double-checked every label.",
         thm_given="A sealed vial held the sample.",
         neutral="The centrifuge spun in the corner."),
    dict(id="p095", verb="owed", subj="The county", rec="the part-time clerk", thm="a late reimbursement",
         rec_given="The part-time clerk had waited two months.",
         thm_given="A late reimbursement appeared on the ledger.",
         neutral="The records room smelled of old paper."),
    dict(id="p096", verb="served", subj="The host", rec="the hungry guests", thm="a warm meal",
         rec_given="The hungry guests gathered around the table.",
         thm_given="A warm meal filled the house with aroma.",
         neutral="Candles flickered in the dim dining room."),
    dict(id="p097", verb="gave", subj="The groomer", rec="the shivering puppy", thm="a gentle bath",
         rec_given="The shivering puppy whimpered on the table.",
         thm_given="A gentle bath would calm the nerves.",
         neutral="The dryer hummed in the back room."),
    dict(id="p098", verb="sold", subj="The optician", rec="the older gentleman", thm="a sturdy frame",
         rec_given="The older gentleman squinted at the chart.",
         thm_given="A sturdy frame suited his active life.",
         neutral="Sample glasses lined the polished counter."),
    dict(id="p099", verb="tossed", subj="The technician", rec="the waiting colleague", thm="a marker pen",
         rec_given="The waiting colleague stood by the whiteboard.",
         thm_given="A marker pen had rolled off the desk.",
         neutral="The seminar room filled slowly with chatter."),
    dict(id="p100", verb="handed", subj="The registrar", rec="the newlywed pair", thm="a signed license",
         rec_given="The newlywed pair beamed at the counter.",
         thm_given="A signed license made it official.",
         neutral="The clerk's office bustled on Monday morning."),
]

# CONTROL arm: large length gap so end-weight has a definite prediction that OPPOSES information
# structure in the dissociating context. clong = long recipient + short theme: in the
# recipient-given context, info -> DOC (given recipient first) but end-weight -> PD (heavy
# recipient last) -> dissociation. tlong = long theme + short recipient: in the theme-given
# context, info -> PD (given theme first) but end-weight -> DOC (heavy theme last) -> dissociation.
# tlong recipients are institutions (coded inanimate, conservative, in the SECONDARY
# corpus-gradient only -- analyze.py INANIMATE_REC_ITEMS = {tlong1..tlong6}). All 12 control
# items are newly authored; none appears in v1 or v2.

CONTROL = [
    # --- long recipient, short theme (recipient-given context dissociates) ---
    dict(id="clong1", verb="handed", subj="The steward", rec="the passenger seated in the last row", thm="a voucher",
         rec_given="The passenger seated in the last row rang the call bell.",
         thm_given="A voucher had been prepared for the long delay.",
         neutral="The cabin lights dimmed for the night flight."),
    dict(id="clong2", verb="offered", subj="The manager", rec="the analyst who had flagged the error", thm="a payout",
         rec_given="The analyst who had flagged the error spoke up first.",
         thm_given="A payout had been set aside that quarter.",
         neutral="The trading floor quieted after the closing bell."),
    dict(id="clong3", verb="mailed", subj="The registrar", rec="the student who missed the enrollment deadline", thm="a form",
         rec_given="The student who missed the enrollment deadline called the office twice.",
         thm_given="A form was required before any late entry.",
         neutral="The campus gates closed early over the break."),
    dict(id="clong4", verb="paid", subj="The promoter", rec="the vendor at the far end of the market", thm="a deposit",
         rec_given="The vendor at the far end of the market packed up slowly.",
         thm_given="A deposit was due before the weekend fair.",
         neutral="The stall awnings flapped in the afternoon wind."),
    dict(id="clong5", verb="showed", subj="The docent", rec="the tourist lingering by the museum entrance", thm="a shortcut",
         rec_given="The tourist lingering by the museum entrance looked quite lost.",
         thm_given="A shortcut through the galleries saved several minutes.",
         neutral="The marble halls echoed with distant footsteps."),
    dict(id="clong6", verb="wrote", subj="The senator", rec="the constituent who had written every week", thm="a reply",
         rec_given="The constituent who had written every week phoned again today.",
         thm_given="A reply had sat unfinished on the desk.",
         neutral="The district office fielded calls all morning."),
    # --- long theme, short recipient (theme-given context dissociates) ---
    dict(id="tlong1", verb="sent", subj="The lab", rec="the bureau", thm="the samples from the contaminated well site",
         rec_given="The bureau had been awaiting the data for weeks.",
         thm_given="The samples from the contaminated well site were finally sealed.",
         neutral="The testing backlog grew through the long summer."),
    dict(id="tlong2", verb="offered", subj="The studio", rec="the trio", thm="a residency at the coastal arts center",
         rec_given="The trio had toured the region for years.",
         thm_given="A residency at the coastal arts center opened up.",
         neutral="The booking season filled quickly that spring."),
    dict(id="tlong3", verb="showed", subj="The architect", rec="the panel", thm="the revised plans for the riverside development",
         rec_given="The panel had rejected the first proposal outright.",
         thm_given="The revised plans for the riverside development were ready.",
         neutral="The design office worked late through the week."),
    dict(id="tlong4", verb="lent", subj="The library", rec="the academy", thm="the letters of the exiled composer",
         rec_given="The academy had requested rare items for its exhibit.",
         thm_given="The letters of the exiled composer were catalogued.",
         neutral="The archive vault stayed cool through the summer."),
    dict(id="tlong5", verb="sold", subj="The estate", rec="the foundation", thm="the archive of the pioneering photographer",
         rec_given="The foundation had been raising funds all year.",
         thm_given="The archive of the pioneering photographer drew interest.",
         neutral="The auction house prepared its spring catalogue."),
    dict(id="tlong6", verb="mailed", subj="The committee", rec="the league", thm="the findings of the disciplinary review board",
         rec_given="The league had demanded answers for months.",
         thm_given="The findings of the disciplinary review board were complete.",
         neutral="The season opener approached amid the controversy."),
]


def doc_phrase(it):   # double object: verb + recipient + theme
    return f"{it['verb']} {it['rec']} {it['thm']}"


def pd_phrase(it):    # prepositional dative: verb + theme + to + recipient
    return f"{it['verb']} {it['thm']} to {it['rec']}"


CONTEXTS = ["rec_given", "thm_given", "neutral"]
# Which contexts each arm uses. MAIN uses all three (neutral = both-new baseline); CONTROL uses
# the two givenness contexts (its dissociation lives there).
ARM_CONTEXTS = {"main": ["rec_given", "thm_given", "neutral"],
                "control": ["rec_given", "thm_given"]}


def build():
    items = []
    for it in MAIN:
        it = dict(it, arm="main")
        items.append(it)
    for it in CONTROL:
        it = dict(it, arm="control")
        items.append(it)

    trials = []
    for it in items:
        rl, tl = wc(it["rec"]), wc(it["thm"])
        for ctx in ARM_CONTEXTS[it["arm"]]:
            # order counterbalancing: DOC as option A, and DOC as option B
            for doc_is_a in (True, False):
                trials.append({
                    "item": it["id"],
                    "arm": it["arm"],
                    "context_kind": ctx,
                    "context": it[ctx],
                    "subject": it["subj"],
                    "verb": it["verb"],
                    "recipient": it["rec"],
                    "theme": it["thm"],
                    "recipient_len": rl,
                    "theme_len": tl,
                    "doc": f"{it['subj']} {doc_phrase(it)}.",
                    "pd": f"{it['subj']} {pd_phrase(it)}.",
                    "doc_is_a": doc_is_a,
                })
    return items, trials


# ---------------------------------------------------------------------------
# Certification (byte-identical to v1/v2). Prove no surface-only ("shortcut") reader beats
# chance on the information-structure contrast = within-item shift across the two givenness
# contexts. Each shortcut reader returns a DOC-preference in [0,1] from the TEST SENTENCE ONLY
# (lengths, phrasings, A/B order) -- never the context. The contrast for an item is
# pref(DOC|rec_given) - pref(DOC|thm_given); since the test sentence is identical across an
# item's contexts, every shortcut reader yields exactly 0. We assert that here.
# ---------------------------------------------------------------------------

def shortcut_readers():
    return {
        "always_DOC":     lambda t: 1.0,
        "always_PD":      lambda t: 0.0,
        "always_A":       lambda t: 1.0 if t["doc_is_a"] else 0.0,   # picks option A
        "always_B":       lambda t: 0.0 if t["doc_is_a"] else 1.0,   # picks option B
        # end-weight readers: prefer the phrasing whose FIRST np is shorter / longer.
        # DOC puts recipient first; PD puts theme first.
        "shorter_first":  lambda t: 1.0 if t["recipient_len"] < t["theme_len"] else (0.0 if t["recipient_len"] > t["theme_len"] else 0.5),
        "longer_first":   lambda t: 0.0 if t["recipient_len"] < t["theme_len"] else (1.0 if t["recipient_len"] > t["theme_len"] else 0.5),
        # length-proportional: smoothly prefers shorter-first by the length gap
        "length_prop":    lambda t: 1.0 / (1.0 + 2.718281828 ** (0.5 * (t["recipient_len"] - t["theme_len"]))),
        "position_A_bias": lambda t: 0.7 if t["doc_is_a"] else 0.3,
    }


def item_shift(trials, item_id, reader):
    """pref(DOC|rec_given) - pref(DOC|thm_given), averaged over A/B counterbalancing."""
    def mean_pref(ctx):
        vals = [reader(t) for t in trials if t["item"] == item_id and t["context_kind"] == ctx]
        return sum(vals) / len(vals) if vals else None
    a, b = mean_pref("rec_given"), mean_pref("thm_given")
    return a - b


def certify(items, trials):
    report = {"checks": {}, "fail": []}

    # (a) within-pair length variance = 0: DOC and PD of an item use the same NPs.
    a_ok = all(wc(it["rec"]) >= 1 and wc(it["thm"]) >= 1 for it in items)
    # by construction doc/pd reuse rec/thm verbatim; assert the phrasings share tokens
    for it in items:
        toks_doc = set(re.findall(r"[a-z]+", doc_phrase(it).lower()))
        toks_pd = set(re.findall(r"[a-z]+", pd_phrase(it).lower())) - {"to"}
        if toks_doc != toks_pd:
            a_ok = False
            report["fail"].append(f"(a) token mismatch DOC/PD for {it['id']}")
    report["checks"]["(a) within-pair identical NPs / length variance 0"] = a_ok

    # (d) item counts
    n_main = sum(1 for it in items if it["arm"] == "main")
    n_ctrl = sum(1 for it in items if it["arm"] == "control")
    report["checks"]["(d) >=30 main items"] = n_main >= 30
    report["checks"]["(d) neutral both-new baseline present"] = any(
        t["context_kind"] == "neutral" for t in trials)

    # (b) control arm: >=12 items, >=6 where info-structure predicts the LONGER
    # constituent first in the dissociating context.
    clong = [it for it in items if it["arm"] == "control" and wc(it["rec"]) > wc(it["thm"])]
    tlong = [it for it in items if it["arm"] == "control" and wc(it["thm"]) > wc(it["rec"])]
    report["checks"]["(b) >=12 control items"] = n_ctrl >= 12
    report["checks"]["(b) >=6 control items where given=longer (long recipient)"] = len(clong) >= 6
    report["checks"]["(b) >=6 control items where given=longer (long theme)"] = len(tlong) >= 6

    # (c) length distributions matched across given conditions: trivially identical
    # because each item appears in BOTH givenness contexts with the same NPs. Assert it.
    rec_lens_recgiven = sorted(t["recipient_len"] for t in trials if t["context_kind"] == "rec_given")
    rec_lens_thmgiven = sorted(t["recipient_len"] for t in trials if t["context_kind"] == "thm_given")
    thm_lens_recgiven = sorted(t["theme_len"] for t in trials if t["context_kind"] == "rec_given")
    thm_lens_thmgiven = sorted(t["theme_len"] for t in trials if t["context_kind"] == "thm_given")
    report["checks"]["(c) recipient-length dist identical across given conditions"] = rec_lens_recgiven == rec_lens_thmgiven
    report["checks"]["(c) theme-length dist identical across given conditions"] = thm_lens_recgiven == thm_lens_thmgiven

    # NO ANSWER LEAKAGE: the context sentences must not themselves contain a ditransitive
    # DOC/PD phrasing of the item verb (which a model could pattern-match).
    leak = []
    for it in items:
        for ctx in ARM_CONTEXTS[it["arm"]]:
            if re.search(rf"\b{re.escape(it['verb'])}\b", it[ctx].lower()):
                leak.append(f"{it['id']}/{ctx}")
    report["checks"]["no item-verb appears in its own context (no dative-phrasing leak)"] = not leak
    if leak:
        report["fail"].append(f"verb leak in contexts: {leak}")

    # CORE certification: every shortcut reader yields shift = 0 on EVERY item.
    readers = shortcut_readers()
    max_abs_shift = {}
    for name, r in readers.items():
        shifts = [abs(item_shift(trials, it["id"], r)) for it in items]
        max_abs_shift[name] = max(shifts)
    report["max_abs_item_shift_per_shortcut_reader"] = {k: round(v, 6) for k, v in max_abs_shift.items()}
    all_zero = all(v < 1e-9 for v in max_abs_shift.values())
    report["checks"]["no length/position/order shortcut reader produces ANY within-item shift (all shifts = 0)"] = all_zero
    if not all_zero:
        report["fail"].append("a shortcut reader produced a nonzero shift")

    report["ok"] = (not report["fail"]) and all(report["checks"].values())
    return report


def main():
    items, trials = build()
    stim = {
        "design": "dative information-structure POWERED re-run; within-item givenness-context "
                  "shift; graded forced-choice; ratified decisions/resolved/dative-anchor-and-indicator; "
                  "fresh disjoint POWERED item set (no v1/v2 item reused); 100 main + 12 control",
        "n_items": len(items),
        "n_main": sum(1 for it in items if it["arm"] == "main"),
        "n_control": sum(1 for it in items if it["arm"] == "control"),
        "n_trials": len(trials),
        "contexts_per_arm": ARM_CONTEXTS,
        "items": items,
        "trials": trials,
    }
    payload = json.dumps(stim, indent=2, ensure_ascii=False)
    (HERE / "stimuli.json").write_text(payload)
    sha = hashlib.sha256(payload.encode()).hexdigest()

    report = certify(items, trials)
    report["stimuli_sha256"] = sha
    (HERE / "certification.json").write_text(json.dumps(report, indent=2))

    print(f"stimuli.json: {len(items)} items "
          f"({stim['n_main']} main + {stim['n_control']} control), "
          f"{len(trials)} trials")
    print(f"stimuli_sha256: {sha}")
    print("CERTIFICATION:", "PASS" if report["ok"] else "FAIL")
    for k, v in report["checks"].items():
        print(f"  [{'OK' if v else 'XX'}] {k}")
    print("  max |within-item shift| per shortcut reader:",
          report["max_abs_item_shift_per_shortcut_reader"])
    if report["fail"]:
        print("  FAILURES:", report["fail"])


if __name__ == "__main__":
    main()
