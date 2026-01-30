"""
The MIT License (MIT)

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Literal

SortOptions = Literal["DESC", "ASC"]
RaceCatOptions = Literal["official", "custom"]
AttackFiltersOptions = Literal["incoming", "outgoing", "idFilter"]
ReportCatOptions = Literal["mostwanted", "money", "stats", "references", "friendorfoe", "companyfinancials", "truelevel", "stockanalysis", "anonymousbounties", "investment"]

UserListCatOptions = Literal["Friends", "Enemies", "Targets"]
UserPropertiesFiltersOptions = Literal["ownedByUser", "ownedBySpouse"]
UserPrsnlStatsCatOptions = Literal["all", "popular", "attacking", "battle_stats", "jobs", "trading", "jail", "hospital", "finishing_hits", "communication", "crimes", "bounties", "investments", "items", "travel", "drugs", "missions", "racing", "networth", "other", "itemmarketcustomers", "itemmarketsales", "itemmarketrevenue", "itemmarketfees"]
UserPrsnlStatsStatOptions = Literal["attackswon", "attackslost", "attacksdraw", "attacksassisted", "defendswon", "defendslost", "defendsstalemated", "elo", "yourunaway", "theyrunaway", "unarmoredwon", "bestkillstreak", "attackhits", "attackmisses", "attackdamage", "bestdamage", "onehitkills", "attackcriticalhits", "roundsfired", "specialammoused", "hollowammoused", "tracerammoused", "piercingammoused", "incendiaryammoused", "attacksstealthed", "retals", "moneymugged", "largestmug", "itemslooted", "highestbeaten", "respectforfaction", "rankedwarhits", "raidhits", "territoryjoins", "territoryclears", "territorytime", "jobpointsused", "trainsreceived", "marketitemsbought", "auctionswon", "auctionsells", "itemssent", "trades", "cityitemsbought", "pointsbought", "pointssold", "bazaarcustomers", "bazaarsales", "bazaarprofit", "jailed", "peoplebusted", "failedbusts", "peoplebought", "peopleboughtspent", "hospital", "medicalitemsused", "bloodwithdrawn", "reviveskill", "revives", "revivesreceived", "heavyhits", "machinehits", "riflehits", "smghits", "shotgunhits", "pistolhits", "temphits", "piercinghits", "slashinghits", "clubbinghits", "mechanicalhits", "h2hhits", "mailssent", "friendmailssent", "factionmailssent", "companymailssent", "spousemailssent", "classifiedadsplaced", "personalsplaced", "criminaloffensesold", "sellillegalgoods", "theftold", "autotheftcrime", "drugdealscrime", "computercrime", "fraudold", "murdercrime", "othercrime", "organizedcrimes", "bountiesplaced", "totalbountyspent", "bountiescollected", "totalbountyreward", "bountiesreceived", "receivedbountyvalue", "cityfinds", "dumpfinds", "itemsdumped", "booksread", "boostersused", "consumablesused", "candyused", "alcoholused", "energydrinkused", "statenhancersused", "eastereggsfound", "eastereggsused", "virusescoded", "traveltimes", "timespenttraveling", "itemsboughtabroad", "attackswonabroad", "defendslostabroad", "argtravel", "mextravel", "uaetravel", "hawtravel", "japtravel", "uktravel", "satravel", "switravel", "chitravel", "cantravel", "caytravel", "drugsused", "overdosed", "rehabs", "rehabcost", "cantaken", "exttaken", "kettaken", "lsdtaken", "opitaken", "pcptaken", "shrtaken", "spetaken", "victaken", "xantaken", "missionscompleted", "contractscompleted", "dukecontractscompleted", "missioncreditsearned", "racingskill", "racingpointsearned", "racesentered", "raceswon", "networth", "timeplayed", "activestreak", "bestactivestreak", "awards", "refills", "nerverefills", "tokenrefills", "meritsbought", "daysbeendonator", "criminaloffenses", "vandalism", "theft", "counterfeiting", "fraud", "illicitservices", "cybercrime", "extortion", "illegalproduction", "currentkillstreak", "strength", "defense", "speed", "dexterity", "totalstats", "manuallabor", "intelligence", "endurance", "totalworkingstats", "moneyinvested", "investedprofit", "investamount", "banktimeleft", "stockprofits", "stocklosses", "stockfees", "stocknetprofits", "stockpayouts", "networthwallet", "networthvault", "networthbank", "networthcayman", "networthpoints", "networthitems", "networthdisplaycase", "networthbazaar", "networthitemmarket", "networthproperties", "networthstockmarket", "networthauctionhouse", "networthbookie", "networthcompany", "networthenlistedcars", "networthpiggybank", "networthpending", "networthloan", "networthunpaidfees", "huntingskill", "searchforcashskill", "bootleggingskill", "graffitiskill", "shopliftingskill", "pickpocketingskill", "cardskimmingskill", "burglaryskill", "hustlingskill", "disposalskill", "crackingskill", "forgeryskill", "scammingskill", "arsonskill"]

FacCatScopeOptions = Literal["all", "current"]
FacCrimesFiltersOptions = Literal["created_at", "executed_at", "ready_at", "expired_at"]
FacWarfareCatOptions = Literal["ranked", "territory", "raid", "chain", "chainOngoing", "db"]
FacCrimesCatOptions = Literal["all", "recruiting", "planning", "failure", "successful", "expired", "available", "completed"]
FacNewsCatOptions = Literal["main", "attack", "armoryDeposit", "armoryAction", "territoryWar", "rankedWar", "territoryGain", "chain", "crime", "membership", "depositFunds", "giveFunds"]
FacContributorsStatOptions = Literal["medicalitemsused", "criminaloffences", "organisedcrimerespect", "organisedcrimemoney", "organisedcrimesuccess", "organisedcrimefail", "attackswon", "attackslost", "attackschain", "attacksleave", "attacksmug", "attackshosp", "bestchain", "busts", "revives", "jails", "hosps", "medicalitemrecovery", "medicalcooldownused", "gymtrains", "gymstrength", "gymspeed", "gymenergy", "gymdefense", "gymdexterity", "candyused", "alcoholused", "energydrinkused", "drugsused", "drugoverdoses", "rehabs", "caymaninterest", "traveltimes", "traveltime", "hunting", "attacksdamagehits", "attacksdamage", "hosptimegiven", "hosptimereceived", "attacksdamaging", "attacksrunaway", "highestterritories", "territoryrespect", "membersamount", "factionage", "upgradesamount"]

MrktBazaarCatOptions = Literal["Alcohol", "Artifact", "Booster", "Candy", "Car", "Clothing", "Collectible", "Defensive", "Drug", "Energy Drink", "Enhancer", "Flower", "Jewelry", "Material", "Medical", "Melee", "Other", "Plushie", "Primary", "Secondary", "Special", "Supply Pack", "Temporary", "Tool"]
MrktItemBonusOptions = Literal["Any", "Double", "Yellow", "Orange", "Red", "Achilles", "Assassinate", "Backstab", "Berserk", "Bleed", "Blindfire", "Blindside", "Bloodlust", "Burn", "Comeback", "Conserve", "Cripple", "Crusher", "Cupid", "Deadeye", "Deadly", "Demoralize", "Disarm", "Double-edged", "Double Tap", "Emasculate", "Empower", "Eviscerate", "Execute", "Expose", "Finale", "Focus", "Freeze", "Frenzy", "Fury", "Grace", "Hazardous", "Home run", "Irradiate", "Lacerate", "Motivation", "Paralyze", "Parry", "Penetrate", "Plunder", "Poison", "Powerful", "Proficience", "Puncture", "Quicken", "Rage", "Revitalize", "Roshambo", "Shock", "Sleep", "Slow", "Smash", "Smurf", "Specialist", "Spray", "Storage", "Stricken", "Stun", "Suppress", "Sure Shot", "Throttle", "Toxin", "Warlord", "Weaken", "Wind-up", "Wither"]

RaceCarCatOptions = Literal["A", "B", "C", "D", "E"]

TornFactionHofCatOptions = Literal["respect", "chains", "rank"]
TornHofCatOptions = Literal["level", "busts", "rank", "traveltime", "workstats", "networth", "revives", "defends", "offences", "attacks", "awards", "racingwins", "racingpoints", "racingskill"]
TornItemsCatOptions = Literal["All", "Alcohol", "Armor", "Artifact", "Book", "Booster", "Candy", "Car", "Clothing", "Collectible", "Defensive", "Drug", "Energy Drink", "Enhancer", "Flower", "Jewelry", "Material", "Medical", "Melee", "Other", "Plushie", "Primary", "Secondary", "Special", "Supply Pack", "Temporary", "Tool", "Unused", "Weapon"]