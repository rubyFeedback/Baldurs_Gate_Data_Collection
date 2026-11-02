#!/usr/bin/ruby -w
# Encoding: UTF-8
# frozen_string_literal: true
# ============================================================================ #
# http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi
# ============================================================================ #
# Last play-through: November 2026. This is also the final play-through.
# ============================================================================ #
require 'web/autoinclude'
require 'games/constants/constants.rb'

# ============================================================================ #
# === USE_THIS_AS_THE_BACKGROUND_COLOUR
#
# Next run-through should happen via barbarian hammer and flail specialist.
#
# We also need a secondary support warrior focusing on the katana.
# ============================================================================ #
USE_THIS_AS_THE_BACKGROUND_COLOUR = '#d3d2d1;'

english("Baldur's Gate 2") {
created_on '17.10.2023' # Tuesday.
autoextend
ruby_favicon
default_template '

pre {
  font-size: 1.5em;
}

a:link {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

#installation_order_of_the_mods {
  border-bottom: 3px solid '+USE_THIS_AS_THE_BACKGROUND_COLOUR+';
  width: 1500px;
}

#installation_order_of_the_mods:hover {
  background-color: darkgrey;
  border-bottom: 3px solid slategray;
  width: 1500px;
}
'
body_css_style 'background-color: '+USE_THIS_AS_THE_BACKGROUND_COLOUR

require 'games'

# ============================================================================ #
# === primary_link
# ============================================================================ #
def primary_link(
    i
  )
  ntab(
    i.to_s.strip,
    css_class: 'marl2_5em BOLD'
  )
end; alias primary_discussion primary_link # === primary_discussion

# ============================================================================ #
# === finalizer_block
# ============================================================================ #
def finalizer_block(
    name_of_the_mod
  )
  br; version?(name_of_the_mod); br
  the_mod_can_be_downloaded_from(name_of_the_mod)
  visit_the_homepage_of_this_mod_at(name_of_the_mod)
  forum_of_this_mod(name_of_the_mod)
end
    
# ============================================================================ #
# === visit_the_homepage_of_this_mod_at
# ============================================================================ #
def visit_the_homepage_of_this_mod_at(
    name_of_the_mod
  )
  br; e 'Visit the <b>homepage</b> at:'; br
  ntab return_homepage_of_this_mod(name_of_the_mod),
       css_class: 'BOLD marl2_5em'
end

# ============================================================================ #
# === forum_of_this_mod
# ============================================================================ #
def forum_of_this_mod(
    name_of_the_mod
  )
  _ = return_forum_of_this_mod(name_of_the_mod)
  if _ and !_.empty?
    br; e 'Visit the <b>forum</b> of this mod at:'; br
    ntab _,
         css_class: 'BOLD marl2_5em'
  end
end

# ============================================================================ #
# === return_forum_of_this_mod
# ============================================================================ #
def return_forum_of_this_mod(
    name_of_the_mod
  )
  name_of_the_mod = name_of_the_mod.to_sym
  dataset = YAML.load_file(
    ::Games.file_detailed_mod_installation_instructions
  )
  return dataset[name_of_the_mod]['forum'].to_s
end

# ============================================================================ #
# === return_homepage_of_this_mod
# ============================================================================ #
def return_homepage_of_this_mod(
    name_of_the_mod
  )
  name_of_the_mod = name_of_the_mod.to_sym
  dataset = YAML.load_file(
    ::Games.file_detailed_mod_installation_instructions
  )
  homepage = dataset[name_of_the_mod]['github']
  return homepage.to_s
end

# ============================================================================ #
# === the_mod_can_be_downloaded_from
# ============================================================================ #
def the_mod_can_be_downloaded_from(
    name_of_the_mod
  )
  name_of_the_mod = name_of_the_mod.to_sym
  dataset = YAML.load_file(
    ::Games.file_detailed_mod_installation_instructions
  )
  e 'The mod can be <b>downloaded</b> from the following location:'
  br
  # We must fetch the correct entry
  latest_release_at = dataset[name_of_the_mod]['latest_release_at']
  primary_link(latest_release_at)
end; alias can_be_downloaded_from the_mod_can_be_downloaded_from # === can_be_downloaded_from
     alias download_the_mod_from  the_mod_can_be_downloaded_from # === download_the_mod_from
     alias downloadable_from      the_mod_can_be_downloaded_from # === downloadable_from

# ============================================================================ #
# === report_version_of_this_mod
# ============================================================================ #
def report_version_of_this_mod(
    name_of_the_mod
  )
  name_of_the_mod = name_of_the_mod.to_sym
  dataset = YAML.load_file(
    ::Games.file_detailed_mod_installation_instructions
  )
  latest_version = dataset[name_of_the_mod]['latest_version'].to_s
  modified_name = name_of_the_mod.to_s.
                  delete_suffix('_Mod').tr('_',' ').strip.dup
  if modified_name.end_with?('mod')
    modified_name.delete_suffix!('mod')
  end
  e "The latest version of the <b>#{modified_name} "\
    "mod</b> is: <b>#{latest_version}</b>"
end; alias version? report_version_of_this_mod # === version?

# ============================================================================ #
# === BALDURS_GATE_LOGO
# ============================================================================ #
BALDURS_GATE_LOGO = sg('games/baldurs_gate/baldurs_gate2_logo.png',
                    'marr12px round_black2')
main('mar0px pad0px s0_6em') {
  h1 "Baldur's Gate 2",
     'mart1px marb0_5em'
  create_a_sitemap_for_these_links( # sitemap tag
    %i(
      tower_mod
      tales_mod
    )
  )
  ptext {
    e "This website has been created in order to help players - including
    myself, back when I played a lot more - to specifically play through the
    (old) game called <b>Baldur's Gate 2</b> (= <b>BG2</b>).
    This game was originally released on the <b>21.09.2000</b>
    (21st of September, in 2000)."
    br
    e 'The main focus of this document here lies on playing through
    <b>BG2</b> <ud>with</ud> useful <b>mods</b> installed. These mods
    may modify the game experience - and in most cases, <b>enhance</b>
    that experience as well. An initial play-through the original
    (or enhanced) BG2 game, will be referred to as a <b>vanilla</b> run.'
    br
    e 'Take note that this document may contain some spoilers, so it
    is recommended to only read it if you are ok with that or may
    need a bit of help when stuck in a (herein listed) mod.'
    br
    e "After a player has managed to play through the original Baldur's Gate
    2, that player may wish to change some parts of the game, via
    various tweaks or additional encounters. In other words: for
    many such players, the BG2 series can be enhanced via
    mods on subsequent play-throughs."
    br
    e "This document here yields useful information pertaining to
    these objectives. It will cover several different mods for
    Baldur's Gate 2, as well, although not necessarily in
    equal level of detail. In other words: some mods are tested
    more than others. Other mods are barely mentioned here
    at all."
  }
  fancy_spacer
  # ========================================================================== #
  # === Installation Order of BG2 Mods' 
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#installation_order_of_the_mods
  # ========================================================================== #
  h2 'Installation Order of BG2 Mods',
     'rounded_corners pad4px',
     'installation_order_of_the_mods'
  ptext {
    e "The installation order of the mods in BG2 may be important, as some
    mods will only work if installed in the correct installation order."
    br
    e 'For instance, NPC-related mods should typically go <b>after</b>
    quest-mods, simply because some NPCs will detect modded quest content
    and provide (more) interactions with these. You may find a mod NPC
    commenting on a certain mod quest, but only if the NPC can
    logicall follow the quest in the correct installation order.'
    br
    e '<b>Tweak mods</b>, such as the legendary <b>Tweaks Anthology</b>,
    should always come last or close to the end of an installation list,
    as should mods that add new <b>worldmap areas</b>.'
    br
    e 'I keep track of my installation order in the file
    called <b>array_mod_installation_order.yml</b>. You
    can see the latest version of it either in the 
    project (gem) called <b>games</b>, or on github here:'
    br
    primary_link 'https://github.com/rubyFeedback/Baldurs_Gate_Data_Collection/blob/main/array_mod_installation_order.yml'
    br
    e 'In the past I also used to gather specific recommendations
    when the installation of a mod may fail or run into issues. For
    instance, the rather old <b>NPC Strongholds mod</b> can most likely
    be skipped, as the tweaks-mod allows you to play through 
    stronghold mods, even without class restriction. When I typically
    play through BG2, I use the tweaks mod to enable playing
    through all stronghold mods. In this regard, the tweaks mod is,
    in my opinion, better than the old NPC Strongholds mod.'
    br
    e 'Since as of <b>October 2026</b>, though, as I was preparing
    to clean up the document here and bring it up to date, I
    decided that mentioning problematic mods may be outside the
    scope of this document. And some of these mods were improved,
    so old statements I made became outdated. Thus, this 
    subsection here is quite short now, as I will no longer
    discuss bad mods specifically here.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Inns, Pubs and Taverns in BGII
  # ========================================================================== #
  fancy2 "Inns, Pubs and Taverns in BGII"
  ptext {
    e "The <b>Mithrest Inn</b> is an inn that can be found in
    <b>Athkatla's Waukeen's Promenade</b>."
  }
  fancy_spacer
  # ========================================================================== #
  # === Find the Nether Scroll for Edwin
  # ========================================================================== #
  fancy2 'Find the Nether Scroll for Edwin'
  ptext {
    e "This quest is triggered by travelling with <b>Edwin</b> to
    <b>Athkatla's Graveyard District</b>."
    br
    e "Use of the three entrances leading to the lower tombs, enter from
    the pyramid in southwest part of the map, make your way through heaps
    of undeads and spiders then into the lower dungeons from south, the
    <b>nether scroll</b> is obtained from Nevaziah, who did become a lich
    and can be found near his tomb, in the eastern area."
    br
    e "Five days afterwards, Edwin deciphers a part of the scroll and
    will receive a permanent -1 bonus to all saving throws, 50,000
    XP and +20 to his lore."
    br
    e "A couple of days later, another decipher-step of the scroll 
    transforms Edwin into a woman without being able to turn back.
    From this point on, some companions may have a rather interesting
    conversation with Edwina."
    br
    ntab 'https://baldursgate.fandom.com/wiki/Find_the_Nether_Scroll_for_Edwin'
  }
  fancy_spacer
  # ========================================================================== #
  # === Class requirements in BG2
  # ========================================================================== #
  fancy2 'Class requirements in BG2'
  ptext {
    e '<b>Cleric</b>:  Wisdom'
    e '<b>Druid</b>:   Wisdom, Charisma'
    e '<b>Fighter</b>: Strength'
    e '<b>Mage</b>:    Intelligence'
    e '<b>Ranger</b>:  Strength, Dexterity, Wisdom'
    e '<b>Thief</b>:   Dexterity'
  }
  fancy_spacer
  # ========================================================================== #
  # === Efficient play-throughs with mods installed
  # ========================================================================== #
  fancy3 'Efficient play-throughs with mods installed:'
  ptext {
    e 'In the past this subsection focused on giving some advice in how to
    do an efficient run-through, including many mods, based on (primarily)
    power, but also on speed and efficiency.'
    br
    e 'When this document was updated in October 2026, the focus of
    this subsection changed slightly. Rather than making it as
    a step-by-step advice, this paragraph only contains a few
    helpful hints here and there.'
    br
    e 'In the first dungeon of BG2, make sure to
    obtain the <b>Helm of Balduran</b> as well as the
    <b>Girdle of Bluntness</b>. Alternatively you could 
    install the mod <b>Skip Chateau Irenicus</b>
    (see 
    <a href="https://argent77.github.io/A7-SkipChateauIrenicus/index.html">
    here</a>); the items can be found nearby to the
    starting position, after the first dungeon was skipped.'
    br
    e "If you installed Lava's <b>Southern District mod</b> then
    it is recommended to visit it as soon as possible, and
    start to solve the various small quests there; in particular
    the crazy bard may have some items that can be useful,
    such as for a berserker/mage (the katana). Either way,
    doing so should yield some useful items and money
    early on. Consider purchasing at the least one Bag of
    Holding as well - some mods add them, such as the
    Mystigan merchant in the Government district."
    br
    e "In the vanilla variant of BG2, resting in the
    graveyard district does not cost anything, and it is
    easy to reach. No guards will wake up the party -
    though roleplay wise it may be questionable to
    sleep next to the dead, for some characters. If
    you installed the <b>Jazon</b> mod then you can
    find his heart in one of the tombs. Jazon is a
    very useful companion that may simplify some
    battles; at the least in that he may buy some
    time for others in the party to cause more damage."
    br
    e 'Consider obtaining the <b>Daystar sword</b> from the lich
    in the Gate district. You can pick the lock and open the
    chest, then run out, sleep and return to kill the lich
    via Daystar. In fact, it may be possible to make short
    work of most liches with Daystar; Korgan was particular
    useful here for this task.'
    br
    e "In one quest <b>Boo</b> is kidnapped - quite literally
    snatched away from Minsc. If Boo is recovered and the final
    riddle not solved completely, then a small
    figurine will be given to the party for finding
    Boo (and solving two of the three riddles)."
    br
    e 'Obtain the <b>respite</b> from Hexxat early on.'
    br
    e 'Steal the <b>djinni flask</b> in Trademeet, via Hexxat or
    another character. Alternatively, if you are about to finish
    the subquest from the djinni, you could kill the djinni
    outside the tent, rush in and initiate dialogue with the
    leader of the djinni. This will solve the quest and may be
    an option for parties not having a thief character at that
    point in time.'
    br
    e 'Obtain the <b>Horn of Valhalla</b>, to be found in the
    <b>Bridge</b> district. This horn can be upgraded twice
    in total.'
    br
    e 'Obtain the <b>golem</b> early on, to summon it quickly.'
    br
    e 'Obtain the <b>moon dog figurine</b> if a ranger.'
    br
    e 'Buy the mauler club for strength 18. Aerie may benefit
    from it, but also Viconia may benefit from it in the
    early play-time. (Viconia can boost her strength via
    a miracle, so the club may not be that useful in
    later stages of the game.)'
    br
    e 'Obtain the <b>spider figurine item</b> from the graveyard,
    from Paina. The party will also find a summon spider
    spawn scroll there.'
    br
    e "Progress with Dusk's NPC mod (Autumn Fall), in particular to
    obtain the <b>100.000 gold coins</b> as reward. This should then
    make it significantly easier to purchase some high-quality gear,
    such as the robe of Vecna."
  }
  fancy_spacer
  # ========================================================================== #
  # === Can wands be recharged in BG2?
  # ========================================================================== #
  fancy2 "Can wands be recharged in BG2?"
  ptext {
    e 'You may be able to recharge a wand indirectly, if you sell them to
    a shopkeeper, then re-buy them. I have not tested this though.'
    br
    e 'There is also at the least one mod that allows the player to
    re-charge wands; a NPC can be found for this, in the <b>Promenade
    District</b>.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Available companions - Companions in Baldur's Gate 2 (vanilla):
  # ========================================================================== #
  fancy2 "Available companions - Companions in Baldur's Gate 2 (vanilla):"
  ptext {
    e '❤️ <b>Dorn Il-Khan</b>'
    e '❤️ <b>Neera</b>'
    e '❤️ <b>Rasaad yn Bashir</b>'
    br
    e 'Nalia:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Nalia_de%27Arnise'
    br
    e 'A list of all Companions can be found at the following link:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Companions#Baldur.27s_Gate_II_companions'
  }
  fancy_spacer
  # ========================================================================== #
  # === Nalia's main quest
  # ========================================================================== #
  fancy2 "Nalia's main quest"
  ptext {
    e "As part of Nalia's main quest, Lord Farthington Roenall will come
    to the Keep, asking to speak to the player."
    br
    ntab 'https://baldursgate.fandom.com/wiki/Ruling_the_de%27Arnise_Keep_and_Lands'
    br
    e "If the player refuses to see him, then one of his guards will
    enter and make a threat to Gorion's Ward, trying to intimidate
    them into giving up the Keep, before leaving."
    br
    e "If the player sees him, again, Lord Roenall demands that the player
    give the De'Arnise Keep to him. The player may either acquiesce,
    losing their Stronghold permanently, or throw him out (continues the
    Stronghold storyline)."
    br
    e 'If the quest gets corrupted, use the console and enter:'
    br
    cmd 'C:CreateCreature("kprunner")'
  }
  fancy_spacer
  # ========================================================================== #
  # === Jan Jansen (jan tag)
  # ========================================================================== #
  fancy2 'Jan Jansen'
  ptext {
    e "Jan's home (\"<i>Jansen Stead</i>\") can be found in the Athkatla \"Slums\",
    but he is actually (initially) in the Government District, near the
    middle part of it, <b>selling products without permission</b>."
    br
    e "For his quest the party first has to talk to Lady Jysstev in the
    Government District (3300 exp), then talk to the owner of the Sea's
    Bounty Tavern, in the \"<b>Docks</b>\" district."
    br
    e 'Jan has the Flasher master crossbow. He has an icon showing
    under his special abilities that allows him to make X new flasher
    masters per day. This may only work once you are out of ammunition,
    which allows Jan to conjure up some Bruiser Mates.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Throne of Bhaal - Marching Mountains
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Throne of Bhaal - Marching Mountains') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Marching_Mountains'
    ntab 'https://baldursgate.fandom.com/wiki/Yaga-Shura%27s_Lair'
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/ToB/chapter-8/areas/marching-mountains.php'
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/ToB/chapter-8/areas/yaga-shuras-lair-level-1.php'
    br
    e "The Hammer Wardstone is needed to access the
    central western room in Yaga-Shura's Lair."
  }
  fancy_spacer
  # ========================================================================== #
  # === Anomen                                                    (anomen tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Anomen') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e '<b>Anomen Delryn</b> is a lawful neutral male human
    fighter/cleric in BG2. He is a potential companion.'
    br
    e "Anomen's quest relates primarily to his sister's death. After her
    death, Anomen will return home and become <b>lawful good</b> if he qualifies
    as a knight."
    br
    e 'His quest will proceed as follows:'
    br
    e 'After Anomen has been in the party for <b>five days</b>, a servant of the
    Delryn family named Terl will appear and tell Anomen his sister Moira
    Delryn has been murdered.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Useful maps pertaining to Baldur's Gate 2
  # ========================================================================== #
  fancy2 "Useful maps pertaining to Baldur's Gate 2:"
  ptext {
    ntab 'https://mikesrpgcenter.com/bgate2/maps.html'
    ntab 'https://baldursgate.fandom.com/wiki/Baldur%27s_Gate_II:_Shadows_of_Amn'
  }
  fancy_spacer
  # ========================================================================== #
  # === Joluv the merchant                                         (joluv tag)
  # ========================================================================== #
  fancy2 'Joluv the merchant'
  ptext(id: 'joluv') {
    e 'Joluv the merchant'
    br
    e 'Joluv sells items such as the <b>Ninjatō of the Scarlet Brotherhood</b>.'
    br
    e 'For instance, Joluv sells the <b>Ninjatō of the Scarlet Brotherhood</b>:
    a +3 speed sword.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Hexxat%27s_request'
  }
  fancy_spacer
  # ========================================================================== #
  # === "Dragomir's tomb - Hexxat's first quest"
  # ========================================================================== #
  fancy2 "Dragomir's tomb - Hexxat's first quest"
  ptext(id: 'dragomir') {
    e 'To defeat <b>Dragomir</b>, <b>+2 weapons</b> are necessary.'
    br
    e 'Debuffing Dragomir is possible via „<b class="darkblue italic">slow</b>“
    is also useful.'
    br
    e "The main tank of the party, soaking up Dragomir's hits, should
    be kept alive. Also, consider using <b>mirror image</b> on the main
    tank as well as <b>stoneskin</b> before the beginning of the fight."
    br
    ntab 'https://baldursgate.fandom.com/wiki/Dragomir%27s_Tomb'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Claw of the Black Leopard (Hexxat's second quest)
  # ========================================================================== #
  fancy2 "The Claw of the Black Leopard (Hexxat's second quest):"
  ptext {
    e 'Loot the <b>sarcophagi</b> for a Periapt of Life Protection
    and subsequently <b>disarm traps</b> as you venture forth, with the
    key. Then open the door at (x=1900, y=1600).'
    br
    e 'Open any sarcophagi nearby to awake five angry Greater
    Mummies to deal with, the middle sarcophagi (x=2100, y=1420)
    contains <b>The Jade Fang dagger</b>. If Keno died, more ghosts
    will attack the party from all sides along the way.'
    br
    e "Take the east way to find Ki Chin Sang (x=1900, y=820) who holds
    the Key of the Master's Crypt. You can fight him for it. He will
    also hand it over voluntarily if you challenge the master's six
    '<b>most trusted lieutenants</b>' in the hallway to the south. Accept
    the challenge for more xp: after you kill Borok-Tosst, Yi Niu,
    Weimin Min, Ming-hua Dai, Yi Kwon, and Jiang Dai who merge after
    clicking one of their sarcophagi, Ki Chin Sang will walk to you
    and hand over the key."
    br
    e 'Alternatively, the key can be pickpocketed (confirmed with
    Jan @ 125 skill). Your first try will get a few coins.'
    br
    e 'Use the key to open the doors at (x=1350, y=550), disarm two traps
    to meet Nan Kung Chi at (x=2169, y=556), whatever you say will end
    up into a fight, loot his tomb at (x=2047, y=486). Once you possess
    the Claw of the Black Leopard, Hexxat will offer to be back to
    Amn, if you decide to stay a little longer (probably kill some
    ghosts for xp), just to tell her to wait then manual talk to her
    again.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Hexxat%27s_request'
  }
  fancy_spacer
  # ========================================================================== #
  # === Hexxat's third quest (The Tomb of the Prophet Unproved):
  # ========================================================================== #
  fancy2 "Hexxat's third quest (The Tomb of the Prophet Unproved):"
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Hexxat'
    ntab 'https://baldursgate.fandom.com/wiki/Hexxat%27s_request'
    br
    e "Prior to passing through the next door, you can elect to put the
    <b>Piece of Silk</b> in the nearby statue container. It will disable three
    traps tied to the three other items found in the chest near the
    tomb's entrance. Taking back the Piece of Silk will not reactivate
    these traps, so read on to see what they do before making that
    decision."
    br
    e "To solve the \"put your hand in my mouth\" riddle, after
    answering your character's name first, choose the following
    as the solution:"
    br
    cmd '1→2→1→1→1'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Five Flagons Theatre
  # ========================================================================== #
  fancy2 "The Five Flagons Theatre"
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Five_Flagons_Theatre'
    br
    e 'The theatre can be found in the <b>Bridge district</b>, in the
    basement of the <b>Five Flagons Inn</b>.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Balor in Baldur's gate
  # ========================================================================== #
  fancy2 "Balor in Baldur's gate"
  ptext {
    e 'A Balor is a formidable enemy, with magic resistance up
    to 90%.'
    br
    e 'How to fight down such a creature?'
    br
    e '<b>Bolt of Glory</b> ignores magic resistance and deals
    considerable damage against demons.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Balor'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Montaron quest as part of SoA
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Montaron quest as part of SoA") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Find_out_What_Happened_to_Montaron'
    br
    e "<b>Xzar</b>, a companion from Baldur's Gate will approach the party and
    ask you to free <b>Montaron</b>, his fellow companion, from the Harpers."
    br
    e 'Rylock, the doorman in front of the Harper building, is in
    the southwestern part of the "docks" district. He will ask
    the party to kill some evil creatures in Prebek\'s house before
    he will allow you to enter the building.'
    br
    e "Thus, enter Prebek's House near the center of the area
    and defeat Prebek, Sanasha, and the goblins. Return to Rylock
    and then you can enter the building whenever you like."
    br
    e "When you are inside, the Harpers will say that you can't
    enter the floor above without harm if you don't have a
    Harper Amulet. An amulet can be found in one of the
    rooms on the base floors."
    br
    e "Go to the first level floor. With the Harper Amulet
    equiped, the Spectral Harpists won't attack you and your
    party and they will answer some of your questions as
    well. You will find some letters somewhere here
    which suggest that the Harpers have polymorphed Montaron
    into a bird."
    br
    e 'Go to the room with the aviary. Enter the
    aviary and take the "Harper Bird" who was
    once Montaron.'
    br
    e 'Leave the harper building and give the bird to Xzar.
    He will cast a reverse polymorph spell, but the bird
    is actually an assassin from the Harpers named Lucette
    who kills Xzar (you can kill Xzar if you are quick
    enough for 4500xp). The party has been misled.'
    br
    e "Kill Lucette for some additional experience. It
    requires a fast casting Slow or a well set-up thief
    with a backstab as she's out of sight quite quickly.
    She will appear behind Xzar and you may not see
    her if you're not directly facing him. (However
    had, this may mess up the quest.)"
    br
    e 'If you have Jaheira in your group, the "Summoned
    to the Harper Hold" quest will give you access
    again to the Harper Hold.'
    br
    e 'Searching the chests upstairs will reveal his
    body for an additional 20,000 experience (even
    if you previously opened and emptied all of them).'
  }
  fancy_spacer
  # ========================================================================== #
  # === Being captured by Mind Flayers southeast of the drow city
  # ========================================================================== #
  fancy2 'Being captured by Mind Flayers southeast of the drow city'
  ptext {
    e 'It can be quite a challenge for some parties to defeat the
    mind flayers southeast of the drow city in BG2.'
    br
    e 'Should you have problems here, consider any of the following
    strategies - aside, of course, from being as high in level as
    possible before trying to fight the Mind Flayers.'
    br
    e "- Chaotic command, a druid spell, can render the main actor
    invincible against Mind Flayers."
    br
    e '- Make use of the Illithid Serum on one of the machines
    in the southeast corner of the area, in order to free the
    slaves.'
    br
    e '- Click on the large machine in the northeast corner of
    the room four times to obtain Control Circlets, four in
    total. If you should run out of Control Circlets, you
    can also transform into the Slayer to open the doors, as
    the Slayer is an immortal being.'
    br
    e '- Once you have the elder brain blood, after killing
    the big master brain, go to the exit at the northeastern
    part of the map (same as the entrance, quite logically).'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Captured_by_Mind_Flayers'
  }
  fancy_spacer
  # ========================================================================== #
  # === Combat strategies in general, with regards to BG2
  # ========================================================================== #
  fancy2 'Combat strategies in general, with regards to BG2'
  ptext {
    e 'Combat strategies that may work against a demilich,
    in a vanilla run:'
    br
    cmd "→ use <b>Melf's Minute Meteors</b>"
    cmd '→ use <b>a scroll of protection from undead</b>'
    cmd '→ use <b>spell immunity</b> and choose <b>abjuration</b>'
    br
    e 'Note that the <b>freedom spell</b> can reverse <b>imprisonment</b>.
    For this to work it has to be cast in the area where the imprisonment
    happened. The scroll for Freedom can be obtained from the Arcana
    Archives. If the tweaks mod is used then it can also be
    purchased from Ribald.'
    br
    e '<b>Spell Immunity</b>: <b>Abjuration</b> should also help against
    imprisonment. The <b>ring of spell turning</b> can also be used
    here. Shield of the Archons and Cloak of Atonement might help
    as well.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Deck of Many Things - DoMT (and Aesgareth)
  # ========================================================================== #
  fancy2 'Deck of Many Things - DoMT (and Aesgareth)'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Aesgareth'
    ntab 'https://baldursgate.fandom.com/wiki/Deck_of_Many_Things'
    br
    e "Aesgareth (to be found as part of the Watcher's Keep) can simply
    be killed - the Deck of Many Things will be in his corpse, so you
    do not have to gamble if you merely wish to obtain the deck as
    such."
    br
    e 'If you decide to gamble then it seems prudent to first gamble
    for the Spectral Brand. If you get cursed by "<b>Strength</b>",
    then you need to use "remove curse", a level 3 spell.'
    br
    e 'The <b>Star card</b> increases your "main stat" by 1. For
    single-class characters, this is obvious. For duals, I <b>think</b>
    it is the active class, and for multis, I have not yet found a
    correct guide. A fighter/thief will receive a dexterity increase.
    If you are unlucky, you can get a permanent save penalty from
    the Deck as well.'
    br
    e 'First draw:'
    br
    cmd 'bad:  DONJON, EURYALE and RUIN'
    cmd 'good: FLAMES, GEM and JESTER (+50.000 XP)'
  }
  fancy_spacer
  # ========================================================================== #
  # === Lazarus' Missing Spellbook (in the Throne of Bhaal)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Lazarus' Missing Spellbook "\
           "(in the Throne of Bhaal campaign)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Lazarus%27_Missing_Spellbook'
    br
    e '- After talking to <b>Lazarus</b>, speak to "Squip" just north
    of the Arcana Archives. He will tell the party that Hectan paid
    him to steal the book.'
    br
    e '- Next, the party should venture to the "Tankard Tree inn" and
    speak to Hectan. He will admit to taking the book but will only
    give it back if Lazarus gives him a teleportation scroll to
    get out of the town.'
    br
    e "- Go back to the Arcana Archives and speak to Lazarus. Tell
    him what Hectan wants in return for the book. Lazarus gladly
    gives you a teleportation scroll but also warns you that
    Yaga-Shura's mages have raised a magical barrier around
    the city. If Hectan tries to use the scroll, he will
    be killed."
    br
    e "- Go back to the Tankard Tree give the scroll to Hectan
    in return for the spellbook. If you don't warn him, he
    uses the scroll and gets blown up, and the party
    loses a reputation point."
    br
    e '- Return to Lazarus and give him the spellbook. All
    party members receive 5000xp and Lazarus will allow
    you access to his stock.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Free the captive druids
  # ========================================================================== #
  fancy2 'Free the captive druids'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Helping_Irenicus%27s_captive_dryads'
    br
    e 'The party must venture to the "<b>Windspear Hills</b>" after having
    obtained the acorns from the first dungeon in SoA.'
    br
    e 'Once the party has arrived on the Windspear Hills, go to the southeast
    corner of the map there, where the Fairy Queen <b>Vaelasa</b> will be found.'
    br
    e "Give her the acorns and the Dryads in the dungeon will finally be freed.
    The party will receive 32,500 XP upon handing the acorns over and a
    further 9,750 XP upon the Dryads' arrival, for a total of <b>42,250 XP</b>."
  }
  fancy_spacer
  # ========================================================================== #
  # === Jon Irenicus
  # ========================================================================== #
  fancy2 "Jon Irenicus"
  ptext {
    e 'How can Jon Irenicus be defeated in a vanilla run, in the area before
    ToB begins, when Jon transforms into the Slayer?'
    br
    e 'You may be able to run away from Jon and his minions. The demons
    may follow the party while Irenicus stays put - and behind. First, kill
    all the demons, heal and buff your party as well. Then it should be
    easier to fight Irenicus, without being attacked by the demons.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Jon_Irenicus'
    ntab 'https://baldursgate.fandom.com/wiki/Baldur%27s_Gate_II_Chapter_7'
  }
  fancy_spacer
  # ========================================================================== #
  # === Baron Ployer: saving Jaheira from the plague
  # ========================================================================== #
  fancy2 'Baron Ployer: saving Jaheira from the plague'
  ptext {
    ntab 'https://baldursgate2.fandom.com/wiki/Save_Jaheira_from_Baron_Ployer%27s_Curse'
    br
    e '- When you enter the "Sea Bounty" by the Docks, Baron Ployer, a
    former slaver, will confront Jaheira (if she is in the party that
    is). Three mages will appear and cast a curse on Jaheira.'
    br
    e '- Next, enter the government building in the <b>Government District</b>
    and ask "Corneil" about Baron Ployer or the mages. He will not be
    very helpful.'
    br
    e '- Resuming therein, speak to <b>Terrece</b>, who will be standing
    just outside the government building. He will offer to stay out of
    the coming fight for 1000 gold. For 2000 gold he will agree to
    kill Ployer.'
    br
    e "- Enter Baron Ployer's home in the northeast side of the
    \"slums\" area, called the \"Derelict Home\". If you paid Terrece
    2000 gold to kill Ployer, he will appear and do the deed. If
    you paid him 1000 gold to stay out of it, you can either kill
    Ployer by himself, or you can force him to remove Jaheira's
    curse. Jaheira will not honor the deal, however, and will
    kill Ployer. If Terrece was not bribed then the party will
    have to fight Baron Ployer and his three hired mages."
    br
    e "- Take the Lock of Jaheira's hair from Ployer's body and
    Jaheira will feel better. The curse will disappear after
    <b>24 hours</b>."
  }
  fancy_spacer
  # ========================================================================== #
  # === The Wish spell
  # ========================================================================== #
  fancy2 'The Wish spell'
  ptext {
    e 'All useful information pertaining to the Wish spell can be
    found here:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Wish#Wisdom_18.2B'
  }
  fancy_spacer
  # ========================================================================== #
  # === Available Strongholds in Baldur's Gate II:
  # ========================================================================== #
  fancy2 "Available Strongholds in Baldur's Gate II:"
  ptext {
    e 'It is possible for an evil protagonist to acquire the <b>Five
    Flagons Theatre</b> as a stronghold without being a bard. More
    details can be found on the page Running the Five Flagons
    Playhouse.'
    br
    e 'Alternatively one could use the tweaks-mod and enable
    NPC strongholds without class-restrictions.'
    br
    e 'Thief stronghold:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Thieves%27_Guild_Stronghold'
  }
  fancy_spacer
  # ========================================================================== #
  # === How to cure the status "level drained" in BG2?
  # ========================================================================== #
  fancy2 'How to cure the status "level drained" in BG2?'
  ptext {
    e '- In a temple, you can purchase the
    "<i>restoration spell</i>".'
    br
    e '- Alternatively have a cleric cast "lesser restoration", a
    level 4 spell.'
    br
    anm 'Personally I tend to prefer using Viconia here (when
    she is in the party; Aerie would do just fine too), casting
    <b>lesser restoration</b> in the process - this is both
    cheaper and saves some time than going to a temple usually.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Bard class and their songs
  # ========================================================================== #
  fancy2 "The Bard class and their songs"
  ptext {
    e 'The signature ability of the bard is their powerful
    <b>battle song</b>. While actively engaged in singing,
    the party will be fortified against fear, both natural
    and magical.'
    br
    e 'Most Bard songs work within a limited range, roughly
    fireball-sized. In the EE version 2.0+ there is also
    a +3 Luck bonus, as effect of the song.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The child Wellyn quest - a subquest of SoA
  # ========================================================================== #
  fancy_h1('The child Wellyn quest - a subquest of SoA') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'On the graveyard of Athkatla one can meet the ghost
    of Wellyn. He is missing his teddy bear.'
    br
    e 'Llynis - who stole the teddy bear - has a room at the
    "<b>Copper Coronet</b>", in the "Athkatla Slums" district.'
    br
    e "Go confront Llynis and ask for the teddy bear. Depending on
    the dialogue options chosen, Llynis will either attack
    the party, or hand over the bear peacefully. Either way,
    you might as well loot his room when Llynis is gone."
    br
    e 'Now return to the graveyard in the evening or at night and
    speak to Wellyn again. He will be so happy and will finally
    be able to rest in peace. The party receives <b>15,500 XP</b>
    as reward.'
    br
    e "Return to Wellyn's grave in the morning and speak to his
    parents, who are usually mourning nearby. His parents will be
    overjoyed that their little boy can finally sleep peacefully.
    The party will get an additional 5,000 XP."
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Put_the_Spirit_of_the_Child_Wellyn_to_Rest'
  }
  fancy_spacer
  # ========================================================================== #
  # === Deirex's Tower (in the drow city)
  # ========================================================================== #
  fancy2 "Deirex's Tower (in the drow city)"
  ptext {
    e "Deirex's Tower is a two-story tower located in Ust Natha and is
    the home of Deirex the Lich. You must enter the tower if you want
    to retrieve the Jae'llat Wardstone from Deirex. Deirex will drop
    Lich's Tooth, which will allow access to Deirex's Cave, via the
    stairs on the outside of the tower."
    br
    e "Now head down to Deirex's Tower, Deirex the Lich is right
    there, and you are soon teleported to Jarlaxle's Pocket
    Dimension. The resident tells you that he wants the gem
    Deirex processes, he gives you one day to accomplish this
    before teleporting you back to Deirex's Tower."
    br
    e "Fight with Deirex, who is capable of casting Time
    Stop, Abi-Dalzim's Horrid Wilting and puts up as
    a normal lich battle (22,000 XP). Be sure to search
    his body for the Lich's Tooth and the Jae'llat
    Wardstone. Also search this place for treasures
    (some of which are trapped):"
    br
    e '- Glitterdust scroll, Wizard Eye scroll, Deafness
    scroll, Contagion scroll, Remove Magic scroll,
    Limited Wish scroll and more.'
    e '- Leather Armor of the Viper +5'
    e "- Jarlaxle's Gems"
    br
    e "Taking Jarlaxle's Gems will instantly teleport you
    back to the pocket dimension. Jarlaxle takes the Gems.
    Accept his thanks (2,500 Gold Piece or kill him
    (14,000 XP + 12,000 XP). In any case you will be
    teleported back to the tower."
  }
  fancy_spacer
  # ========================================================================== #
  # === The Tweaks Anthology mod                                  (Tweaks tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#tweaks
  # ========================================================================== #
  name_of_the_mod = :Tweaks_Anthology_Mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Tweaks Anthology mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'tweaks') {
    report_version_of_this_mod(name_of_the_mod)
    br
    e 'The <b>Tweaks Anthology mod</b> is a compilation of fixes,
    cosmetic changes, and tweaks that will run on every Infinity
    Engine game.'
    br
    e 'Each component of this mod can be <b>installed separately</b>, so
    the player can pick and choose only which ones they wish to install.'
    br
    e 'The mod will add <b>Bags of Holding</b> to <b>Ribald</b>. Such
    containers can also be made bottom-less, as part of this mod,
    which is quite convenient.'
    br
    e 'The tweaks mod can also add <b>Universal Clubs</b>, which
    allows <b>mages</b> to wield clubs and gain a proficiency
    point in clubs.'
    br
    e "Not all tweaks are necessarily great, though - for instance,
    the <b>Use BG Walking Speeds</b> should probably not be used,
    whereas the <b>Speed up de'Arnise Keep Stronghold Quest</b> 
    might be useful on subsequent play-throughs and could be
    enabled."
    br
    e 'The mod can also extend the experience point caps, via
    <b>Change Experience Point Cap</b>. This one is quite
    useful.'
    br
    the_mod_can_be_downloaded_from(name_of_the_mod)
    visit_the_homepage_of_this_mod_at(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Trials of the Luremaster mod                   (trials tag, trial tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#trials_of_the_luremaster_mod
  # ========================================================================== #
  name_of_the_mod = :Trials_of_the_Luremaster_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Trials of the Luremaster mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'trials_of_the_luremaster_mod') {
    e "The Trials of the Luremaster quest begins by talking to the
    halfling called <b>Hobart Stubbletoes</b>, who can be found
    either in the <b>Umar Hills Inn</b> (SoA), <b>Amkethran Inn</b> (ToB)
    or in the southeastern area of the <b>Coalition Camp</b> (SoD)."
    br
    e 'In the course of the adventure you have the opportunity to explore
    a <b>haunted castle</b>, test your mettle in challenging combat and
    lift an ancient curse. In addition to the original adventure, the mod
    provides various story and combat improvements as well as interactions
    from all of the Bioware and Beamdog NPCs. Some interesting
    items may also be purchased from the halfling.'
    br
    e 'The <b>Luremaster</b> will give at the least one riddle.
    The correct answer to that riddle is <b>Wind</b>.'
    br
    e 'In the large <b>crypt</b>, the party may eventually
    find <b>four coffins</b>. Place the four gathered Tales
    into the following coffins:'
    br
    cmd '<b>Western coffin</b>:  Tale of Sir Erris   # two-handed axe +2'
    cmd '<b>Southern coffin</b>: Tale of Sir Giles   # mace +1'
    cmd '<b>Eastern coffin</b>:  Tale of Sir Zierkki # spear +1'
    cmd '<b>Last coffin</b>:     Tale of Sir Geddian'
    br # === The flawed gems
    e 'For the larger area underneath you will need various gems and
    pearls that can be found in different chests, in particular:'
    br; reset_the_counter
    counter '<b>Flawed Moonbar Gem</b> # can be found at the Dire Bears Area','marl2_5em'
    counter '<b>Flawed Skydrop Gem</b> # found in the Minotaur Area','marl2_5em'
    counter '<b>Flawed Pearl</b> # can be found in the Harpy Area, aka
    "Cave of the Stones"','marl2_5em'
    counter '<b>Flawed Emerald</b> # can be found in the Spider Area','marl2_5em'
    counter '<b>Flawed Fire Agate Gem</b> # can be found in the Jackal Area','marl2_5em'
    br
    e 'These must then be converted into <b>flawless gems</b>, before they
    can be placed in the large circle containing the five slots. This step
    can be done in the <b>Chest of Seasons</b>, which is at the path in
    the <b>southwestern</b> area, at x: 730, y: 1470, <b>within</b> the
    <b>Minotaur Area</b>. The converted gems can then be found in
    each of the five altars.'
    br
    e 'Once the flawless gems have been obtained, they have to be put into
    the correct slot. "Heaven above" refers to the Star Sapphire. South
    to this the Flawless Waterstar Gem has to be put.'
    br
    e 'After defeating the <b>Luremaster</b>, a ring can be found, which
    has to be equipped and then used, in order to escape from the
    haunted castle.'
    br
    e 'Discussion about the mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/73701/mod-trials-of-the-luremaster-for-bg2-ee'
    br
    e 'A walkthrough of this mod can be seen here:' # === The walkthrough
    br
    primary_link 'https://gamefaqs.gamespot.com/pc/430803-icewind-dale-heart-of-winter/faqs/10898'
    br
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Skip chateau Irenicus mod
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#skip_chateau_irenicus_mod
  # ========================================================================== #
  name_of_the_mod = :Skip_Chateau_Irenicus_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Skip chateau Irenicus mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Skip chateau Irenicus mod allows the player to skip the very first
    dungeon in BG2-SoA, without losing equipment and items.'
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Reunion - a Mod with Nalia                               (reunion tag)
  # ========================================================================== #
  name_of_the_mod = :The_Reunion_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Reunion") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'In the <b>Reunion mod</b>, you are the Child of Bhaal, and your journey
    is nearly complete. But after you arrive in Amkethran, Nalia approaches you
    with distressing news. Her castle is once again under attack, this time
    by demons, and her people are in clear danger.'
    finalizer_block(name_of_the_mod)
  }
  # ========================================================================== #
  # === The Yvette NPC mod                                        (yvette tag)
  # ========================================================================== #
  fancy_spacer
  name_of_the_mod = :The_Yvette_NPC_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Yvette NPC mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Yvette (the NPC) can be "found" when one purchases a strange
    parchment on the Promenade. It displays the portrait of young
    lady.'
    br
    e 'Help her remember who she really is, let her experience
    adventures, let her stay by your side - that may guide you
    to something more than friendship, something Sune herself
    would bless.'
    br
    e 'The romance will only start if the main actor is male, and
    an elf, human, half-elf, tiefling and not evil in alignment.'
    br
    e 'The Yvette mod may have an issue in that Yvette does not spawn
    after the banter; at the least this used to be the case when
    I played this mod in 2024 or so.'
    br
    e 'Discussion about this mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/38948/mod-yvette-romance'
    finalizer_block(name_of_the_mod)
  br;}
  # ========================================================================== #
  # === BG2 EE Romantic Encounter mod                           (romantic tag)
  # ========================================================================== #
  fancy_spacer
  name_of_the_mod = :BG2_EE_Romantic_Encounters
  fancy_h1("#{BALDURS_GATE_LOGO} BG2 EE Romantic Encounter mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>romantic encounter mod</b> adds a few more options for
    romance: flirting and some more intense, romance-specific
    options.'
    br
    e 'This mod also adds a few items, such as "Mira\'s Special
    Stock", which yields a boost to constitution.'
    br
    e 'A more thorough explanation of the content of this mod
    can be seen here:'
    br
    primary_link 'https://gibberlings3.github.io/Documentation/readmes/Readme-RE.txt'
    br
    e 'This mod comes with various NPC encounters - in total about
    54 events, as can be seen from the above link. These NPC encounters
    are as follows:'
    br
    le2 '- <b>Aimi</b>, a young girl, which can be found in the Trademeet
    Inn, after the PC was declared a Hero of Trademeet. Yes, she only
    likes heroes.'
    br
    le2 "- Chandra can be found in the Den of the Seven Vales, which is an
    inn in the Waukeen's Promenade. (Make sure to give her a kiss in
    the dialoge options.)"
    br
    le2 "- Sheri the Bardess can be found in Athkatla, at the Promenade's
    Mithrest Inn, near the piano."
    br
    le2 '- Another encounter happens with <b>Rebecca the Gypsy</b> in Trademeet.
    She can tell you your fortune after all.'
    br
    le2 "- Mira, a merchant in Waukeen's Promenade, has some special wares
    for you if you are interested."
    br
    le2 '- Trademeet with Guildmistress <b>Busya</b> may be another opportunity.'
    br
    le2 '- <b>Weathermistress Ada</b> has a few things to try out.'
    br
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === The Tangled Oak Isle mod                                 (tangled tag)
  # ========================================================================== #
  name_of_the_mod = :The_tangled_oak_isle_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Tangled Oak Isle mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'tangled_oak_isle') {
    embed_remote_image 'https://i.imgur.com/HxSlZPf.png',
                       'round_black3 mar0_5em mars3em',
                       'drag_bg2_mod_tangled_oak_isle'
    e 'The Tangled Oak Isle mod adds another district to <b>Athkatla</b>: an island
    in the sea just outside the city wall.'
    br
    e 'The isle has:'
    br
    le '- an inn','mars2em BOLD'
    le '- a tavern','mars2em BOLD'
    le '- a temple','mars2em BOLD'
    le '- a lighthouse, and more.','mars2em BOLD'
    br
    e "Besides various mini-quests, you can investigate the sickness that has befallen
    the Tangled Oak (the isle's namesake), which leads to additional new maps."
    br
    e 'The mod still works fine as of <b>2023</b>.'
    br
    e 'Discussion about the mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/79831/mod-tangled-oak-isle'
    br
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Southern Edge mod
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/southern-edge/
  # ========================================================================== #
  name_of_the_mod = :Southern_Edge_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Southern Edge mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'southern edge') {
    e 'Southern Edge mod is about a parasite.'
    br
    e 'The <b>four parasites parts</b> can be found as follows:'
    br; reset_the_counter
    counter 'chest in the house with breached door (top of the map)','marl2em BOLD'
    counter 'Weid play of the angry Bard (2nd floor of Inside the Wall)','marl2em BOLD'
    counter 'Mr. Cat: can be found in the southern part of the map','marl2em BOLD'
    counter 'Girl in one of the tents, bring her a nice toy to get it',
    'marl2em BOLD'
    br
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Crucible                                                (crucible tag)
  # ========================================================================== #
  name_of_the_mod = :The_Crucible_Mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Crucible mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'crucible') {
    e 'The <b>Crucible mod</b> features a continuation of the story once the player
    closes their pocket plane in ToB.'
    br
    e 'A discussion about the Crucible mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/88017/new-mod-teaser-announcement-crucible'
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Assassinations                                    (Assassinations tag)
  # ========================================================================== #
  name_of_the_mod = :Assassinations_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Assassinations mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'assassinations') {
    e 'The Assassinations mod adds a single quest-line that starts
    in <b>chapter 2</b>.'
    br
    e 'The quest begins by talking to Bernard in the Copper Coronet (in
    the Slums district of Athkatla) – he says that he has received a
    letter for you. (Requires: non-Paladin CHARNAME with a
    reputation below 17.)'
    br
    e '<b>Nevier Costa</b> can be found in the slums, at the
    bottom right corner of the map.'
    br
    e 'Discussion in the forum about the Assassinations mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/75935/mod-spotlight-assassinations/p1'
    br
    e 'A full explanation of the mod - including a walk-through - can be
    found here:'
    br
    primary_link 'https://mods.pocketplane.net/kulyok/Readme-Assassinations.txt'
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Aura the NPC                                                (aura tag)
  # ========================================================================== #
  name_of_the_mod = :Aura_the_artificer_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Aura the cute artificer-NPC") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'aura') {
    e 'Aura will have the automaton at level 9 and above. Or just
    pick up the automaton from her room.'
    br
    e 'Her quest has to do with a substance called <b>Titan</b>.'
    br
    e 'She is quite fragile, so ideally keep her in backrow.'
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === The Dreadful Tales: The Bloodied Stings of Barovia - a dark Ravenloft adventure (Barovia tag)
  #
  # Barovia tag. The Ravenloft mod.
  # ========================================================================== #
  name_of_the_mod = :The_Dreadful_Tales_The_Bloodied_Stings_of_Barovia
  fancy_h1("#{BALDURS_GATE_LOGO} The Dreadful Tales: The Bloodied "\
           "Stings of Barovia - a dark Ravenloft adventure") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'barovia') {
    e 'The Dreadful Tales: The Bloodied Stings of Barovia - a dark Ravenloft
    adventure, created by <b>Lava</b>.'
    br
    e 'In the later part of the mod, there is the handkerchief and a special
    bowl - a ritual bowl - somewhere in the mansion. There is also a hidden
    door behind one of the barrels. The altar can be found in the cellar.
    Both items - the handkerchief and the bowl - should be put on the
    altar, which will trigger the next scene.'
    br
    e 'To leave Barovia, one has to find a letter in a chest. This letter will
    show which are the five items necessary in order to open the portal that
    allows the party to leave Barovia again.'
    br
    e 'My favorite one is the rose-covered tree. But there is also
    a ghost of a child near the bonfire or the quest related to
    the pile of bones. That ghost is actually an additional fighter.'
    br
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === The ink gallery                                              (ink tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#the_ink_gallery
  # ========================================================================== #
  name_of_the_mod = :The_Ink_gallery_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The ink gallery") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'the_ink_gallery', style: 'margin-bottom: 0px') {
    e 'The rewards are as follows, somewhat arbitrarily
    ranked by me from <b>best</b> to <b>worst</b>:'
    table2('pretty_table default_table marl2em marb1px','','',
      '<b>(1)</b> The Birth of the Fury','The Enrage ability 
       (very useful for Drizzt)',
      '<b>(2)</b> The Deathly Groans','+3% magic resistance',
      '<b>(3)</b> The Dance of the Swords','+5% slashing resistance',
      '<b>(4)</b> Eight-legged Strider','Save versus poison +1',
      '<b>(5)</b> The War below','+5% fire resistance',
      '<b>(6)</b> The Grasp of the Glabrezu','+5 Lore',
      '<b>(7)</b> Tale of the Dead Eye','+1 to saving throw versus spells',
      '<b>(8)</b> The Story of the Three Sisters','+5% cold resistance as a
           permanent benefit; as souvenir the <b>Three Moon Phases</b>
           +3 <b>shield</b> (which will increase the AC by +4).',
      '<b>(9)</b> Of Seed and Fire','+2 hp; the souvenir
       is the <b>Fire Rown ring</b>, which increases AC by +2
       and Saving Throws +2. Also, Fire Seed can be used
       on a daily basis.',
      '<b>(10)</b> The Waves of flesheaters','+5% acid resistance',
      '<b>(11)</b> The Light in the Snow','+5% crushing damage resistance',
      '<b>(12)</b> The Three Thirsty Rascals','+5% piercing damage resistance'
    )
    finalizer_block(name_of_the_mod)
  }
  fancy_spacer
  # ========================================================================== #
  # === Tower of Deception                                     (Deception tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#tower_of_deception
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#tower_mod
  # ========================================================================== #
  name_of_the_mod = :Tower_of_Deception_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Tower of Deception") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'tower_of_deception', style: 'margin-bottom: 0px') {
    e 'The <b>Tower of Deception</b> is a rather difficult side quest,
    unless properly prepared for it.', id: 'tower_mod'
    br
    e 'To defeat the (snake-like looking) Guardian protecting the
    Astral Shard, make sure that it does not have Stoneskin or
    Protection from Magical weapons active. Alternatively - or
    in addition to that - Ruby Ray of Reversal and Lower Resistance
    spells could be used against that Guardian, plus spell
    sequencer or the  Greater Malison spell. Even then magic
    missile will do the trick.'
    br
    e 'In order to then defeat the Astral Shard, guarded by the Guardian,
    one can use a fireball or one of those exploding potions to damage
    it. A single exploding potion should suffice. Alternatively you can
    pick up fireball scrolls in the tower.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === A7-GolemConstruction                           (golem tag, golems tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#golems
  # ========================================================================== #
  name_of_the_mod = :The_golem_construction_mod
  fancy_h1("#{BALDURS_GATE_LOGO} A7-GolemConstruction") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'golems', style: 'margin-bottom: 0px') {
    embed_remote_image 'https://i.imgur.com/1ykgldN.jpg',
                       'round_black3 mar0_5em mars3em',
                       'drag_bg2_mod_golems'; drag_for :drag_bg2_mod_golems
    br
    e 'The <b>A7-GolemConstruction mod</b> adds various
    <b>golem building manuals</b>.'
    br
    e 'The <b>available golems</b> will be:'
    br
    lem2 '<b>Flesh Golems</b> in lesser, regular, greater and perfect variants.'
    lem2 '<b>Clay Golems</b> in lesser, regular, greater and perfect variants.'
    lem2 '<b>Stone Golems</b> in lesser, regular, greater and perfect variants.'
    lem2 '<b>Iron Golems</b> in lesser, regular, greater and perfect variants.'
    lem2 '<b>Mithral Golems</b> in lesser, regular, greater and perfect variants.'
    lem2 '<b>Adamantite Golems</b> in lesser, regular, greater and perfect variants.'
    br
    e "In <b>Shadows of Amn</b> the Planar Sphere and Jermien's Home in Imnesville are
    suitable places for building golems."
    br
    e "The Wizard's Library on the second floor of Watcher's Keep can be used as
    well."
    br
    e "In order to construct a <b>Perfect Flesh Golem</b>, the <b>Deep Bloodstone
    Gem</b> is required. A regular bloodstone gem can be found in, for instance,
    <b>Valygar's Home</b>."
    br # === Perfect Clay Golem
    e 'In order to construct a <b>Perfect Clay Golem</b>, four blocks of clay,
    one scroll of Haste and one bag of Enchanted Coral Powder are necessary.
    Without the enchanted coral powder one can only build a <b>Greater Clay
    Golem</b>.' # I did this first successfully on the June 2025.
    br # === Perfect Adamantite Golems
    e 'Adamantite Golems require adamantine, as well as a thief with the
    <b>"Use Any Item"</b> ability.'
    br
    e 'These golems regenerate hitpoints per turn, and
    are immune to non-magical, +1 and +2 weapons.'
    br
    e 'Furthermore they can cast the <b>"Trample"</b> ability
    on enemies of normal size or smaller, which does
    8d10+30 crushing damage and will also stun the
    target for one round (save vs. death at -4 penalty
    for half damage and avoid stun).'
    br
    e 'The <b>Greater Adamantite Golem</b> requires eight bars of
    adamantine. Its attributes are:'
    br
    cmd 'STR: 24'
    cmd 'HP: 110'
    cmd 'AC: 0'
    cmd 'THAC0: 0'
    cmd 'APR: 3/2'
    cmd 'Saves: 1/3/2/2/4'
    br
    e 'The Perfect Adamantite Golem requires one <b>drop of
    blood</b> from a Solar or Fallen Solar.'
    br
    finalizer_block(name_of_the_mod)
    br
    e 'Detailed information about the golems can be found here:'
    br
    ntab 'https://raw.githubusercontent.com/Argent77/A7-GolemConstruction/refs/heads/devel/A7-GolemConstruction/readme/golem_information.txt'
  }
  fancy_spacer
  # ========================================================================== #
  # === Region of Terror                              (region tag, Drizzt tag)
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#region_of_terror
  # ========================================================================== #
  name_of_the_mod = :Region_of_Terror_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Region of Terror mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'region_of_terror', style: 'margin-bottom: 0px') {
    e 'The <b>Region of Terror mod</b> is a mod about <b>Drizzt do Urden</b>.'
    br
    e '<b>Drizzt</b> can be found on the <b>second level of the very first
    dungeoon</b>.'
    br
    e 'The mod also adds the city <b>Arlax</b>. There are <b>three sewer entrances</b>
    in Arlax; one is situated right after the main <b>northern gate</b>.'
    br
    e "Furthermore, the mod contains a component where the party has to
    travel to <b>Gaidan's Castle</b>."
    br # The village of Westchar:
    e 'The village of <b>Westchar</b> is added by this mod. The house in
    the southeastern part of the village can be opened by a key
    given by the drow <b>Alora</b>, which can be found in Umar hills near
    the cave - but first you have to find Regis. The house in
    Westchar then allows the party to travel to the <b>Realm of the
    Gragha</b>.'
    br # === Regis
    e "Regis can be found in Montezuma's cave. Once he is freed he will give the
    next clue for the main quest, which is to visit the Umar Hills. Both Drizzt
    and the main character have to be close to Regis, in order for Regis to
    begin to talk."
    br
    e "One side quest of this mod makes use of <b>Randall</b>, a lethargic mage.
    five days after Randall has joined the party, when the protagonist has
    more than 250.000 XP, a mage labeled 'Necromancer' approaches the party
    while traveling outdoors. Razor can not be defeated; instead, when his
    hit points are reduced to 1, he will initiate a new dialog and reveals
    that he and his accomplice Marcus murdered Randall's real father. But
    before Razor can narrate the whole story, he perishes."
    br
    e '<b>The Quest for the Eye of a God</b> can be started by having
    Pip forge an item, by making use of a <b>Rock of a Glowing Star</b>.
    This can be done by, for instance, giving Pip a <b>chain
    mail armor</b>.'
    br
    e 'In one city a demi-lich can be found. Killing him will yield a
    <b>mithril chainmail</b> (which would be quite useful
    for Drizzt), and a tooth of the demilich, granting immunity
    against normal weapons.'
    br
    # ======================================================================== #
    #
    # ======================================================================== #
    ptext {
      e 'Solution for the <b>Test of Intelligence</b>:'
      br
      cmd '3,2,2,4,5'
    }
    # ======================================================================== #
    # === Brynnlaw
    # ======================================================================== #
    fancy3 'Brynnlaw'
    ptext {
      e "Shadows of Amn chapter 4 brings the party to Brynnlaw. Here
      Brother Martin has to be found outdoors near the Pirate Lord's
      Home, and when you are ready, ask him to teleport you to
      Spirit Soaring."
      br
      e 'This quest has to be solved in this chapter, in order to
      complete the Region of Terror mod.'
    }
    # ======================================================================== #
    # === City of the Gragha                                      (Gragha tag)
    # ======================================================================== #
    fancy3 'City of the Gragha'
    ptext {
      e 'The answer to the riddle, as text, is kind of the order
      that is shown, as-is. So simply type "1" to select the
      first answer - this should suffice for <b>all</b>
      subsequent answers.'
    }
    # ======================================================================== #
    # === Bremen                                                  (Bremen tag)
    # ======================================================================== #
    fancy3 'Bremen'
    ptext {
      e 'A walkthrough for Bremen can be read here:'
      br
      ntab 'https://baldursgate.fandom.com/wiki/Region_of_Terror_walkthrough/Bremen'
      br
      e 'The Ice Temple can be found as part of Bremen - see the next
      subsection.'
    }
    # ======================================================================== #
    # === Ice Temple                                          (Ice Temple tag)
    # ======================================================================== #
    fancy3 'Ice Temple'
    ptext {
      e 'In order to open the talking door, the "Mysterious Scroll"
      from the hermit is required.'
      br
      e "If instead you wish to solve the monk's riddle, you must place
      the gems in the following order, from bottom left:"
      br
      e 'yellow, violet, dark red, light red, dark green, light
      blue (= sapphire), light green, dark blue, black, white.'
      br
      e 'Abbot Baurmin can be found on the second level, in the 
      most southern room (called Sanctuary room).'
      br
      ntab 'https://baldursgate.fandom.com/wiki/Region_of_Terror_walkthrough/Ice_Temple'
    }
    # ======================================================================== #
    # === Eye of a God Cave
    # ======================================================================== #
    fancy3 'Eye of a God Cave'
    ptext {
      e 'To start The Quest for the Eye of a God, talk to
      Pip Grayfoot and let him forge something
      using a Rock of a Glowing Star.'
      br
      e 'This causes Pip to "graduate" from his apprenticeship, and
      set up his own smithy nearby.'
      br
      e 'Next, talk to Pip at his new smithy, and ask him if there
      are other forging gems beside the ones in his recipe book.
      He tells you about a legendary gem called "The Eye of A
      God", and marks a cave near Athkatla on your worldmap.'
      br
      e 'Four tablets have to be gathered on the first level. Once
      they have been collected they should be shown to the guardian,
      who resides at the bottom-left area.'
      br
      e 'Inside the cave, Lord Garrax can be found. How to defeat him?'
      br
      e '- Have a Wish prepared.'
      e '- Be wary of the spellcasters, for they can gate in new demons.'
      e '- Killing the summons is useful, as they do not replenish
      eventually.'  
    }
    br
    e 'The <b>available quests</b> in this mod are:'
    br; reset_the_counter
    cmd_counter("A Ghost")
    cmd_counter("Alissa's Abilities (Alissa)")
    cmd_counter("Arena fights")
    cmd_counter("Book Collector")
    cmd_counter "Castles at War"
    cmd_counter "Clob's Son Missing"
    cmd_counter "Demi-Lich in the Basement, in Arlax"
    cmd_counter "Demons in the Spirit Soaring (Drizzt)"
    cmd_counter "Depressed People"
    cmd_counter "Dragons' Sanctuary"
    cmd_counter "Eleana and the Scroll"
    cmd_counter "Escaped Prisoner"
    cmd_counter "Farmer in Need of Aid"
    cmd_counter "Find Garem's Ring from the Sewers"
    cmd_counter "Find Maralda's Scroll"
    cmd_counter "Giants Took Rob's Wife"
    cmd_counter "Haman Encounter"
    cmd_counter "Help Drizzt Finding His Friends (Drizzt)"
    cmd_counter "Help the Thief in Arlax"
    cmd_counter "Helping the Farmers"
    cmd_counter "Hunting"
    cmd_counter "Journey to the North"
    cmd_counter "Kill the Cyclop Leader"
    cmd_counter "Lamorine's Brother"
    cmd_counter "Locked Door"
    cmd_counter "Molly's Stolen Necklace"
    cmd_counter "Necromancer After Randall (Randall)"
    cmd_counter "Pickpocketer Colbert"
    cmd_counter "Revenge on the Behalf of Hands"
    cmd_counter "RoT Assassinations"
    cmd_counter "Save the Children"
    cmd_counter "The Hermit"
    cmd_counter "The Hunters"
    cmd_counter "The Lost Gragha"
    cmd_counter "The Quest for the Eye of a God"
    cmd_counter "The Strange Talking Armor"
    cmd_counter "Thief at Kindast Store"
    cmd_counter "Weapons Missing"
    cmd_counter "Westchar in Troubles"
    cmd_counter "What is Matthew up to?"
    cmd_counter "Wulfgar's Wife (Wulfgar)"
    finalizer_block(name_of_the_mod)
    br
    e 'A walkthrough can be found at the following link:'
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Region_of_Terror_walkthrough'
    primary_link 'https://baldursgate.fandom.com/wiki/Region_of_Terror_walkthrough/Main_quest'
  }
  fancy_spacer
  # ========================================================================== #
  # === Innershade mod                                        (Innershade tag)
  # ========================================================================== #
  name_of_the_mod = :The_Innershade_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Innershade mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'innershade_mod', style: 'margin-bottom: 0px') {
    e 'This subsection mentions a few noteworthy
    points about the <b>Innershade mod</b>. First: Innershade
    can be found close to the large forest area southeast
    of Amn.'
    br
    e 'The <b>angry bard</b> in Innershade can teach new
    skills to other bards.'
    br
    e 'When <b>The Dream</b> is finally defeated, a +3 long sword may
    be the reward, or a staff.'
    br
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === I SHALL NEVER FORGET                                      (forget tag)
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/eilistraees-song/
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#i_shall_never_forget
  # ========================================================================== #
  name_of_the_mod = :I_shall_never_forget_mod
  fancy_h1("#{BALDURS_GATE_LOGO} I SHALL NEVER FORGET") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'i_shall_never_forget', style: 'margin-bottom: 0px') {
    e "This Baldur’s Gate 2 mod allows you to work with <b>Orion</b> – a
    mage who has lost the sense of his life."
    br
    e 'The quest begins in the <b>Government District</b>. Look for a
    new exit called "<b>2nd Floor Observatory</b>".'
    br
    e "Another new area is the <b>The Temple of Sune</b>, located in
    Waukeen's Promenade."
    br
    e 'To find <b>The Incomplete</b>, as part of the main quest, one
    has to go to the <b>sewers</b> under the Temple District. In
    the southern part, a new exit can be found, leading to the
    hideout of <b>The Incomplete</b>.'
    finalizer_block(name_of_the_mod)
  br;}

  
  fancy_spacer
  # ========================================================================== #
  # === Eilistraee's song                                     (Eilistraee tag)
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/eilistraees-song/
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#eilistraee_song
  # ========================================================================== #
  name_of_the_mod = :Eilistraees_Song_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Eilistraee's song") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'eilistraee_song', style: 'margin-bottom: 0px') {
    e "Eilistraee's song is a mod that expands the plot of Eilistraee."
    br
    e 'One of the sidequest yields an <b>Elephant Figurine</b>
    as a reward. This figurine will, upon use (one daily use)
    increase the hitpoints of the user by +50 hp, for two minutes.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Tales of the Deep Garden (garden tag, gardens tag, colours tag, tales tag)
  # ========================================================================== #
  # https://baldursgate.fandom.com/wiki/Tales_of_the_Deep_Gardens
  # https://downloads.weaselmods.net/download/tales-of-the-deep-gardens/
  # https://baldur-cob--bg-pl.translate.goog/totdg/solucja-totdg?_x_tr_sl=pl&_x_tr_tl=en
  # ========================================================================== #
  name_of_the_mod = :Tales_of_the_Deep_Garden_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Tales of the Deep Garden") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e '<b>Tales of the Deep Garden</b> can be started by talking to
    the <b>crazy mage</b> (the Mysterious Wizard) in the
    <b>Government district</b> of Athkatla, in the large, central park
    area there.'
    br
    e 'To participate in the tournament, a small riddle has to be
    solved first - the correct answer is <b>Mermaid</b>. Then, four
    items have to be found within three days.'
    br; reset_the_counter # === 1st item
    counter 'The first item can be found in the slum-district, at the
    southwestern corner of the tavern - look for a beggar. After asking
    for a coin he will attack the party.'
    br # === 3rd item
    e 'The third item can be obtained in the Temple district, in the
    southwestern part, from a NPC.'
    br # === 4th item
    e 'The fourth item can be found in the Flagron Inn, at the
    bar, where Barney, a fat man stands.'
    br
    e 'Now you have to <b>collect several colours</b>, in order
    to solve the main quest.'
    br; reset_the_counter
    # === Violet
    counter '<b>Violet</b> can be found on the table in the south-western part
    of the map.','marl2em'
    # === Gold
    counter '<b>Gold</b> and <b>Silver</b> can be found in the first
    cave, in the southwestern part of the map.','marl2em'
    # === Green and Blue
    counter '<b>Green</b> can be taken from the tree in the second cave; that
    tree can be found in the southeastern part of the map. <b>Blue</b> can be
    simply taken from the well in the northwestern part, also in the second
    cave.','marl2em'
    # === Gray
    counter 'Once the party has the Blue colour, they can visit the House of Gray.
    Inside of it is an old man called Senex. He wants to see the Blue colour and
    will give the Gray colour.','marl2em'
    # === Red
    counter '<b>Red</b> can be found in the pit in the southeastern area.
    Here the party has to take Red from the corpse and additionally take
    a dried plant from the hiding place, needed for the Green Witch.',
    'marl2em'
    br
    # === Black
    counter 'The <b>black colour</b> can only be obtained after the party
    has gathered <b>eight colours</b> already.'
    br
    e '<b>Silvertongue</b> (a woman) yields the following rewards,
    sorted by usefulness (top is best, bottom is worst), for a cost of
    16.000 gold coins:'
    br; reset_the_counter # costs 16.000 gp
    counter '- Green:  -1 to spell casting time','marl2em'
    counter '- Violet: regenerate 1 HP every 9 seconds','marl2em'
    counter '- Silver: +15% to magic resistance','marl2em'
    counter '- Red:    +1 THAC0, +1 Damage','marl2em'
    counter '- Yellow: +1 AC','marl2em'
    counter '- Black:  +5 saves against death, -1 reputation','marl2em'
    counter '- Gray:   +1 attack per round, -3 to death saves, -6 HP, -2 to THAC0','marl2em'
    counter '- Gold:   +10% resistance to acid, cold, electricity and fire','marl2em'
    counter '- Amber:  +7 to HP','marl2em'
    counter '- Blue:   +20000 experience points','marl2em'
    br
    e 'The <b>Riddle of the Hooded Man</b> can be solved as follows:'
    br
    l2em '  2, 4, 7, 2','BOLD darkblue'
    brbr
    finalizer_block(name_of_the_mod)
    br # === Quest run through at: https://baldur-cob--bg-pl.translate.goog/totdg/solucja-totdg?_x_tr_sl=pl&_x_tr_tl=en
    e 'A quest-run-through can be seen here:'
    br
    primary_link '
      https://baldur-cob--bg-pl.translate.goog/totdg/solucja-totdg?_x_tr_sl=pl&_x_tr_tl=en
    '
  }
  fancy_spacer
  # ========================================================================== #
  # === Grey the dog
  # ========================================================================== #
  name_of_the_mod = :Grey_the_dog_NPC_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Grey the dog") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'grey_the_dog', style: 'margin-bottom: 0px') {
    e "The mod Grey the dog features a loyal dog as <b>companion</b> for BG2."
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === The Unfinished Business mod             (business tag, unfinished tag)
  #
  # This one includes the kidnapping of Boo. It should be installed first.
  # ========================================================================== #
  # https://github.com/Pocket-Plane-Group/UnfinishedBusiness/releases
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#unfinished_business_mod
  # ========================================================================== #
  name_of_the_mod = :Unfinished_Business_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Unfinished Business mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'unfinished_business_mod', style: 'margin-bottom: 0px') {
    e "The <a href=\"https://github.com/Pocket-Plane-Group/UnfinishedBusiness/releases\">
    <b>Unfinished Business mod</b></a> is one of the oldest mods for Baldur's
    Gate 2 and restores much of the cut and dummied out content in the
    game."
    br
    e 'A few NPCs will appear, such as <b>Suna Seni</b>. Suna is
    not a recruitable NPC, though.'
    br
    e 'The mod includes side quests such as <b>The Kidnapping of Boo</b> and
    unique tweaks such as <b>Bodhi</b> hunting the party in Spellhold.'
    br
    e "If Drizzt is asked for help to fight Bodhi then <b>Artemis
    Entreri</b> will show up as a hostile creature in Bodhi's Lair."
    br
    e 'It is a highly recommended MOD - I give it 4 out of 5 stars. '+
       string_four_stars
    br
    e 'The <b>Kidnapping of Boo</b> can be started by going to the Athkatla
    Docks, waiting two days, and then re-entering again with Minsc in the
    party before departing again. The answers to the <b>three riddles</b>
    asked by Eleanya are:'
    br # Noise, Cabbage, no gem.
    e '"<b>Noise</b>",
    "<b>Cabbage</b>" and
    "<b>You need no gem</b>".'
    br
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === The Ooze Lounge
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/oozes-lounge/
  # ========================================================================== #
  name_of_the_mod = :The_Ooze_Lounge_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The Ooze Lounge") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'the_ooze_lounge', style: 'margin-bottom: 0px') {
    e 'The Ooze Lounge can be found in the Slums district,
    at a trapdoor on the streets.'
    br
    e 'The reward for finding a new eye for the floating eye
    is an <b>amulet</b>.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Dark Tidings                                             (tidings tag)
  # ========================================================================== #
  name_of_the_mod = :Dark_Tidings_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Dark Tidings") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'dark_tidings', style: 'margin-bottom: 0px') {
    e "<b>Dark Tidings</b> begins in the Docks district of Athkatla.
    Here, at the Sea's Bounty Tavern, one has to go upstairs and talk
    to <b>Thalass</b>."
    br
    e 'On the Lighthouse floor 4, the party can find a locked
    chest containing the <b>cellar key</b>, as well as a diary.
    So, head to the cellar next.'
    br
    e 'The wall stones have to be pushed in the following order:'
    br
    cmd 'Fire (left)'
    cmd 'Water (bottom-right)'
    cmd 'Earth (top-right)'
    cmd 'Air (top-left)'
    br
    e 'Next, take the <b>shadow brick</b> and place into the ground
    container on the left side of the first room in the lighthouse.
    Then let one party member wear the cultist helmet from the third
    floor, which will reveal a secret door on the left wall. Pass
    this secret entrance, then click on the creepy shadow portal
    on the cave wall behind it.'
    br
    e 'Take the <b>Luminous Crystal</b> from the altar, to cause
    the <b>Aspect of Tharizdun</b> to appear.'
    br
    e 'After having defeated the Aspect of Tharizdun, complete the
    ritual. Go back to the very first floor of the lighthouse. Place
    the luminous crystal in the container at the base of the
    central altar. Proceed by casting the following three spells
    in the following order:'
    br
    cmd 'Protection From Evil'
    cmd 'True Seeing # via a scroll'
    cmd 'Dispel/Remove Magic'
    br
    e 'All of these spells must be cast inside the <b>ritual
    chamber</b>.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === The White Queen mod                                        (Queen tag)
  # ========================================================================== #
  # The area code for the Silent Swamp location is wq0001.
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/the-white-queen/
  # ========================================================================== #
  # http://localhost/home/x/data/ruby/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#the_white_queen_mod
  # ========================================================================== #
  name_of_the_mod = :The_White_Queen_mod
  fancy_h1("#{BALDURS_GATE_LOGO} The White Queen mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'the_white_queen_mod', style: 'margin-bottom: 0px') {
    e "To start <b>The White Queen</b> storyline buy a new book at
    the <b>book merchant's store</b> on the <b>Promenade</b>."
    br
    e 'There is also a small side quest, where the party has
    to collect wine.'
    br
    e 'The demon (in the house where the White Queen resides)
    offers a powerful <b>sling</b>. The other rewards would be
    15.000 gp or 25.000 xp (or a change to <b>Reaction</b>),
    but the sling is definitely the item to go for here.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Call of the Lost Goddess                                 (goddess tag)
  # ========================================================================== #
  name_of_the_mod = :Call_of_the_Lost_Goddess_mod
  fancy_h1("#{BALDURS_GATE_LOGO} Call of the lost goddess") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'call_of_the_lost_goddess', style: 'margin-bottom: 0px') {
    e 'The <b>Call of the lost goddess</b> mod.'
    br
    e 'A new city district is added by this mod, called <b>Goldspires</b>.'
    br
    e 'This mod also includes over 40 new unique items.'
    br
    e 'After having removed fear from the Tree (use the <b>Remove Fear</b>
    spell), one can take the horn of the demon from the container near
    the Tree.'
    finalizer_block(name_of_the_mod)
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Additional links pertaining to Baldur's Gate 2
  # ========================================================================== #
  fancy3 "Additional links pertaining to Baldur's Gate 2"
  ptext {
    e 'Throne of Bhaal:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Baldur%27s_Gate_II:_Throne_of_Bhaal',
          css_class: 'marl2_5em BOLD'
  }
br;}}

__END__
  
  fancy_spacer
  # ========================================================================== #
  # === (06) Neverwinter Nights for BG2 (neverwinter night tag, neverwinter tag)
  #
  # Abbreviated as: NWNForBG
  # ========================================================================== #
  # Last release: 30.03.2024
  # Last version: 0.97
  # 06_NeverwinterNights-0.97-released-on-30.03.2024
  # ========================================================================== #
  # https://github.com/abalabokhin/NWNForBG
  # ========================================================================== #
  fancy_h1('Neverwinter Nights for BG2') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Neverwinter Nights for BG2.' 
    br
    # ======================================================================== #
    # === The Peninsula
    #
    # The Peninsula originally contains the ceremonial shield.
    # ======================================================================== #
    # https://mikesrpgcenter.com/nwn/items/quest.html
    # ======================================================================== #
    e 'The <b>Peninsula</b>:'
    br
    e "First, rescue <b>Master Johns</b> (he is at about the center of the
    map) and he will gladly tell you about the tunnel from the Tanglebrook
    Estate to the prison.'
    br
    e 'You will find the key to the manor under the Welcome Mat outside.
    The entrance to the cellar in the Tanglebrook Estate can be entered
    without problem. In the tunnels, walk carefully around the giant chess
    board to avoid traps and then defeat the fire beetles blocking
    the entrance to the Prison. You will see Lady Tanglebrook's
    body in the center of the chess board."
    br
    # ======================================================================== #
    # === The Beggar's Nest
    # ======================================================================== #
    e "The <b>Beggar's Nest</b>:"
    br
    e "This district is where the Wailing Death first appeared."
    br
    e 'Speak to <b>Drake</b> first. He will ask you to try to rescue
    <b>Kestral</b> and Jemanie.'
    br
    e '<b>Kestral</b> is in a house to the northeast. From him you will
    learn about the <b>Sword Coast Boys gang</b> and their leader Drawl.
    Drawl made a deal which esulted in the entire gang becoming undead,
    with himself as the most powerful. You will also learn their
    base is in an old abandoned warehouse to the north.'
    br
    e 'There are two ways to get into the Crypts. One way is to
    enter the Warehouse in the north-central part of the
    district. Go down the stairs to the second level and
    fight your way through the zombies to Drawl, their leader.'
    br
    e 'After Drawl is dead, open the cell to release Walters, the
    missing guard, who well tell you what he knows about Drawl
    and the undead. He will suggest you find this "Gulnam"
    creature that Drawl was talking about. There are stairs
    nearby that lead to the Crypts.'
    br
    e "The other way into the Crypts is through the Snake Cult
    Estate in the northwest corner of the Beggar's Nest. You
    need to to have the Estate Ward Stone with you to
    enter."
    br
    e "Either way, head through the Crypts to the lair of a Dire
    Bloated Spider. Behind the spider are some stairs that lead to
    the Great Graveyard. From there, you can enter the
    Warrens of the Damned."
    br
    e 'Just inside the <b>Warrens of the Damned</b> Gulnan will speak
    to you through a zombie. She appears to be one of the Waterdhavian
    creatures.'
    br
    e "In a room near the southeast corner of the area, you will
    find Torin's body, on which you will find a ring which
    should be returned to his brother Jemanie and an Ancient Key."
    br
    e "One door is for the Warrens of Damned. A note says <b>a wall
    at arms length</b>. Put the ceremonial shield you got from
    tomb #1 into the container for the door to open."
    br
    e "In the northwest corner of the area, you will find Gulnan's
    Journal and another Ancient Key."
    br
    e "Use the Ancient Key to open the door to the center
    chamber from the northern part of the area. Destroy
    the pedestal on the dais to the southwest to remove
    half of the undead in the room. Defeat Gulnan and
    the rest of her undead servants and take her Heart 
    from her body."
    br
    e "With Gulnan dead and the focus destroyed, the undead will no longer
    haunt the Beggar's Nest. Report your success to Harben Ashensmith in
    the Shining Serpent for a reward."
    br
    e "Bring the <b>Yuan-Ti Heart</b> to <b>Aribeth</b> in the Hall
    of Justice."
    br
    # ======================================================================== #
    # === The Dock's District
    # ======================================================================== #
    e "The <b>Dock's District</b>:"
    br
    primary_link 'https://forums.beamdog.com/discussion/88115/mod-neverwinter-for-baldurs-gate/p1'
    primary_link 'https://github.com/abalabokhin/NWNForBG'
    primary_link 'https://mikesrpgcenter.com/nwn/walkthrough.html' # A walkthrough.
  }
  fancy_spacer
  # ========================================================================== #
  # === Bridge's block mod                (block tag, bridge tag, bridges tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Bridge's block mod (Last official update:
  24.07.2024)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "The <b>Bridge's block mod</b> contains a few small quests."
    br
    e 'The three <b>glyph fragments</b> can be found at:'
    br; reset_the_counter
    counter "The slavers' ship (the ship-looking building in the Slums District
    of Athkatla).",'marl2em'
    counter 'The pirate cave in seas bounty tavern.','marl2em'
    counter 'The "<b>guarded compound</b>" in the temple district (where the
    unique katana can be found).','marl2em'
    br
    e 'Another subquest is <b>Mr. Rat</b> needing a special apple. This apple is
    in the stall of one of the vendors in the bridge district - either <b>Bel
    Dalemark</b> or one of the other two nearby, next to Bel.'
    br
    e 'Discussion for this mod can be seen here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/83206/mod-athkatlan-grounds-the-bridges-block'
    br
    the_mod_can_be_downloaded_from(
      'https://forums.beamdog.com/discussion/83206/mod-athkatlan-grounds-the-bridges-block',
      'https://weaselmods.net/showthread.php?tid=716',
      'https://downloads.weaselmods.net/download/bridges-block/'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === Verr'sza
  #
  # mkdir 02_VerrBG2-v2.2-26.01.2025/
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/verrsza-bg2ee/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Verr'sza (Last official update:
  19.12.2024)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "VERR'SZA is a NPC."
  }
  fancy_spacer
  # ========================================================================== #
  # === (09) The Sellswords mod
  #
  # Last official update: 15.05.2021
  # Latest version:       9.1
  #
  # mkdir 09_The_Sellswords_mod_v91_15.05.2021
  # ========================================================================== #
  # https://github.com/Pocket-Plane-Group/Sellswords/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Sellswords mod "\
           "(Last official update: <b>15.05.2021</b>)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'In order to <b>leave the Drow-area again</b>, one has
    to <b>collect three wardstones</b>.'
    br
    e "There are various rewards distributed by this mod. One of the more
    useful one is the drider's gauntlet, which will set the Strength
    of the wearer to <b>19</b>. This may be especially useful - and
    fitting - for <b>Viconia</b>." 
    br
    download_the_mod_from('
      https://www.pocketplane.net/the-sellswords/
    ')
    br
    primary_link 'https://github.com/Pocket-Plane-Group/Sellswords/releases'
  }
  
  # ========================================================================== #
  # === Every Mod and Dog v11, by cliffette
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Every Mod and Dog v11, by cliffette (last release in 03.01.2021)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "<b>Every Mod and Dog v11</b> adds a few sidequest, such as the Troll called
    <b>Tegenk</b>, whose happiness depends on whether or not you can help
    him keep his promise. <b>Tegenk</b> can be found in the wilderness in
    the <b>Druid's Grove</b>."
    br
    the_mod_can_be_downloaded_from(
      'https://www.gibberlings3.net/files/file/707-every-mod-and-dog/',
      'https://www.gibberlings3.net/mods/quests/cliffette/'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === Sirene NPC
  # ========================================================================== #
  # Sirene-NPC-for-BG2-EE-master.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+" Sirene NPC") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Sirene NPC'
  }
  fancy_spacer
  # ========================================================================== #
  # === Quallo's quest (The Riddle of the Sewers)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+" Quallo's quest (The Riddle of the Sewers)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Solve_the_Riddle_of_the_Sewers'
    br
    e '- Enter the Sewers beneath the Slums through a secret door by the
    gladiator prison in the Copper Coronet in the Athkatla Slums.
    At the eastern section of the area, you will find a room with
    drain pipes, a voice will tell you that you must solve the
    riddle in order to gain a magical sword called "Lilarcor".'
    br
    e "- Go to the southern corner of the area and kill Quallo's
    friend the Carrion Crawler. Take the blood from the body."
    br
    e '- Stick your hands into the grating in the northwest
    corner of the sewers to find a Hand. Caution: Whoever does
    this will take damage. The area is guarded by an Otyugh.'
    br
    e "- Take the Lover's Ring off the hand of one of
    the skeletons near the center of the area."
    br
    e "- Near the center of the sewers you can find the
    Shaman's Staff in the possession of a kobold shaman.
    Defeat him or buy the staff from him."
    br
    e '- Return to the drain room with the four items and
    click on the drains in the following order:'
    br
    e '3rd, 1st, 2nd, 4th. The magical sword Lilarcor
    will be added to the inventory and the party
    receives experience points.'
  }
  fancy_spacer
  # ========================================================================== #
  # === BG1 NPCs for SoA & ToB mod                              (BG1 tag)
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/82463/mod-bg1-npcs-for-soa-tob/p1
  # https://github.com/SpellholdStudios/BG1_NPCs_for_SoA_-_ToB
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+" BG1 NPCs for SoA & ToB mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'BG1 NPCs for SoA & ToB'
    br
    primary_link 'https://github.com/SpellholdStudios/BG1_NPCs_for_SoA_-_ToB'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Quest pack mod
  #
  # Last upstream update: 20.07.2022 (20th July 2022)
  # Latest version:       3.5 
  #
  # mkdir 05_The_Quest_pack_mod_v3.5_released_on_20.07.2022; cd 05_The_Quest_pack_mod_v3.5_released_on_20.07.2022
  # ========================================================================== #
  # https://forums.pocketplane.net/index.php/board,21.0.html
  # https://forums.pocketplane.net/index.php?PHPSESSID=k4nsca8avbp7jb6sv5sdgddhv7&topic=29950.0
  # https://pocketplane.net/mods/questpack-v35-win.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Quest pack mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>quest pack mod</b>. The latest version is <b>3.5</b>.'
    br
    primary_link 'https://www.pocketplane.net/quest-pack/'
    primary_link 'https://forums.pocketplane.net/index.php/board,21.0.html'
    primary_link 'https://pocketplane.net/mods/questpack-v35-win.zip'
  }
  fancy_spacer
  # ========================================================================== #
  # === (04) The Dreadful Tales: In Love, Undeath - a new quest and a companion for BG2EE
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/in-love-undeath/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'The Dreadful Tales: In Love, Undeath - a 
    new quest and a companion for BG2EE mod (last release: 28.07.2023)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "This quest starts in the Temple's District."
    br
    e 'Discussion of this mod can be found here:'
    br
    selfy 'https://forums.beamdog.com/discussion/87272/mod-the-dreadful-tales-in-love-undeath-a-new-quest-and-a-companion-for-bg2ee',
          css_class: 'BOLD marl2_5em'
    br
    the_mod_can_be_downloaded_from(
      'https://downloads.weaselmods.net/download/in-love-undeath/'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === The Dreadful Tales: Juniper and the Stone Leech mod (Juniper tag)
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/juniper-and-the-stone-leech/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'The Dreadful Tales: Juniper and the Stone Leech mod '\
           '(last release: 07.10.2023)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Juniper and the Stone Leech is a mod that introduces a new <b>Throne
    of Bhaal</b> adventure along with a new companion that will ask you
    to join her in the investigation of the otherworldly realm of
    Har'Akir, part of Ravenloft. Help Juniper and travel with her to the
    mysterious land. See the dark temple, located in the dark desert
    of Har'Akir, fight enemies, discover the halls of the temple
    and find the source of the disturbance that troubles your new friend."
    br
    e 'Discussion of this mod can be found here:'
    br
    selfy 'https://forums.beamdog.com/discussion/87645/mod-the-dreadful-tales-juniper-and-the-stone-leech',
          css_class: 'BOLD marl2_5em'
    br
    the_mod_can_be_downloaded_from(
      'https://downloads.weaselmods.net/download/juniper-and-the-stone-leech/'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Unofficial Item Pack
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/56567/mod-bgii-ee-unofficial-item-pack/p1
  # https://forums.beamdog.com/uploads/editor/q5/zjfyp5tvk60j.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Unofficial Item Pack (Version 2.7b)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/1ykgldN.jpg',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_unofficial_item_pack'; drag_for :drag_bg2_unofficial_item_pack
  ptext {
    e 'The <b>Unofficial Item Pack</b> includes:'
    br
    lem "01) Malla's Soul Stone - Human souls are source great strength. Gotta catch 'em all!"
    lem "02) Sigil of Tyr - Only for the best of us."
    lem "03) Dark Elven Chain - Armor Class: +1; spellcasting is not disabled"
    lem "04) Handmaiden's Mace - Now Mace +3 (also new, better model)"
    lem "05) <b>Mask of King Strohm III</b> - I do not see practically
    nothing. The mask will now yield <b>True Sight once per day</b>."
    lem "06) Symbol of Amaunator - Praise the sun! (sunray once per day)"
    lem "07) Human Flesh +5 - You can be evil and also look elegant."
    lem "08) Keepsake Locket - True love make you stronger."
    lem "09) Shadow Dragon Wardstone - provides Negative Plane Protection."
    lem "10) Mantle of Waukeen - You can save the world with this
    stylish jewelry!"
    lem "14) Deirex's Gems - Souls belonging drow warriors? Does Tenser's
    Transformation once per day."
    lem "15) Talisman of the Hearthfire - three times dimension door per
    day."
    lem "16) Girdle of Fortitude - Stay healthy little longer."
    lem "17) Blackmist +4 - Now you see me..."
    lem "99) Hourglass of Gond - Reward for the hardest fight of your life.
    The cowled wizards have the Hourglass of Gond, so we have to
    kill their female leader. 
    Just keep violating those Athkatla 'no magic without license'
    rules and fight summoned Clowded Wizards units and she will
    eventually show up. That was a very tough battle. There were 10-15
    attempts.
    I assume in Chapter 3 it is almost impossible to beat her without using
    either traps or(and) scroll of Protection from Magic. I took her down
    using two characters. Char (sorcerer) + Minsc. Minsс was under the
    Protection from Magic scroll. Sorc was using True Sight and Breach
    all the time. I also casted Protection from Elements and Protection
    from Magical Energy on Char before the battle. And activated the
    battle with the Spell Immunity spell on the main character, in
    order to be protected from Imprisonment."
    br
    e 'So in other words, use:'
    br
    e '- Protection from Magic'
    e '- Protection from Magical Energy'
    e '- Protection from Elements'
    br
    primary_link 'https://forums.beamdog.com/discussion/56567/mod-bgii-ee-unofficial-item-pack/p1'
  }
  
  fancy_spacer
  # ========================================================================== #
  # === The Circus Tent
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Circus Tent") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Circus_Tent'
    br
    e 'The answer to the first riddle for the djinni is: "The
    prince is 30 while the princess is 40".'
    br
    e 'For the second riddle the answer is "nothing".'
  }
  fancy_spacer
  # ========================================================================== #
  # === (08) Test your mettle mod                                 (Mettle tag)
  #
  # Last release:   30.04.2024
  # Latest version: 1.5
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Test your mettle mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://github.com/Argent77/A7-TestYourMettle'
    br
    e "The adventure starts in the Planar Sphere in Athkatla's Slum District."
    br
    e 'The first waypoint of note lies in the very western part of the maze.'
    br
    primary_link 'https://forums.beamdog.com/discussion/70489/mod-test-your-mettle/p1'
    primary_link 'https://github.com/Argent77/A7-TestYourMettle/releases/tag/v1.5'
  }
  fancy_spacer
  # ========================================================================== #
  # === (18) Throne of the Mad God
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Throne of the Mad God") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The lower part of the key appears when the party interacts with
    the altar in the large central room - the one with the tubes - and
    kill the monster that appears. This creature has the lower part of
    the mold.'
    br
  br;}
  
  # ========================================================================== #
  # === (09) Dusk Aldant, The Wizard Slayer                        (dusk tag)
  #
  # This one is now called bg2-autumns-twilight-mod.
  #
  # Last upstream update: 18.10.2024
  # Latest Version:       1.0.0
  #
  # mkdir 44_Autumns_Twilight_including_Dusk_Aldant_The_Wizard_Slayer_mod_v1.0.0_published_on_18.10.2024; cd 44_Autumns_Twilight_including_Dusk_Aldant_The_Wizard_Slayer_mod_v1.0.0_published_on_18.10.2024
  # wget https://github.com/evancauteren/bg2-autumns-twilight-mod/releases/download/v1.0.0/bg2-autumns-twilight-mod-1_0.zip
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/87246/npc-mod-dusk-aldant-the-wizard-slayer/p1
  # https://github.com/evancauteren/bg2-autumns-twilight-mod/releases/tag/v1.0.0
  # https://github.com/RamosPabloA/NPC_Dusk_MOD/releases/
  # https://github.com/RamosPabloA/NPC_Dusk_MOD/releases/download/v1.5.0/NPC_Dusk_MOD.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Dusk Aldant, The Wizard Slayer mod 
  (last release: 13.12.2023)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Dusk Aldant, <b>The Wizard Slayer</b>."
    br
    e 'Various items can be obtained in this mod, such as <b>Ira</b>, an epic
    weapon forged in the shadows of Pandemonium. It is the ultimate upgrade of
    the crimson sword.'
    br
    e 'The discussion can be seen here:'
    br
    primary_link('
      https://forums.beamdog.com/discussion/87246/npc-mod-dusk-aldant-the-wizard-slayer/p1
    ')
    primary_link('
      https://forums.beamdog.com/discussion/88816/mod-autumns-twilight-bg2at#latest
    ')
    br
    the_mod_can_be_downloaded_from(
      'https://github.com/RamosPabloA/NPC_Dusk_MOD/releases/'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (21) DungeonCrawl mod
  #
  # mkdir 22_DungeonCrawl_mod_v13.1_released_on_16.05.2021; cd 22_DungeonCrawl_mod_v13.1_released_on_16.05.2021
  # wget https://github.com/Pocket-Plane-Group/Dungeon_Crawl/releases/download/v13.1/DungeonCrawl_v13-1.zip
  #
  # https://www.pocketplane.net/dungeon-crawl/
  # https://github.com/Pocket-Plane-Group/Dungeon_Crawl/releases
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}DungeonCrawl mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'DungeonCrawl mod'
  }
  fancy_spacer
  # ========================================================================== #
  # === (21) Song and Silence (silence tag) 
  #
  # Last upstream update: 03.01.2024
  # Version:              18
  #
  # mkdir 21_song_and_silence-v18-released_on_03.01.2024; cd 21_song_and_silence-v18-released_on_03.01.2024
  # wget https://github.com/Gibberlings3/SongAndSilence/releases/download/v18/song_and_silence-v18.exe      
  # ========================================================================== #
  # https://www.gibberlings3.net/mods/kits/sns/
  # https://github.com/Gibberlings3/SongAndSilence
  # https://github.com/Gibberlings3/SongAndSilence/releases/
  # https://github.com/Gibberlings3/SongAndSilence/releases/tag/v18
  # wget https://github.com/Gibberlings3/SongAndSilence/releases/download/v18/song_and_silence-v18.exe
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}Song and Silence (last release: ,
  Latest Version: 18)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>Song and Silence mod</b> is a mod for bards and thieves. It will add
    many options for these two classes.'
    br
    primary_link 'https://www.gibberlings3.net/mods/kits/sns/'
    primary_link 'https://www.gibberlings3.net/files/file/977-song-and-silence/'
    primary_link 'https://github.com/Gibberlings3/SongAndSilence'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Ghostly Apparition 
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}The Ghostly Apparition") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>Ghostly Apparition</b> is a side quest available in
    "<b>Saradush Prison</b>".'
    br
    e 'Put the "skull" and the "rusted amulet" in the cell next door and the
    apparition will appear again, asking you to sanctify his grave. The "rusted
    amulet" can be found in a nearby cell.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/The_Ghostly_Apparition'
    ntab 'https://mikesrpgcenter.com/bgate2/walkthrough-tob.html#apparition'
  }
  fancy_spacer
  # ========================================================================== #
  # === (10) Coran NPC
  #
  # 03_Coran_NPC_mod_for_Baldurs_Gate_II_v9_01.01.2023
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}Coran NPC") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Coran NPC'
  }
  fancy_spacer
  # ========================================================================== #
  # === The imps in the City of Caverns (Riddle of the Imps, imp tag)
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}The imps in the City of Caverns (Riddle of the Imps, imp tag)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-4/areas/city-of-caverns.php'
    br
    e 'Here are two Imps who want to play a little game with you. If you
    win the game, they will open the chest at (x=620, y=3070) for you and lure
    out the Spectre that is guarding it. If you try to loot the chest
    without their help, the Spectre will kill you, so accept to play
    their game – but make sure to have your Thief sweep the area for
    traps first! There are six traps in the area, at least some of
    which can prove lethal.'
    br
    e "For the Imps' game, there are also five famous characters
    who will each give you an item and a tip on which item they
    need. Your job is to place each item in the chest behind
    the person it belongs to."
    br
    cmd '(1) Elminster:          wants the "pipe".'
    cmd '(2) Khelben Blackstaff: wants the "staff".'
    cmd '(3) Alustriel:          wants the "pendant".'
    cmd '(4) Piergeiron:         wants the "helmet".'
    cmd "(5) Drizzt do'Urden:    wants the \"scimitar\"."
    br
    e "Reward: for winning the game, each party member receives
    18.500 XP and the Imps open the last chest and dispose of
    the Spectre. You can now loot the chest for a pair of
    \"Boots of Etherealness\" and a nifty Cloak of Protection
    +2."
  }
  fancy_spacer
  # ========================================================================== #
  # === (10) Luxley (luxley tag) 
  #
  # Last upstream update: 17.06.2021
  # Version:              2.0
  #
  # mkdir 10_The_Luxley_Family_mod_v2.0_released_on_17.06.2021
  # cd 10_The_Luxley_Family-v2.0-released-on-17.06.2021
  # wget https://github.com/SpellholdStudios/The_Luxley_Family/releases/download/v2.0.0/the-luxley-family-v2.0.0.zip
  # ========================================================================== #
  # https://spellholdstudios.github.io/readmes/luxleysoa-readme-english.html
  # https://github.com/SpellholdStudios/The_Luxley_Family
  # ========================================================================== #
  # wget https://github.com/SpellholdStudios/The_Luxley_Family/releases/download/v2.0.0/the-luxley-family-v2.0.0.zip
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}The Luxley family (last release: 30.12.2022, Version: 12.9)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The Luxley family.'
    br
    primary_link 'https://spellholdstudios.github.io/readmes/luxleysoa-readme-english.html'
    primary_link 'https://github.com/SpellholdStudios/The_Luxley_Family'
  }
  fancy_spacer
  # ========================================================================== #
  # === (20) Shadows over Soubar                                  (Soubar tag)
  # ========================================================================== #
  # Last release: 07.07.2024
  # Last version: 2.1.2
  # mkdir 20_Shadows_over_Soubar_v2.1.2-released-on-07.07.2024; cd 20_Shadows_over_Soubar_v2.1.2-released-on-07.07.2024
  # wget https://github.com/SpellholdStudios/Shadows_over_Soubar/releases/download/v2.1.2/shadows-over-soubar-2.1.2.zip
  # ========================================================================== #
  # https://github.com/SpellholdStudios/Shadows_over_Soubar/releases
  # https://github.com/SpellholdStudios/Shadows_over_Soubar/releases/tag/2.0
  # wget https://github.com/SpellholdStudios/Shadows_over_Soubar/releases/download/v2.1.2/shadows-over-soubar-2.1.2.zip
  # ========================================================================== #
  fancy_h1('Shadows over Soubar') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'In Trademeet our hero learns that some mysterious men from the
    north are looking for them.'
    br
    e 'Note that the NPC called Selence is also part of this mod.'
    br
    e 'Sir William tends to sleep, so one may have to wait until daytime
    - or simply idle for a while. He will eventually wake up.'
    br
    e 'How to defeat the <b>Master Werewolf</b>?'
    br
    e 'Use summons as fodder, and Magic Missiles, Skull
    Trap, Cloudkill, Lower Resistance, Doom. An
    Efreeti can also be used to cast magic.'
    br
    e '<b>Ceeb Isson</b> can be found in the Trademeet tavern.'
    br
    e '<b>Selence</b> can lateron be found upstairs in the Five Flagons
    inn. Hand over the items to Selence for lots of gold - or keep them.
    Aerie may want to try the <b>Argent Shield</b>: AC+3 and +25% Magic
    Resistance.'
    br
    e "One can then go into Ribald's market, but only one character
    at a time can enter."
    br
    e "After completing Selence' quest one can open the chest upstairs
    in the Copper Coronet back rooms, in Llynis' room. Do first obtain
    a Stronghold, though."
    br
    e '<b>Soubar</b> has another Robe of Vecna.'
    br
    e 'The Chaunteau Science Reading Room contains scrolls of
    protection, as well as various containers for convenient storage
    of gear and loot. A Tome of Clear Thought (INT +1) is also
    found here, as well as a ring of Invisibility and a 
    Periapt Amulet of Life Protection.'
    br
    primary_link 'https://github.com/SpellholdStudios/Shadows_over_Soubar/releases'
    # === http://www.shsforums.net/topic/59716-baldurs-gate-2-shadows-over-soubar-walkthrough-2018/
    primary_link 'http://www.shsforums.net/topic/59716-baldurs-gate-2-shadows-over-soubar-walkthrough-2018/'
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (23) MagicStore mod
  # ========================================================================== #
  # Last release: 10.03.2024 
  # Last version: 4.1
  #
  # mkdir 23_MagicStoreMod-4.1-10.03.2024; cd 23_MagicStoreMod-4.1-10.03.2024
  # wget https://github.com/Argent77/A7-MagicStore/releases/download/v4.1/win-A7-MagicStore-v4.1.zip
  # ========================================================================== #
  # https://github.com/Argent77/A7-MagicStore
  # ========================================================================== #
  fancy_h1('MagicStore') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>Magic Store</b> mod can be obtained from this webpage:'
    br
    primary_link 'https://github.com/Argent77/A7-MagicStore'
    primary_link 'https://github.com/Argent77/A7-MagicStore/releases'
    primary_link 'https://github.com/Argent77/A7-MagicStore/releases/download/v4.0/win-A7-MagicStore-v4.0.zip'
  }
  fancy_spacer
  # ========================================================================== #
  # === Dorn the half-orc companion                                 (Dorn tag)
  # ========================================================================== #
  fancy_h1('Dorn the half-orc companion') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'dorn') {
    ntab 'https://baldursgate.fandom.com/wiki/Dorn_Il-Khan'
    ntab 'https://baldursgate.fandom.com/wiki/Dorn_Il-Khan#Quests'
    ntab 'https://baldursgate.fandom.com/wiki/Dorn_Il-Khan#Recruitment_3'
    ntab 'https://baldursgate.fandom.com/wiki/Abyssal_Blade#Statistics'
    ntab 'https://baldursgate.fandom.com/wiki/Dorn%27s_bloody_path#Throne_of_Bhaal'
    ntab 'https://baldursgate.fandom.com/wiki/Dorn%27s_bloody_path'
    ntab 'https://www.gamebanshee.com/baldursgateii/walkthrough/resurrectiongorge.php'
    br
    e "Dorn is available to recruit from Baldur's Gate II Chapter 2. Travel
    to the southern part of \"<b>Temple</b>\" District, talk to him to let him
    join. Recruiting him will initiate a number of reputation-damaging
    but rewarding quests."
    br
    e 'His quests can be found here:'
    br
    ntab' https://baldursgate.fandom.com/wiki/Dorn%27s_bloody_path'
    ntab' https://baldursgate.fandom.com/wiki/Dorn%27s_bloody_path#Throne_of_Bhaal'
    br
    e 'You can cross the rope bridges until you reach Yarrow and Treadsoft.
    Treadsoft is in the northern part of the map.'
    br
    e 'Siding with Ur-Gothoz will earn him the powerful helmet The Visage.'
    br
    e 'If you leave at least one of them alive, be it Ur-Gothoz or Azothet,
    you unlock his final quest in the godly plane of Lunia. To leave
    that area use an Acorn of Yarrow.'
    br
    e "In Watcher's Keep, the player can get him the blackguard-only
    sword Ir'revrykal, effectively an evil version of Carsomyr."
    br
    e 'Dorn is the only companion other than Minsc and Valygar that can use
    Defender of Easthaven, Armor of Faith, and Hardiness, making him an
    excellent physical damage tank. Draw Upon Holy Might allows him to
    reach 25 Strength at level 26 without the use of magical equipment,
    which can be saved for other party members, along with 22 Dexterity
    and 20 Constitution.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Strategies when fighting against Ruhk and Maharajah
  # ========================================================================== #
  fancy2 "Strategies when fighting against Ruhk and Maharajah"
  ptext {
    e '- Use +3 weapons against these opponents.'
    br
    e '- Turning into a jelly slime can help with magic resist.'
    br
    e '- Use mirror image to reduce the chance of them hitting
    your party.'
    br
    e '- Use summonables against them.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Horn of Valhalla
  # ========================================================================== #
  fancy2 "The Horn of Valhalla"
  ptext {
    e "In the Bridge District, north western wall, there's a
    table of fish outside a house, upstairs in the trapped
    chest at the foot of the bed. The Horn of Valhalla can
    be obtained from that chest."
    br
    e 'You need a diamond for the first upgrade of the horn.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The killer mimic and the mimic's blood:
  # ========================================================================== #
  fancy2 "The killer mimic and the mimic's blood:"
  ptext {
    e 'This is a short side quest from the Umar Hills.'
    br
    %w(
      https://baldursgate.fandom.com/wiki/Find_mimic%27s_blood_for_Jermien_the_Cowled_Wizard
      https://baldursgate.fandom.com/wiki/Killer_Mimic
      https://baldursgate.fandom.com/wiki/Mimic%27s_Blood
      https://baldursgate.fandom.com/wiki/Jermien%27s_Home
    ).each {|remote_URL|
      oop_a(remote_URL,
            description: :copy,
            css_class:   'mars2em BOLD',
            new_tab:     true,
            breakline:   true)
    }
  }
  fancy_spacer
  # ========================================================================== #
  # === An overview of the available quests in Baldur's Gate II:
  # ========================================================================== #
  fancy2 "An overview of the available quests in Baldur's Gate II:"
  ptext {
    oop_a 'https://baldursgate.fandom.com/wiki/Quests#Shadows_of_Amn',
           description: 'Quests',
           css_class:   'mars2em BOLD',
           new_tab:     true
  }
  fancy_spacer
  # ========================================================================== #
  # === Recruiting Viconia
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games/lib/games/www/baldurs_gate2/baldurs_gate2.cgi#recruiting_viconia
  # ========================================================================== #
  fancy2 "Recruiting Viconia:"
  ptext(id: 'recruiting_viconia') {
    e "Viconia DeVir is available to recruit from Chapter 2. She can be found in
    Athkatla's Government District near the Prison, where she must be rescued
    from followers of Beshaba, who want to burn her on a stake. If you try
    to rescue her, this will provoke the followers to attack your party."
    br
    e "As Drow have gained extreme notoriety in the Forgotten Realms,
    recruiting Viconia reduces the party's reputation by 2. This
    reputation loss is regained as soon as she is removed from
    the group."
    br
    e "If she is removed from the party, she can be found in the
    Graveyard, near the far entrance of Bodhi's lair."
    br
    oop_a 'https://baldursgate.fandom.com/wiki/Viconia_DeVir#Recruitment_3',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://sorcerers.net/Games/BG2/Walkthrough2/npcs/viconia.php',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
  }
  fancy_spacer
  # ========================================================================== #
  # === Neera the wild-mage and the other wild mages (and Daxus, neera tag)
  # ========================================================================== #
  fancy2 "Neera and wild magic:"
  ptext {
    oop_a 'https://baldursgate.fandom.com/wiki/Neera%27s_Hidden_Refuge',
           description: :base,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    br
    e "After meeting Hayes and Telana at the gate, the next move of
    the party is to find <b>Daxus Taralom</b> - but before that, explore a
    bit, people around the camp have their own affairs, it's recommended
    to complete these mini quests before triggering Daxus's rescue
    in Delosar's Inn for more rewards there and after."
    br 
    e "To find Daxus, go to the \"Bridge District\" in Athkatla,
    Hayes will be waiting south-west of \"Delosar's Inn\", go
    inside to find Daxus on the lower floor."
    br
    e "Back to Hidden Refuge the party notices that it was under
    attack. Many of its former inhabitants are gone. Telana is
    still here though, as are Mereth and Kirik, if you completed
    their quests. After talking to Telana, the party should
    head off to the Red Wizard Enclave in Waukeen's Promenade."
    br
    e 'Associated Miniquests:'
    br
    e "#1) Mereth - Mereth's hairband: The hairband can be found
    in the crates in the \"Bridge District\" near where the
    cutscene took place. Upon return of the item, Mereth
    rewards Gorion's Ward with a Wooden Horse Necklace."
    br
    e "#2) Knocktor the Fizzled - Talisman of the
    Hearthfire (3500 XP)"
    br
    e 'You need: 2 Diamonds, a Silver Necklace, and 3,000
    gold. The talisman can teleport into the hidden
    refuge.'
    br
    e '#3) Mironda - A new beer for Mironda (3500 XP)'
    br
    oop_a 'https://baldursgate.fandom.com/wiki/A_new_beer_for_Mironda',
           description: :base_tr,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    br
    e "In \"<b>A new beer for Mironda</b>\", Mironda in the Hidden
    Refuge asks to get a cask of Halfling's Help from \"Vyatri's
    Pub\" in Trademeet for 50 gold. The reward will be a
    tankard."
    br
    e "#4) Barad Ding - Barad Ding's eight cats"
    br
    e "Talk to Barad Ding to initiate the quest and agree to locate his eight
    missing cats. They are all located in the Wild Forest and he will give
    you Cat Food to lure them into your inventory. It is a good idea to
    have cleared the traps from the forest prior to luring any cats. The
    cats have a 5% chance to escape from your inventory every two rounds,
    which means that once you have a cat in a party member's inventory you
    should head for the nearest map edge and travel to the Hidden Refuge.
    The cat will automatically leave your inventory once you arrive and
    you can immediately travel back to find the remaining cats. The cats
    also cannot be moved from the inventory space they occupy, so you
    cannot put them in a container such as Dragomir's Respite to hold
    onto them."
    br
    e "If you run out of cat food you can return to Barad Ding and ask for
    more. It is not known if there is a limit to how many times you can
    request this although his character says he does not have an unlimited
    supply."
    br
    e "#5) Reginald - Pester him then go around, kite him (no need
        to turn AI off), after a while he'll cease attacking, wait."
    br
    e "#6) Amanis Khal & Kirik Khal - Amanis Khal's Missing Son (3500 XP)"
    br
    selfy 'https://baldursgate.fandom.com/wiki/Amanis_Khal%27s_Missing_Son'
    br
    e 'The missing son is at the wild forest area, at the northwestern area.'
    br
    e 'You then have to fight Lanneth. Have her drink all potions - she will
    become more visible afterwards. Her corpse will contain the
    Laboratory Key. '
    br
    e 'To then open the cages, do this:'
    br
    e 'The correct order is 55-13-11-42 aka:'
    br
    e '  55 (Amanis - this is the top-right cage)'
    e '  13 (unnamed female Wild Mage - this is bottom-left)'
    e '  11 (Barad Ding - )'
    e '  42 (Zaviak) - in other words: 55-13-11-42'
    br
    e ' After Zaviak, the remaining numbered captives (Reginald, Knocktor
    and Daxus, if still alive) may be freed in any order. Talking
    to a Wild mage after their cage is opened will dismiss them;
    each escaping Wild Mage is worth 5000xp.'
    br
    e "In Lanneth's Personal Quarters one can find the Magical
    Sword spell, which is immensely useful."   
  }
  fancy_spacer
  # ========================================================================== #
  # === Aataqah's question in the very first dungeon:
  # ========================================================================== #
  fancy2 "Aataqah's question in the very first dungeon:"
  ptext {
    oop_a 'https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-1/quests/quest-list.php',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://baldursgate.fandom.com/wiki/Chapter_One',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://baldursgate.fandom.com/wiki/Aataqah%27s_Question',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    br
    e 'Choose to "press the button". You will be congratulated by
    <b>Ataqah</b> and fight a weak Ogre Mage, as well as receive a
    3500 XP bonus.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Investigate the Deaths in the Umar Hills (lots of werewolves and shadows):
  # ========================================================================== #
  fancy2 'Investigate the Deaths in the Umar Hills (lots of werewolves and shadows):'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Investigate_the_Deaths_in_the_Umar_Hills'
    br
    e 'You need to go to the Temple Ruins, in order to
    find the female werewolf.'
    br
    e 'The statue gives three tests for The Holy Ritual (2,3,1,3,1,1,1,3,2):'
    br
    cmd 'Test 1 (2, 3, 1)'
    cmd 'I shall say a prayer to the light'
    cmd 'I shall hold the Holy book...'
    cmd 'I shall reflect on the glory...'
    br
    cmd 'Test 2 (3, 1, 1)'
    cmd 'I shall sing a hymn...'
    cmd 'I shall raise my hands to the light'
    cmd 'I shall rejoice at the dominance...'
    br
    cmd 'Test 3 (1, 3, 2)'
    cmd 'I will recite the Tenets of faith'
    cmd 'I will hold high my children...'
    cmd 'I shall mourn as I watch...'
    br
    e "The Symbol of Amaunator is created when the
    Sun Ray Symbol, Dawn's Light Symbol, and
    Lightstone Symbol are together in your
    party's inventory. It is an item needed
    for Investigate the Deaths in the Umar
    Hills."
    br
    e 'The <b>Lightstone Symbol</b> can be found hidden in
    an alcove in the back of a cell near the defiled chapel
    in the Ruined Temple (the one with the sneaky shade).'
  }
  fancy_spacer
  # ========================================================================== #
  # === Ranger-Protector of the Umar Hills
  # ========================================================================== #
  fancy2 'Ranger-Protector of the Umar Hills'
  ptext {
    e 'The reward for this quest will be +1 Reputation, 26750 XP, and
    a Moon Dog Figurine.'
    br
    e 'Four days after the completion of the second Ranger Stronghold
    quest, the party will again meet Delon. He asks you to return
    to the Umar Hills again and speak to Minister Lloyd. This
    time, the Umar Witch has returned!'
    br
    e 'See also:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Ranger-Protector_of_the_Umar_Hills'
  }
  fancy_spacer
  # ========================================================================== #
  # === Jaheira becomes a Great Druidess:
  # ========================================================================== #
  fancy2 "Jaheira becomes a Great Druidess:"
  ptext {
    e 'To <b>begin</b> this quest sleep in the Druid Grove, which was the arena
    <b>Jaheira</b> fought in.'
    br
    oop_a 'https://baldursgate.fandom.com/wiki/Heeding_the_Spirit_of_the_Grove',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
  }  
  fancy_spacer
  # ========================================================================== #
  # === Mazzy has challenged Gorf the Squisher:
  # ========================================================================== #
  fancy2 "Mazzy has challenged Gorf the Squisher:"
  ptext {
    oop_a 'https://baldursgate.fandom.com/wiki/Mazzy_Fentan#Quests',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    br
    oop_a 'https://baldursgate.fandom.com/wiki/Mazzy_has_challenged_Gorf_the_Squisher',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    br
    e "The quest is obtained by bringing Mazzy Fentan in front of the 
    Copper Coronet in the Slums District of Athkatla. Mazzy will 
    meet Gorf the Squisher, an aggressive ogre, and challenge 
    him to a duel in the Copper Coronet's fighting pits."
    br
    e "Inside the Copper Coronet, Bunkin can be approached and 
    asked to fetch Gorf for the fight. Next to the stairs of 
    the common room, Festule the Alchemist will sell a 
    potion to the group for 500 gold (400 with bargaining) 
    to drug Gorf. With a flattery Bunkin can then be persuaded 
    to give the potion to Gorf. Completing this optional 
    step will land 11500 XP to the group."
    br
    e 'Once Gorf and Mazzy are ready they both will be teleported
    to the small fighting pit. Mazzy will be stripped of her
    equipment and given a short sword and a small shield.
    Gorf will fight with a regular club.'
    br
    e 'Killing Gorf is worth 2500 XP and completing the quest
    is worth 5000 XP.'
    br
    e "Afterwards you can save Mazza's sister:"
    br
    e "- At some point Danno Fairfoot will appear and asks Mazzy
    to return to Trademeet to help her sister who has been
    poisoned."
    e "- Go to Trademeet and enter the Fentan home. You will
    be told that Pala drank a 'love potion' sold by
    Wallace."
    e "- Go to the Market Square in Trademeet and confront
    Wallace, the merchant. He will tell you that he got
    the potion from a young cleric named Barl."
    e "- Enter the temple of Waukeen and speak your
    concerns about Barl to Overgold Renwellyn. After
    he investigates his room, he will summon Barl and
    confront him with what he found. Barl will attack
    your group."
    e "- After the battle, Mazzy will find a potion on
    Barl's body, and you will all return to the
    Fentan home. Mazzy will use the potion on her
    sister, and Pala will be restored by the potion."
    br
    boldbr 'Reward: 31,750 XP'
  }
  # ========================================================================== #
  # === Trademeet
  # ========================================================================== #
  fancy2 "Trademeet"
  ptext {
    e 'The Djinni called Taquee has an Efreeti Bottle. The bottle can
    be pickpocketed from him.'
    br
    e 'Animal trouble in Trademeet is a side quest given by Flydian near
    the Athkatla "City Gates". He will ask the to help Trademeet
    with its animal problems. This adds the area of Trademeet
    upon the map.'
    br
    e 'Enter the basement of the house and speak to Cernd. He will
    tell the party what he knows about this and he will offer to
    join your party. In order to end this quest, you may need
    at least one druid in your party.'
    br
    e 'Now leave Trademeet and journey to the Druid Grove.'
    br
    e 'Head north and you will be confronted by a druid named
    Pauden. He will tell you that a shadow druid named Faldorn
    has taken over the grove, after the former leader of the
    druid grove, died.'
    br
    e 'Make your way through the area to the north-west
    druid circle where you will be attacked by Dalok.
    Defeat him and enter the grove.'
    br
    e 'Approach Faldorn and if you have a druid in your
    party, you can challenge her. Your druid and Faldorn
    will fight each other one-to-one without any of your
    equipment and items. There are only two quarterstaffs
    which can be picked up. Use the abilities of the druid
    to gain the advantage in this fight.'
    br
    e 'Once <b>Faldorn</b> has been defeated (the good way),
    you can take over the leadership of the grove if
    you are a level 14 druid. Otherwise, Verthan will
    assume leadership.'
    br
    e 'Return to Logan Coprith in Trademeet for
    the reward. He will also ask for your assistance
    in dealing with the genies in town. You may also
    finish that quest before this one.'
    br
    e "In the troll cave you can find The Dale's
    Protector which yields a +2 for missile weapons."
    br
    e '→ Dealing with the Trademeet genies'
    br
    e "Logan Coprith will ask your help in
    dealing with Trademeet's genie problem.
    They are cornering the market and no other
    vendor is allowed to make any sales. The
    quest can be started independently of
    Animal trouble in Trademeet."
    br
    e "Talk to Guildmistress Busya in the Mayor's
    house. She will ask you to speak with the
    Dao djinns just outside the city."
    br
    e 'Go to the Dao tent just outside the
    southeast part of Trademeet and speak to
    Khan Zahraa, the leader of the genies.
    Taquee, the Dao outside the tent, carries
    the precious Efreeti Bottle, which can
    be pickpocketed from him.'
    br
    e 'If you agree to hunt down Ihtafeer, go to
    the northeast corner of the area and talk
    with Itona, a shadow thief. She believes
    that the rakshasa killed Adratha, the
    potion seller at the Druid Grove area,
    and has taken her form.'
    br
    e "Leave the town and go to the Druid Grove,
    then enter Adratha's Cottage in the
    northeast corner of the area."
    br
    e "Defeat Ihtafeer and take her head. Return to
    Trademeet and give the head to Khan Zahraa. He
    will reward you with his sword, Rashad's Talon,
    and then leave with the other djinns. Note 
    that this means that you cannot steal the
    Efreeti Bottle from Taquee afterwards anymore."
    br
    e 'Report your success to Guildmistress Busya
    and Lord Logan Copirth and they will sculpt
    you another reward.'
    br 
    ntab 'https://baldursgate.fandom.com/wiki/Trademeet'
  }
  # ========================================================================== #
  # === Another Mission for the Temple:
  # ========================================================================== #
  fancy2 "Another Mission for the Temple:"
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Another_Mission_for_the_Temple'
    ntab 'https://baldursgate.fandom.com/wiki/Borinall%27s_House'
    br
    e 'Help "Dawnbringer Sain", who is a priest of
    the Temple of Lathander to the east of the temple
    of Helm right adjacent to the templf of Helm, in
    the very same district. Sain will ask you to
    recover the Dawn Ring.'
    br
    e 'First speak to Travin.'
    br
    e "Enter Borinall's House above the Copper Coronet and
    either swear allegiance to Talos and Borinall will
    give you the ring or kill him and take the ring from
    his body. If you're not aiding Talos and lie about
    it, your party leader will get hit by lightning, 
    inflicting minor damage, which convinces Borinall
    you're not acting in his name and this causes
    him to turn hostile."
    br
    e 'Solving this quest yields 16,250 XP and 1,000 GP.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Dragon eggs quest in Ust Natha (the drow city)
  # ========================================================================== #
  fancy2 "The Dragon eggs quest in Ust Natha (the drow city)"
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Dragon_Eggs'
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-5/quests/ust-natha-exchange-eggs.php'
    br
    e "Enter Adalon's lair on the east side of the area. She will ask you
    to retrieve her eggs which were stolen by Irenicus and Bodhi and
    in return she will help you leave the Underdark. She will transform
    your party into drow so that you can enter the city. Leave Adalon's
    lair and approach the gates of the drow city of Ust Natha. The
    gates will open and you will be questioned. Say you are Veldrin
    from Ched Nasad and you will be allowed entrance into the city."
    br
    e "Speak to Solaufein in front of the Male Fighter's Society. He
    will tell you he to talk to Imrae outside of the city, so leave
    the city, then speak to Solaufein again near the entrance to
    the city. A handmaiden will be there and will you will be
    asked to aid Solaufein in rescuing the Matron Mother's
    daughter from Mind Flayers."
    br
    e 'Thus, leave the city and go to the southeast corner of
    the Underdark. Along the way you will be ambushed by a party
    of adventurers who think you are a real drow (idiots!).'
    br
    e 'Speak to Solaufein again and he will draw the Mind
    Flayers to him. Destroy the Mind Flayers and their
    Umber Hulks.'
    br
    e 'Now return to Ust Natha and speak with Solaufin, he
    will tell you Phaere is waiting for you in the tavern.
    Enter the tavern and speak with Phaere. She will command
    you to meet her at the entrance to the city within a
    few days. Rest at the inn and then meet Phaere at the
    entrance to the city. She will tell you that she
    requires your aid in defeating a Beholder that has
    been smuggling adamantine. Go to the southeast corner
    of the city and speak to Phaere again. Destroy the
    Beholder that appears. Speak to Phaere again in the
    tavern for your next task. She will ask you to destroy
    a svirfneblin patrol to instill fear in the gnomes.'
    br
    e "Leave the city and meet Solaufein on the west
    side of the Underdark. You can either destroy
    the gnome patrol with him and take the patrol
    leader's helmet or you can convince Solaufein
    that you can do the deed yourself so he will
    return to the city and when the patrol comes
    along, spare their lives in return for the
    patrol leader's helmet. Return to Ust Natha
    and give the helmet to Phaere in the tavern
    to prove you've finished her task."
    br
    e "Meet Phaere in the Female Fighter's Society.
    She will demand that you kill Solaufein for
    her. Enter the Male Fighter's Society and
    speak to Solaufein. You can either kill him
    and take his cloak or show him mercy and he
    will give you his cloak. If you show  him
    mercy, he will not betray you, and this is
    the recommended option if you want the best
    possible rewards later on. Give the cloak
    to Phaere in the Female Fighter's Society
    and she will be pleased, inviting you to
    meet Matron Mother Ardulace in the Temple
    of Lolth."
    br
    e "If your protagonist is male, however,
    she will invite you to her bed chambers
    first and order you to sleep with her.
    You can either talk your way out of it,
    or just agree to sleep with her.
    However, if you do sleep with her and
    you are pursuing a romance:"
    br
    cmd '- Viconia will not be that bothered, since she understands the ways
    of the Drow.'
    cmd '- Jaheira will be unhappy, so you have to choose your words carefully.'
    cmd '- Aerie will NOT be happy, so your romance is effectively ruined.'
    cmd '- Dorn will be unhappy, so you have to choose your words carefully.'
    br
    e 'Note that Dorn believes you slept with her whether or
    not you did so.'
    br
    cmd "- Neera will be perturbed but insistent that she
    does not want to know what happened 'in there.'"
    br
    e 'The Dragon Eggs'
    br
    e 'Speak to Matron Mother Ardulace in the Temple of
    Lolth in Ust Natha and she will ask you to find
    some blood from a noble race.'
    br
    e "Return to the temple and give the blood to
    Matron Mother Ardulace. She will bid you to
    rest until the ritual, but Phaere will ask
    you to visit her at the Female Fighter's
    Society immediately."
    br
    e "However, in front of the Female Fighter's
    Society, Taso Kala will demand that you
    destroy a cult of another god. Go to the
    southeast corner of Ust Natha (where you 
    originally fought the beholder) and kill
    the priests and monsters, then report
    back to Tasa Kala when you are done.
    She will not give the party any reward,
    but at least she allows the party to
    enter the society again. Speak to Phaere
    inside the Female Fighter's Society and
    she will ask for your help in disposing
    Matron Mother Ardulace. Accept the offer
    to obtain the Despana Treasury Key and
    some Fake Dragon Eggs. If you accepted
    her offer, proceed to the Temple of
    Lolth. In front of the temple, Solaufein
    will appear (if he is still alive) and
    hand over some some Fake Dragon Eggs,
    to exact revenge on Phaere. Enter
    the temple and use the Despana Treasury
    Key to open the door on the east side
    and defeat the two Egg Guards."
    br
    e 'Note: If the guards go hostile and manage to talk to you,
    the ENTIRE ROOM will go hostile, thus prematurely
    ending the quest. It is better to go invisible, open
    the door, and then stealing the eggs (with or without
    replacing them) and then quickly leaving. Alternatively,
    kill the guards before they have a chance to talk to
    you. Spells like Time Stop make this easier.'
    br
    e 'Once you loot the Real Dragon Eggs, the
    Golem Guards will attack you, so kill them.
    At this point, the best option is as follows:'
    br
    e "Betraying Ardulace: Replace the Real Eggs with
    Phaere's Fake Dragon Eggs, then return to Phaere
    and give her the Real Dragon Eggs. She will be
    happy and you will receive 10,000 XP, before
    telling you that the ritual will start very
    soon. Same as above, Adalon's Imp will appear,
    urging you to leave the city before the ritual's
    demon exposes your disguise, and then a short
    while later you get summoned to the ritual."
    br
    e "Whatever your choice is, assuming the guards are
    not hostile yet, leave 
    the city of Ust Natha quickly before the alarm goes out that you were 
    responsible for the matron mother's death and return the Real Dragon 
    Eggs to Adalon. Be prepared before talking to her because after the 
    conversation, she will teleport you immediately to a middle of a 
    battle. She will reward you with Necaradan's Crossbow +3, 78,500 XP 
    for each party member, and transform your party back to your true 
    forms, before finally honoring the agreement to teleport you near 
    the surface. Once she teleports you, you will be in the middle of 
    a battle so kill all the enemies (Adalon will be helping you) and 
    then enter the ruins and help the elves fight the drow. On the 
    west side of the area is the exit from the Underdark."
  }
  fancy_spacer
    # ========================================================================== #
  # === (50) Tactics remix mod                                  (tactics tag)
  #
  # Tactics remix was written by morpheus562.
  #
  # Last release:          08.11.2023
  # Last upstream release: Remix v0.6.2 Beta
  # mkdir 50_tactics-remix-v0.8-beta-released-on-08.05-2024
  # ========================================================================== #
  # https://github.com/Gibberlings3/Tactics-Remix
  # https://github.com/Gibberlings3/Tactics-Remix/releases
  # https://www.morpheus-mart.com/tactics-remix
  # https://www.dropbox.com/scl/fi/ac74savjvfqbg2981vfrl/Tactics-Remix.zip?rlkey=gzvs3a48evwpsjpn25pnytp7l&st=6rrczbx7&dl=0
  # ========================================================================== #
  fancy_h1('The Tactics remix mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    # ======================================================================== #
    # === Kuroisan
    # ======================================================================== #
    e 'The Tactics remix mod adds <b>Kuroisan</b> as well as <b>Gebhard
    Blucher</b> (and more), a lich in the Docks. Gebhard can be found
    <b>to the north</b> of the main Shadow Thief guildhouse entrance.'
    br
    # ======================================================================== #
    # === Red Badge
    # ======================================================================== #
    e "The <b>Red Badge</b> Poison-Based Encounter is triggered if the main
    actor has more than 3 million XP, has either killed Gromnir or be in SoA,
    and is standing outside of Watcher's Keep."
    br
    # ======================================================================== #
    # === The Ritual
    # ======================================================================== #
    e "In <b>The Ritual</b> the party has to ultimately kill the dragon
    called <b>Pontifex</b>. <b>Level 9 spells</b> help a lot here - or the
    equivalent scrolls. To defeat Pontifex himself one may need the
    <b>True Sight</b> spell. Also multiple mages casting time stop can be
    of immense help. Spell Trigger - set it via Lower Resistance - helps
    as well, and then attacks via Skull Traps, Magic Missiles, as well as
    Melf's Acid Arrows and ADHWs. Note that Stoneskin can stop Wing buffet.
    Mirror Image can also prevent the breath attack. Protection from Magical
    Weapons also helps, so you can put Jan close to him. Jan can also use
    <b>Carsomyr</b>. Furthermore, feeblemind may be useful in this
    fight."
    br
    e 'Discussion at the BG2 website:'
    br
    primary_link 'https://forums.beamdog.com/discussion/87668/tactics-remix'
    primary_link 'https://github.com/Gibberlings3/Tactics-Remix'
    primary_link 'https://www.morpheus-mart.com/' 
  }
  fancy_spacer
  # ========================================================================== #
  # === (38) Heart of the wood                                     (heart tag)
  #
  # Latest release: 04.06.2020
  # Latest version: 7.0
  #
  # mkdir 38_Heart_of_the_wood_v7.0_released_on_04.06.2020; cd 38_Heart_of_the_wood_v7.0_released_on_04.06.2020
  # wget https://github.com/SpellholdStudios/HeartOfTheWood/releases/download/v7.0.0/heart-of-the-wood-7.0.0.zip
  # ========================================================================== #
  # https://github.com/SpellholdStudios/HeartOfTheWood/releases
  # ========================================================================== #
  fancy_h1('Heart of the wood') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The latest release occurred on 04.06.2020.'
    br
    primary_link 'http://www.shsforums.net/topic/60821-heart-of-the-wood-updated-to-v700-ee-compatible/'
    primary_link 'https://github.com/SpellholdStudios/HeartOfTheWood/releases'
  }
  fancy_spacer
  # ========================================================================== #
  # === (38) Forgotten Armament                                (Armament tags)
  #
  # Latest version:    4.4
  # Latest release on: 26.06.2024
  #
  # mkdir 38_Forgotten_Armament_v4.4_released_on_26.06.2024; cd 38_Forgotten_Armament_v4.4_released_on_26.06.2024
  # ========================================================================== #
  # https://www.gibberlings3.net/files/file/1036-forgotten-armament/
  # https://www.weaselmods.net/showthread.php?tid=1739
  # https://www.gibberlings3.net/forums/topic/33924-forgotten-armament-v01-beta/
  # ========================================================================== #
  fancy_h1('Forgotten Armament') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The latest release occurred on 26.06.2024, version 4.4.'
    br
    primary_link 'https://www.gibberlings3.net/files/file/1036-forgotten-armament/'
    primary_link 'https://www.morpheus-mart.com/forgotten-armament'
  }
  # ========================================================================== #
  # === (08) A Mod for the Orderly v7                            (orderly tag)
  #
  # Last updated: 02.08.2020
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"A Mod for the Orderly v7 (last release in 02.08.2020)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "This mod adds a keyring to help manage the avalanche of keys the player
    acquires during the course of the game."
    br
    e "The keyring can be found in the <b>northeastern part of the Slums</b>,
    near the Archway, after a quest. It can also be purchased from <b>Jahaboam
    at the Docks</b> (the merchant that also sells the Keepsake Locket),
    <b>Mira</b> at Waukeen's Promenade or the peddler from Trademeet (once
    you fix up Trademeet's druid and djinn problems). In ToB it can be
    bought from Karthis al-Hezzar in the North Forest."
    br
    e 'This mod works fairly well - I have not encountered any problems,
    probably due to its small size.'
    br
    e 'The mod is described in more detail here:'
    br
    primary_link 'https://gibberlings3.github.io/Documentation/readmes/readme-cliffkey.html'
    br
    the_mod_can_be_downloaded_from(
      'https://www.gibberlings3.net/files/file/702-a-mod-for-the-orderly/'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (49) Afaaq, the Djinni Companion                           (Afaaq tag)
  #
  # Last official update: 10.03.2024
  # Latest version:       2.10
  #
  # mkdir 49_Afaaq_the_Djinni_Companion_v2.10_released_on_10.03.2024; cd 49_Afaaq_the_Djinni_Companion_v2.10_released_on_10.03.2024
  # wget https://github.com/Argent77/DjinniCompanion/releases/download/v2.10/win-A7-DjinniCompanion-v2.10.zip
  # ========================================================================== #
  # https://github.com/Argent77/DjinniCompanion
  # https://github.com/Argent77/DjinniCompanion/releases
  # https://forums.beamdog.com/discussion/41108/mod-afaaq-the-djinni-companion-for-bg2-and-bg2-ee-released/p1
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Afaaq, the Djinni Companion') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e '<b>Afaaq, the Djinni Companion</b> - he can be the seventh
    companion.'
    br
    e "One way to solve the djinni's quest is by invading <b>House Arabani</b>. In
    order to do so, a wardstone is needed - possibly the one from the nearby house.
    Possibly containers have the wardstone, too."
    br
    e 'There is also someone called <b>Adratha</b>.'
    br
    can_be_downloaded_from(
      'https://argent77.github.io/DjinniCompanion/index.html',
      'https://github.com/Argent77/DjinniCompanion',
      'https://github.com/Argent77/DjinniCompanion/releases'
    )
  }
  fancy_spacer
  fancy_spacer
  # ========================================================================== #
  # === (49) Afaaq, the Djinni Companion                           (Afaaq tag)
  #
  # Last official update: 10.03.2024
  # Latest version:       2.10
  #
  # mkdir 49_Afaaq_the_Djinni_Companion_v2.10_released_on_10.03.2024; cd 49_Afaaq_the_Djinni_Companion_v2.10_released_on_10.03.2024
  # wget https://github.com/Argent77/DjinniCompanion/releases/download/v2.10/win-A7-DjinniCompanion-v2.10.zip
  # ========================================================================== #
  # https://github.com/Argent77/DjinniCompanion
  # https://github.com/Argent77/DjinniCompanion/releases
  # https://forums.beamdog.com/discussion/41108/mod-afaaq-the-djinni-companion-for-bg2-and-bg2-ee-released/p1
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Afaaq, the Djinni Companion') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Find Valygar Corthala, the bounty hunter, then travel in
    the sphere:'
    br
    e "Valygar's servant has some info if you pretend to be a
    friend, or just search upstairs for Corthala Tax Notice which
    gives you the same clue revealing the man's property is in
    the Umar Hills area. He may, however had, also be upstairs
    in his house in the Docks or there may be a <b>tax notice</b>
    there - depending on some mods, most likely. This tax
    notice can then be shown to Llarsh, in the Council of
    Six Building in the Government district."
    br
    e "Valygar's Cabin is located northwest of the Umar Hills maps,
    he has some goons outside his house. You can either fight them,
    or tell them that you aren't here to hurt their master if
    you are not looking for a fight."
    br
    e 'In his house, <b>Valygar</b> tells the party that he killed
    the Cowled Wizards out of self-defense because they needed him,
    dead or alive, to open up the Planar Sphere, which was created
    by his ancestor, a lich named Lavok and Valygar would like
    to remove him, with your help.'
    br
    e 'The correct order to activate the runes in the sphereis:'
    br
    cmd 'Top, Bottom, Right, Left.'
    br
    e 'Or: <b>Northeast</b>, <b>Southwest</b>, <b>Southeast</b>,
    <b>Northwest</b>, if one wishes to look at it like a compass.'
    br
    e 'Completing the puzzle awards the party with 24,500 XP and
    grants access to the <b>Sphere Core</b> via the stairway to
    the South.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Lavok%27s_Sphere'
    ntab 'https://baldursgate.fandom.com/wiki/Inside_the_Planar_Sphere'
    ntab 'https://baldursgate.fandom.com/wiki/Valygar_Corthala#Quests'
  }
  fancy_spacer
  # ========================================================================== #
  # === (11) Wares of the Planes                                   (wares tag)
  #
  # Last official version:  1.3
  # Last official update:   15.07.2024
  #
  # mkdir 11_Wares_of_the_Planes_v1.3_released_on_15.07.2024; cd 11_Wares_of_the_Planes_v1.3_released_on_15.07.2024
  # wget https://github.com/Argent77/A7-WaresOfThePlanes/releases/download/v1.3/win-A7-WaresOfThePlanes-v1.3.zip
  # ========================================================================== #
  # https://github.com/Argent77/A7-WaresOfThePlanes
  # https://github.com/Argent77/A7-WaresOfThePlanes/releases
  # https://github.com/Argent77/A7-WaresOfThePlanes/releases/tag/v1.2
  # wget https://github.com/Argent77/A7-WaresOfThePlanes/releases/download/v1.2/win-A7-WaresOfThePlanes-v1.2.zip
  # mkdir 18_Wares_of_the_Planes-v1.3-released-on-15.07.2024
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Wares of the Planes') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "This mod imports a large number of items from the Planescape universe
    to the Baldur's Gate series and makes them available by a unique merchant."
    br
    can_be_downloaded_from(
      'https://github.com/Argent77/A7-WaresOfThePlanes'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === (11) Anishai the NPC monk
  #
  # Last official update: 
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Anishai the NPC monk') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Anishai the NPC monk can be found in Mae'Var's guildhouse."
    br
    can_be_downloaded_from(
      'https://www.gibberlings3.net/files/file/687-anishai-one-day-npc/'
    )
  }
  # ========================================================================== #
  # === (34) Will of the Wisps                           (wisps tag, wisp tag)
  #
  # Last update:    17.10.2024
  # Latest version: 3.01
  #
  # mkdir 34_Will_of_the_Wisps_v3.01_released_on_17.15.2024; cd 34_Will_of_the_Wisps_v3.01_released_on_17.15.2024
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/will-of-the-wisps/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Will of the Wisps mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'In the <b>Will of the Wisps</b> quest the protagonist has to find a
    thief who has ashes. These <b>ashes</b> then have to be placed in the ruined
    temple area - the one were the werewolf could be found.'
    br
    e 'The latest version is <b>3.0</b>.'
    br
    primary_link 'https://forums.beamdog.com/discussion/61754/mod-will-of-the-wisps-shamanic-enhancements'
    primary_link 'https://www.weaselmods.net/showthread.php?tid=28'
    primary_link 'https://downloads.weaselmods.net/download/will-of-the-wisps/'
  }
  # ========================================================================== #
  # === Tales of Anegh                                             (anegh tag)
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#tales_of_anegh_last_update__version_3
  # ========================================================================== #
  # https://www.baldurs-gate.de/index.php?resources/tales-of-anegh.14/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Tales of Anegh (Last update: <b>09.03.2018</b>, 
            Version <b>3</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/T1Ni7Ac.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_mod_tales_of_anegh'; drag_for :drag_bg2_mod_tales_of_anegh
  ptext {
    e 'In Tales of Anegh a mysterious mage asks for your help to defend the
    town of Anegh from an invasion by a horde of half-breed monsters. But
    how did the monsters get here, and what is the mage really up to?'
    br
    e "Some side quests can be solved in Tales of Anegh. For instance, Emir's
    Pipe can be brought to Emir, in the second tent from the left."
    br
    e "Barfets Hammer can be given to Barfet in the third tent from the left,
    after freeing the villagers. Most of these subsequent side quests require
    that the villagers have been freed."
    br
    e 'For more discussion about the <b>Tales of Anegh</b> mod, see:'
    br
    primary_link 'http://www.shsforums.net/topic/42996-tales-of-anegh/'
    primary_link 'https://forums.beamdog.com/discussion/76089/mod-spotlight-tales-of-anegh'
    br # === Walkthrough for "Tales of Anegh"
    e 'A walkthrough in german can be seen here:'
    br
    primary_link 'https://www.baldurs-gate.de/index.php?resources/tales-of-anegh-komplettl%C3%B6sung.26/'
    br
    the_mod_can_be_downloaded_from(
      'https://www.baldurs-gate.de/index.php?resources/tales-of-anegh.14/'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === (06) Evandra                                            (evandra tag)
  #
  # Last official update: 
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Evandra (NPC) (Last Updated: )') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e '<b>Evandra</b> is a <b>True Neutral elven illusionist</b>, and for
    those familiar with the Dragonlance setting, a Red Robed Wizard of
    High Sorcery.'
    br
    e 'Given her elven background, her alignment in some senses represents a
    fall - a significant departure from what she had at one point expected
    out of life.'
    br
    e 'Evandra can be found inside the Planar Sphere prior to Chapter 4,
    trapped with the Knights of Solamnia. She is <b>immediately
    recruitable</b>.'
    br
    primary_link 'https://www.gibberlings3.net/mods/npcs/evandra/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (08) Navarra the NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Navarra the NPC") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Navarra is a NPC. She can be found in the Den of seven vales,
    towards the back.'
  }
  fancy_spacer
  # ========================================================================== #
  # === (40) The Item Upgrade Mod                                (ItemUpgrade)
  #
  # This is the mod by Westley Weimer.
  #
  # Last update:    30.12.2023
  # Latest version: 52
  #
  # mkdir 40_The_Item_Upgrade_Mod_v52_released_on_30.12.2023; cd 40_The_Item_Upgrade_Mod_v52_released_on_30.12.2023
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#every_mod_and_dog_v11_by_cliffette_last_release_in_03_01_2021
  # ========================================================================== #
  # https://github.com/Pocket-Plane-Group/Item_Upgrade
  # https://github.com/Pocket-Plane-Group/Item_Upgrade/releases/
  # https://github.com/Pocket-Plane-Group/Item_Upgrade/releases/download/v52/itemupgrade-v52.exe
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'The Item Upgrade Mod (Last official release: 
  <b>30.12.2023</b>, Last Version: <b>52</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>Item Upgrade mod</b> allows Cromwell and Cespenar to upgrade
    additional items in BGII.'
    br
    e 'Discussion in the Beamdog-Forum about the Item Upgrade Mod:'
    br
    primary_link 'https://forums.beamdog.com/discussion/64762/weimers-item-upgrade-mod'
    br
    the_mod_can_be_downloaded_from(
      'https://weidu.org/Weimer-ItemUpgrade-v40.exe',
      'https://weidu.org/c2/README-ItemUpgrades.txt',
      'https://github.com/Pocket-Plane-Group/Item_Upgrade'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (47) Ascalon's questpack                                 (ascalon tag)
  #
  # Last release: 04.12.2023
  # Version:      5.2
  #
  # mkdir 47_Ascalons_questpack_v5.2_last_published_on_04.12.2023; cd 47_Ascalons_questpack_v5.2_last_published_on_04.12.2023
  # wget https://github.com/Gitjas/Ascalons_Questpack/releases/download/v5.2/ascalons-questpack-5.2.zip
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/69160/mod-ascalons-questpack-kerzenburgforum
  # https://github.com/Gitjas/Ascalons_Questpack
  # https://github.com/Gitjas/Ascalons_Questpack/releases/tag/v5.2
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Ascalon's questpack") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/j7ouwim.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_ascalons_questpack_mod'
  ptext {
    e "Ascalon's questpack: latest version is <b>5.2</b>."
    br
    e 'Discussion about the mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/69160/mod-ascalons-questpack-kerzenburgforum'
    br
    the_mod_can_be_downloaded_from('https://github.com/Gitjas/Ascalons_Questpack')
  }
  fancy_spacer
  # ========================================================================== #
  # === (45) Fishing for Trouble                    (fishing tag, trouble tag)
  #
  # Last upstream release: 29.01.2024
  # Version:               3.2.10
  #
  # mkdir 45_Fishing_for_Trouble_mod_v3.2.10_released_on_29.01.2024; cd 45_Fishing_for_Trouble_mod_v3.2.10_released_on_29.01.2024
  # wget https://github.com/InfinityMods/FishingForTrouble/releases/download/v3.2.10/fishing-for-trouble-v3.2.10.zip
  # ========================================================================== #
  # https://github.com/InfinityMods/FishingForTrouble/releases/
  # https://github.com/InfinityMods/FishingForTrouble/releases/download/v3.2.10/fishing-for-trouble-v3.2.10.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Fishing for Trouble (Last update: 
  <b>29.01.2024</b>, version <b>3.2.10</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/j7ouwim.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_mod_fishing_for_trouble'
  ptext {
    e 'The <b>Fishing for Trouble mod</b> adds four new major locations, and a
    long quest-line to tie them all together. The first area is an additional
    district in Athkatla, in the government district westside.'
    br
    e 'The quest begins by Lief Torman requesting the main actor to deliver
    a letter to <b>Elminster</b>. Elminster can be found in Trademeet, near
    the fountain.'
    br
    e 'After visiting the Demon in the lighthouse, one has to travel to
    the <b>Government West</b> district of Athkatla, and talk to
    <b>Ceinwen Ravenhair</b> in her house.'
    br
    e '<b>Cerendor Hold</b> is the fortress that <b>guards the path into the
    Cloudpeak Mountains</b>. The protagonist can talk to <b>Countess
    Wultheof</b> on the third floor of the hold for the <b>Food Thief
    Quest</b>.'
    br
    the_mod_can_be_downloaded_from(
      'https://forums.beamdog.com/discussion/79451/mod-spotlight-fishing-for-trouble/p1',
      'http://www.spellholdstudios.net/ie/fft',
      'https://github.com/InfinityMods/FishingForTrouble/releases/download/v3.2.8/fishing-for-trouble-v3.2.8.zip',
      'https://github.com/InfinityMods/FishingForTrouble/releases/'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === Made in Heaven - Item Pack Mod                            (Heaven tag)
  #
  # Last update:    19.12.2022
  # Latest version: 7
  #
  # mkdir 12_Made_in_Heaven_Item_Pack_Mod_v7_released_on_19.12.2022
  # wget https://github.com/AngelGryph/MadeInHeaven_ItemPack/releases/download/v7/mih_ip-v7.zip
  # ========================================================================== #
  # https://github.com/AngelGryph/MadeInHeaven_ItemPack
  # https://github.com/AngelGryph/MadeInHeaven_ItemPack/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Made in Heaven - Item Pack Mod 
  (Last update: <b>17.12.2022</b>, Version: <b>7</b>)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Made in Heaven - Item Pack. This mod contains items such as the
    <b>Mirror of Illusions</b> or the <b>Brooch of Shielding</b>.'
    br
    e 'The mod may also install some quests and new monsters.'
    br
    pre "mh#amul1 Amulet against Undead   Temple of Lathander (shop)
mh#amul2 Necklace of Prayer Beads         Temple of Lathander (shop)
mh#amul3 Gem of Insight                   Temple of Oghma (shop)
mh#amul5 Brooch of Shielding              Druid Grove (battle)
mh#amul6 Scarab versus Golems             Adventurer's Market (shop)
mh#amul8 Medallion of Faith               Chateau Irenicus (import)

mh#belt1 Girdle of Dwarvenkind            Chateau Irenicus (chest)
mh#belt2 Sunite Sash                      Vaelasa (event or battle)
mh#belt3 Storm's Garter                   Harper Hold (battle)

mh#boot1 Boots of the Master Ninja        Mae'var Guildhouse (battle)
mh#boot2 Boots of Striding and Springing  Firkraag's Lair (battle)
mh#boot3 Boots of Balance                 Slaver Stockade (battle)

mh#brac1 Vambraces of Evil's Warding      Chateau Irenicus (import)
mh#brac2 Gauntlets of the Dwarven King    Chateau Irenicus (import)
mh#brac3 Bracers of Winter's Chill        Therndle Daglefodd (event)
mh#brac5 Gauntlets of Smiting             Bridge District (battle)
mh#brac9 Gloves of Thievery               Chateau Irenicus (import)

mh#btax1 Foesplitter +1                   Maheer (shop)
mh#btax3 Redethemar +4                    Tree of Life (container)
mh#btax4 Might of Heroes +3               Trademeet Merchant (shop)

mh#bull1 Priest's Bullet                  Various Temples (shop)
*mh#bull2 Bullet of Pulverizing +1        ???

mh#chan1 Eversing +2                      Arnolinus the dwarf (shop)

mh#clck1 Mutamin's Cloak                  Trademeet Merchant (shop)
mh#clck3 Cloak of Arachnida               Ust Natha (shop)
mh#clck5 Bolder's Cloak of the Rogue      Twisted Rune (battle)
mh#clck7 Cloak of Lathander               Temple of Lathander (shop)
mh#clck8 Cloak of Flame                   Planar Sphere (battle)
mh#clck9 Battlecloak of Vycaena           Firkraag (battle)

mh#comp6 Black Dragon Scales          Suldanessenar (battle)

mh#dagg1 Catclaw +3                   Mae'var Guildhouse (battle)
mh#dagg3 Golemblight +2               Trademeet Merchant (shop)

mh#dart1 Lein's Fiery Darts +2        Planar Sphere (chest)
mh#dart2 Chandler's Icy Darts +2      Planar Sphere (chest)

mh#drag1 Black Dragon Scale           Cromwell (forging)

mh#flai1 Slimecrusher +1              Maheer (shop)

mh#helm1 Helm of Valor                D'Arnise Keep (chest)
mh#helm2 Helm of the Dwarven Lords    Adventurer's Market (ch6)

mh#hide1 Winter Wolf Hide +1          Chateau Irenicus (battle)
mh#hide1 White Skin of Umpluutu       Windspear Hills (battle)

mh#ioun3 Bright Orange Ioun Stone     Adventurer's Market (shop)
mh#ioun4 Telkiira                     Suldanessenar (battle)
mh#ioun5 Mottled Green Ioun Stone     Harper Stronghold (battle)
mh#ioun6 Maroon Star Ioun Stone       Bridge District (battle)
mh#ioun7 Blood of Lathander           Temple of Lathander (event)

mh#lbow1 Bow of Eletha                Trademeet Merchant (shop)

mh#mace1 Radiant Star +1              Maheer (shop)
*mh#mace2 Heaven's Wrath +4           Underdark (event)
*mh#mace3 Skull Mace +2               ???

mh#misc1 Pearl of Power               Trademeet Merchant (shop)
mh#misc2 Bag of Tricks                Druid Grove (battle)
mh#misc3 Crystal Ball                 Adventurer's Market (shop)
mh#misc5 Horn of Goodness/Evil        Waukeen's Wares (shop)
mh#misc6 Bottle of Pleasant Odors     Mira (shop)

mh#plat3 Laeral's Storm Armor +2      Adventurer's Market (ch6)
mh#plat4 Plate of Solamnus +5         Adventurer's Market (ch6)

mh#potn1 Oil of Acid Resistance      (various potion shops)
mh#potn2 Potion of Clairvoyance      (various potion shops)
mh#potn4 Oil of Disenchantment       (various potion shops)
mh#potn5 Potion of Longevity         (various potion shops)
mh#potn6 Alchemist's Fire            Adventurer's Market (shop)
mh#potn7 Acid Flask                  Adventurer's Market (shop)
*mh#potn8 Elixir of Life             ???

mh#ring2 Ring of Warmth              Chateau Irenicus (import)
mh#ring3 Ring of the Neophyte        Chateau Irenicus (import)
mh#ring4 Ring of White Bone          Temple Ruins (werewolf cave)
mh#ring5 Ring of Mind Shielding      Ust Natha (shop)
mh#ring6 Ring of Shooting Stars      Suldanessenar (shop)
mh#ring8 Ring of Armory              Chateau Irenicus (import)
mh#ring9 Ring of Water Control       Adventurer's Market (shop)

mh#robe1 Robe of the Elements        Firkraag's Lair (battle)
mh#robe2 Robe of the Necromancer     Ust Natha (shop)
mh#robe3 Robe of the Pure Heart      Temple of Lathander (shop)
mh#robe4 Shadow Dancer's Robe        Ust Natha (shop)

mh#scrl1 Scroll of Heal              Temple of Lathander (shop)
mh#scrl2 Scroll of Resurrection      Temple of Lathander (shop)

mh#shld3 Shield of the Phoenix +2    D'Arnise Keep (chest)
mh#shld9 Shield of the Dragonslayer +3    Adventurer's Market (ch6)

mh#staf1 Staff of Rumathil           Planar Sphere (battle)
mh#staf5 Staff of Water +2           Adventurers Market (shop)

mh#swrd1 Terminus Est +2             Trademeet Merchant (shop)
mh#swrd2 Smythe's Slicer +1          Maheer (shop)
mh#swrd4 Planar Sword +1             Planar Sphere (controls)
mh#swrd9 Holy Sword +2               Chateau Irenicus (import)

mh#wand1 Wand of Illusions           Planar Sphere (chest)

"
    br
    primary_link 'https://github.com/AngelGryph/MadeInHeaven_ItemPack'
    primary_link 'https://github.com/AngelGryph/MadeInHeaven_ItemPack/releases'
  }
  fancy_spacer
  # ========================================================================== #
  # === (18) Zakrion, a NPC (a true neutral Human Duelist)
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#zakrion
  # ========================================================================== #
  # https://www.gibberlings3.net/mods/npcs/zakrion/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Zakrion, a NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e '<b>Zakrion</b> can be found in the Docks district.'
    br
    primary_link 'https://www.gibberlings3.net/mods/npcs/zakrion/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (18) Beaurin Legacy v5.2.1
  #
  # This mod was last updated upstream on the 19.06.2022.
  #
  # mkdir 18_Beaurin_Legacy_Mod_v5.2.1_released_on_the_19.06.2022; cd 18_Beaurin_Legacy_Mod_v5.2.1_released_on_the_19.06.2022
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#tangled_oak_isle
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Beaurin Legacy  (Last update: <b>23.06.2023</b>)',
           id: 'tangled_oak_isle') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Beaurin Legacy is about an elven Enchanter/Thief and a hidden
    NPC to BGII:SoA & ToB and BGII:EE.'
    br
    e '<b>Minyae Beaurin</b> can be found outside of the Crooked Crane
    in the City Gates.'
    br
    e 'The mod includes custom portraits, a friendship track for
    both Minyae and the Hidden NPC, numerous banters and
    interjections, encounters and quest(s), voicing for
    both NPCs, a romance with a Bioware NPC, player-initiated
    dialogues, and custom friendship track themes.'
    br
    e 'If you killed the lich within the Crooked Crane, her initial quest
    is finished.'
    br
    e 'The webforum holds discussions about this MOD:'
    br
    primary_link 'https://www.gibberlings3.net/forums/forum/200-the-beaurin-legacy/'
    br
    can_be_downloaded_from(
      'https://www.gibberlings3.net/mods/npcs/beaurin/'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (32) DAWAP mod
  # ========================================================================== #
  # https://github.com/Deratiseur/DAWAP
  # https://github.com/Deratiseur/DAWAP/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'DAWAP mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'DAWAP'
    br
    e '34 Spellcasters kits that will make you revise the way you
    play.'
    br
    primary_link 'https://github.com/Deratiseur/DAWAP'
  }
  fancy_spacer
  # ========================================================================== #
  # === (24) lichdom mod                                         (Lichdom tag)
  #
  # Last update:  28.09.2024
  # Last version: v1.3.1
  #
  # mkdir 27_Lichdom_Mod-v1.3.1-released-on-27.09.2024; cd 27_Lichdom_Mod-v1.3.1-released-on-27.09.2024
  # wget https://github.com/LCA-EET/Lichdom/releases/download/v1.3.1/Install_Lichdom.zip
  # ========================================================================== #
  # https://github.com/LCA-EET/Lichdom
  # https://github.com/LCA-EET/Lichdom/releases
  # https://forums.beamdog.com/discussion/88122/lichdom-for-bg2ee-eet-merry-lichmas
  # wget https://github.com/LCA-EET/Lichdom/releases/download/v1.1/Install_Lichdom.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Lichdom mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Lichdom Mod features a new NPC, called Morris.'
  }
  fancy_spacer
  
  fancy_spacer
  # ========================================================================== #
  # === (26) Golden-Horse
  #
  # Last official update: 04.10.2024
  # Version:              1.8e
  #
  # wget https://github.com/Spellhold-Studios/Golden-Horse/releases/download/v1.8e/golden-horse-1.8e.zip
  #
  # mkdir 26_Golden_Horse_v1.8e_released_on_04.10.2024; cd 26_Golden_Horse_v1.8e_released_on_04.10.2024
  # wget https://github.com/Spellhold-Studios/Golden-Horse/releases/download/v1.8e/golden-horse-1.8e.zip
  # ========================================================================== #
  #
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Golden Horse') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e ''
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (26) Alabaster Sands                                   (alabaster tag)
  #
  # Last official update: 09.05.2024
  # Version:              1.7
  #
  # mkdir 26_Alabaster_Sands_v1.7-released-on-09.05.2024; cd 26_Alabaster_Sands_v1.7-released-on-09.05.2024
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/alabaster-sands/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Alabaster Sands (Last Updated: 09.05.2024)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Alabaster Sands is about Djinni - a small quest mod from the
    Athkatlan Grounds quest mod series, which adds new areas and
    quests to Shadow of Amn's main city location. There is one
    main quest, and a few smaller ones, all oriented around the
    titular area, which is nothing else but Athkatla's public
    beach. So visit the place, help those you'll meet there,
    and see this brand new part of the City of Coin."
    br
    e "The mod adds 7 new quests that introduce new characters, items,
    and item graphics. These quests include the artist <b>Yhe</b>, the
    <b>sirine</b>, the <b>chicken quardian</b>, <b>Mr O'Possum</b> and
    <b>the missing bell</b>. The other two quests can be found outside
    the District - there is a woman on the lower left corner of
    Waukeen's Promenade that sends you to Alabaster Sands, giving you
    the purpose to visit the Sands for the first time."
    br
    e "Then, there is also a secret quest that appears only for ~3
    hours per day, close to midnight. Finally, not a quest, but you
    should visit the guard's tent every few days during the night
    to see how their relationship grows. Not a quest, but a
    heartwarming set of encounters."
    br
    e 'There is a <b>chicken quest</b> as well. One can check behind the tent, to
    see that there is something new there - a <b>dog</b> guardian.'
    br
    e 'The <b>Yhe</b> quest can be solved by making gem dust and then fetching
    some oil from Mira or another merchant.'
    br
    e '<b>Alabaster Sands Mod</b> can be downloaded from:'
    br
    primary_link 'https://downloads.weaselmods.net/download/alabaster-sands/'
  br;}
  fancy_spacer
  # ========================================================================== #
  # === (23) THE JOURNEY TO THE WHIN HILL         (Whin Hill tag, journey tag,
  #                                                Whin tag)
  #
  # Last official update: 23.04.2024
  # Last version:         1.3
  #
  # mkdir 14_The_Journey_to_the_Whin_Hill_v1.3_released_on_23.04.2024; cd 14_The_Journey_to_the_Whin_Hill_v1.3-23.04.2024
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/the-journey-to-the-whin-hill/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Journey to the Whin Hill "\
           "(Last official update: <b>05.07.2023</b>)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>Whin Hill</b> is known to be a home for wyverns.'
    br
    e 'The statue can become <b>Afu</b>, a cleric, via a <b>stone to
    flesh scroll</b>.'
    br
    e 'Killing the dragon will yield <b>copper scales</b>.'
    br
    e 'Discussion can be found here:'
    br
    primary_link(
      'https://forums.beamdog.com/discussion/86905/mod-the-journey-to-the-whin-hill'
    )
    br
    download_the_mod_from('
      https://downloads.weaselmods.net/download/the-journey-to-the-whin-hill/
    ')
  }
  fancy_spacer
  # ========================================================================== #
  # === OF HEIRLOOMS AND CLASSES
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/of-heirlooms-and-classes/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Of heirlooms and classes') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The items can be found here, respectively:'
    br
    pre "
MAGE'S ITEM:

A) Firkraag Entrance Area
B) Sea's Bounty - secret chamber

CLERIC'S ITEM:

A) Mae'Var's Inn Basement
B) Temple of Talos

WARRIOR'S ITEM:

A) Marella's Body
B) Temple of the Forgotten God

RANGER'S ITEM:

A) Planar Sphere
B) Kobold Shaman (Sewers under the Copper Coronet)

PALADIN'S ITEM:

A) Path to the Ghoul village (The Unseeing Eye Quest)
B) Temple Ruins (Interior)

DRUID'S ITEM:

A) Druid Gove - Store Tower

MONK'S ITEM:

A) Tanner's Bedroom
B) Mekrath's Library

SHAMAN'S ITEM:

A) Trademeet Tomb 
B) TorGal

SORCERER'S ITEM:
A) Firkraag's Dungeon
B) Twisted Rune

THIEF'S ITEM:

A) Slums - Bregg
B) Neb

BARD'S ITEM:
A) Harpers' Headquaters"
    primary_link 'https://downloads.weaselmods.net/download/of-heirlooms-and-classes/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (12) Heroes, Thieves and Moneylenders   (Moneylenders tag, heroes tag)
  #
  # Last upstream release: 10.08.2024
  # Last upstream version: 4.5
  #
  # mkdir 12_Heroes_Thieves_and_Moneylenders-4.5-released-on-10.08.2024
  # wget https://github.com/Austin-BG/HTaM/releases/download/v.4.5/heroes-thieves-and-moneylenders-4.5.zip
  # ========================================================================== #
  # https://github.com/Austin-BG/HTaM/releases
  # https://github.com/Austin-BG/HTaM/releases/tag/v.4.4.1
  # wget https://github.com/Austin-BG/HTaM/releases/download/v.4.4.1/heroes-thieves-and-moneylenders-4.4.1.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Heroes, Thieves and Moneylenders (Last official upstream 
            release: <b>10.08.2024</b>, 
            Version <b>Version 4.5</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/HNW7880.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_mod_heroes_thieves_and_moneylenders'; drag_for :drag_bg2_mod_heroes_thieves_and_moneylenders
  ptext {
    e 'This interesting mod adds a <b>bank</b> to Athkatla, as well
    as several quests.'
    br
    e 'The bank allows the party to open an account, deposit money, let it
    accrue interest, and make withdrawals. It can be found in the
    <b>Waukeen Promenade</b>, in the bottom right corner.'
    br
    e 'There are quests related to the bank, quests related to the thieves
    guild (including an <b>Aran Linvail</b> romance), and other quests (including
    a detective quest about a missing circus troll). Some of them lead to
    beautiful new maps.'
    br
    anm 'Note that the quest in regards to the location of the bank
    may be bugged.'
    brbr
    e 'Discussion about this mod can be found at the beamdog-forums,
    such as here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/81464/mod-heroes-thieves-and-moneylenders-banter-quest-romance-mod-for-bg2'
    br
    the_mod_can_be_downloaded_from(
      'https://www.gibberlings3.net/mods/quests/htam/',
      'https://github.com/Austin-BG/HTaM',
      'https://github.com/Austin-BG/HTaM/releases',
      'https://github.com/Austin-BG/HTaM/releases/download/v.4.2.6/heroes-thieves-and-moneylenders-4.2.6.zip'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === (26) Skie the cost of one girl
  #
  # Last update: 
  # ========================================================================== #
  # https://www.weaselmods.net/showthread.php?tid=29
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Skie, the NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Skie can be found in a pub, in Athkatla.'
    br
    e 'A new merchant can be found near Lord and Lady Ophal.'
    br
    e 'The Return of Eddard Silvershield starts in the <b>Bridge
    District</b>. Skie will notice a man she knows, then the
    party has to viisit man in a house he is using, and then
    the party will meet his contact behind the house. After
    that, head to the docks.' 
    br
    e 'More information about this mod can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/68711/mod-skie-the-cost-of-one-girls-soul'
    primary_link 'https://baldursgate.fandom.com/wiki/Skie_Silvershield'
  }
  fancy_spacer
  # ========================================================================== #
  # === (26) NPC Strongholds
  #
  # Last update: August 2022.
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'NPC Strongholds (<b>version 8</b> is the latest, as of August 2022)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'There are at the least two different mods that handle strongholds
    for the party. This paragraph tries to focus mostly on the more
    modern mod, rather than the older, original mod, which is a bit
    buggy.'
    br
    e "This mod is fairly trivial: some of the NPCs in the party can
    run a stronghold. In order to enable this, the NPC has to be in
    the party <b>at the time of meeting the conditions</b>."
    br
    e 'For the Mage Stronghold (the sphere), in the final lesson the
    apprentices must attempt to create a more powerful magical item.
    The choices available here are:'; br; reset_the_counter
    counter 'the Robe of the Apprenti (AC3)'
    counter 'the Ring of Wizardry'
    counter 'Reaching Ring'
    counter 'Staff of Power'
    br
    e 'More information about the <b>Mage Stronghold mod</b> can be
    found here:'
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Mage_Stronghold#Gameplay'
    br
    e 'The final reward for the Druid Stronghold mod is the
    <b>Golden Lion Figurine</b>.'
    br
    e 'The <b>NPC Strongholds</b> mod can be downloaded from the following
    location:'
    br
    primary_link 'https://www.gibberlings3.net/mods/quests/npcstrongholds/'
    primary_link 'https://www.gibberlings3.net/files/file/959-npc-strongholds/'
    primary_link 'https://www.gibberlings3.net/files/file/959-npc-strongholds/?do=download'
    primary_link 'https://drive.google.com/file/d/1KcZPzRMDA2HqIo83VyADZJIjYTIGvNrF/view'
  }
  fancy_spacer
  # ========================================================================== #
  # === (46) Tyris Flare - the NPC                                 (tyris tag)
  #
  # Latest release: 31.08.2023
  # Latest version: v11.00
  #
  # mkdir 46_Tyris_Flare_NPC_mod_v11.00_released-on-31.08.2023; cd 46_Tyris_Flare_NPC_mod_v11.00_released-on-31.08.2023
  # wget https://github.com/Gibberlings3/TyrisFlare/releases/download/v11.00/tyris-flare-npc-v11.zip
  # ========================================================================== #
  # https://www.gibberlings3.net/mods/npcs/tyris/
  # https://github.com/Gibberlings3/TyrisFlare
  # https://github.com/Gibberlings3/TyrisFlare/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Tyris Flare - the NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/jRVMBs8.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_tyris_flare'; drag_for :drag_bg2_tyris_flare
  ptext {
    e 'Tyris Flare - the NPC'
    br
    the_mod_can_be_downloaded_from 'https://github.com/Gibberlings3/TyrisFlare'
    br
    the_mod_can_be_downloaded_from 'https://github.com/Gibberlings3/TyrisFlare/releases/tag/v11.00'
  }
  fancy_spacer
  # ========================================================================== #
  # === Alternatives tag
  #
  # Latest update:  28.03.2021
  # Latest version: 15
  #
  # mkdir 15_Alternatives_mod_v15_released_on_28.03.2021; cd 15_Alternatives_mod_v15_released_on_28.03.2021
  # wget https://github.com/Gibberlings3/Alternatives/releases/download/v15/Alternatives_v15.zip
  # ========================================================================== #
  # https://github.com/Gibberlings3/Alternatives
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Alternatives') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Alternatives'
    br
    primary_link 'https://www.gibberlings3.net/mods/quests/alternatives/'
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Saradas tag
  #
  # Latest update:  23.07.2021
  # Latest version: 2.0.0
  #
  # mkdir 11_saradas_magic_for_BG2-v2.0.0_released_on_23.07.2021; cd 11_saradas_magic_for_BG2-v2.0.0_released_on_23.07.2021
  # wget https://github.com/SpellholdStudios/Saradas_Magic_for_BG2/releases/download/v2.0.0/saradas-magic-for-bg2-v2.0.0.zip
  # ========================================================================== #
  # https://github.com/SpellholdStudios/Saradas_Magic_for_BG2/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Saradas mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Saradas: This mod introduces a new NPC, Saradas the archmage, who
    interacts in various ways with the Bhaalspawn's group. In Shadows of
    Amn, he is a non-playable NPC that offers many services to the Bhaalspawn's
    group. You can find him in the temple of Lathander, in the Temple
    District of Athkatla."
    br
    e 'Latest version: 2.0.0, released on the 23.07.2021.'
    br
    the_mod_can_be_downloaded_from 'https://github.com/SpellholdStudios/Saradas_Magic_for_BG2'
    br
    the_mod_can_be_downloaded_from 'https://github.com/SpellholdStudios/Saradas_Magic_for_BG2/releases'
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Lhannd                                                   (Lhannd tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Lhannd mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Lhannd'
    br
    e "After a day, you should return to his home. He won't be there. Then,
    go back to Crooked Crane. He won't be by the bar, but next to the
    stairs, on the ground, drunk. He may be a bit easy to miss. Go next
    to the stairs, behind the bartender."
    br
    primary_link 'https://www.weaselmods.net/forumdisplay.php?fid=66'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Shuri Ninja Kit mod
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'The Shuri Ninja Kit mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    the_mod_can_be_downloaded_from(
      'https://github.com/GwendolyneFreddy/Shuri-Ninja/releases'
    )
    br
    e 'Discussion can be found here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/81880/mod-the-shuri-ninja-kit-mod-has-been-updated-v2-0-0'
  }
  fancy_spacer
  # ========================================================================== #
  # === (48) Jazon the revenant                                    (jazon tag)
  #
  # Last upstream release:      01.11.2024 
  # Latest version:             3
  #
  # mkdir 19_Jazon_the_revenant_v2_published-on-01.11.2024; cd 19_Jazon_the_revenant_v2_published-on-01.11.2024
  # wget https://github.com/Deratiseur/Jazon/archive/refs/tags/v3.zip
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/88526/jazon-the-revenant-a-new-tiny-mod-for-bg2ee-and-iwdee
  # https://github.com/Deratiseur/Jazon
  # https://github.com/Deratiseur/Jazon/releases
  # wget https://github.com/Deratiseur/Jazon/archive/refs/tags/v1.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Jazon the revenant (Last update: 
    <b>15.05.2024</b>, version <b>1</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Jazon the revenant. He can be found in the Athlakata cemetary, in one
    of the tombs.'
    br
    the_mod_can_be_downloaded_from(
      'https://github.com/Deratiseur/Jazon',
      'https://github.com/Deratiseur/Jazon/releases'
    )
  br;}
  fancy_spacer
  # ========================================================================== #
  # === Check the Bodies                                          (bodies tag)
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/75748/mod-spotlight-check-the-bodies/p1
  # https://www.spellholdstudios.net/ie/ctb/
  # https://github.com/SpellholdStudios/Check_the_Bodies
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Check the Bodies (Last update: <b></b>, version <b></b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/jRVMBs8.png',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_mod_check_the_bodies'; drag_for :drag_bg2_mod_check_the_bodies
  ptext {
    boldbr "<b>Check the Bodies</b> adds a few new areas. For instance,
    <b>Hlondeth</b> is a whole new city with three districts, about a
    seven day's march east of Athkatla (first accessible in chapter 2)."
    br
    e 'The Academy of Kuldin is a large dungon (first accessible in chapter 2).
    "Academy of Kuldin" is added to the world-map (south of the Snowflake
    Mountains) the first time you visit the City Gates district of
    Athkatla.'
    br
    e "The mod also installs <b>Candlekeep Chores</b>, which will
    trigger inside the library of Irenicus' Dungeon. This quest can be
    a bit annoying, as the young protagonist has a very slow movement
    rate. It is recommended to also install the component
    'Candlekeep Chores Fast Foreward'. Each finished chore will grant
    the PC an ability."
    br
    e "This mod also installs a Saerk Farrahd's banquet invitation,
    which can cause issues."
    br
    e "One can also dive into the pool of water in the cave in Umar
    Hills; you will land in a cave which connects to an ancient
    library."
    br
    e 'Holly The Elf can be found inside the <b>Temple of Helm</b>,
    in the Temple district of Athkatla.'
    br
    e "<b>Ice</b> can be found after talking to <b>Calbor</b>
    inside Delosar's Inn in the Bridge district of Athkatla."
    br
    e 'Helping Melynda the Mute: find a way to communicate
    with Melynda in the kitchen of the Copper Coronet in
    the Slums district of Athkatla (good path), or talk
    to the two Cowled Wizards standing outdoors in
    the Government district of Athkatla (evil path).'
    br
    e '<b>Velvetfoot</b> the pirate can be found in the City Gates
    district of Athkatla. This requires a fighter of level 10+ or
    any other class of level 14+.'
    br
    e 'The <b>Drow Library</b> is an Ancient Library. It will be
    added onto the map the first time you visit the City Gates
    district of Athkatla.'
    br
    e "The Academy of Kudin is a large dungeon (first accessible
    in chapter 2), which reuses the area backgrounds of IWD1's
    <b>Severed Hand</b> tower."
    br
    e 'The <b>Company of Eight</b> is a dungeon crawl adventure, in
    the Forest of Tethyr.'
    br
    e "The Liberation of Hlondeth is a whole new city with three
    districts, about a seven day's march east of Athkatla (first
    accessible in chapter 2)."
    br
    e 'The Maltese Artifact is an elven lady approaching you in
    the Bridge district of Athkatla, and slipping you a statuette.
    This requires a mage in the party, and the main actor has to
    have acquired a stronghold already.'
    br
    e 'Civil Disobedience can be encountered upon entering the
    Government district of Athkatla in chapter 6.'
    br
    e "The Master Vampire starts when looting a letter from
    Bodhi's sarcophagus after killing her in chapter 6."
    br
    e 'Speak to the Dead * Ryberg and his Uncle (a.k.a
    Lost Inheritance) [quest]: Ryberg approaches you
    outdoors in Athkatla. (Requires: Sorcerer or Mage
    CHARNAME of level 10+.)'
    br
    e 'Horton Spots a Who: Talk to Wyrbrin Horton, who stands
    outdoors in the eastern part of Brynnlaw (upper level) at
    night, using a single-class Thief party member.'
    br
    the_mod_can_be_downloaded_from(
      'https://forums.beamdog.com/discussion/75748/mod-spotlight-check-the-bodies/p1',
      'http://www.spellholdstudios.net/ie/ctb',
      'http://www.shsforums.net/files/category/39-check-the-bodies/',
      'http://www.shsforums.net/files/download/58-check-the-bodies/'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === (22) Back to Brynnlaw                                   (Brynnlaw tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Back to Brynnlaw') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'After meeting the female wizard, the party should venture
    into the Docks district, in order to talk to her again.'
    br
    e 'Note that there was an indirect mod-conflict (at the least in
    March 2024, with the then latest releases) between Back to Brynnlaw
    mod and the Tactics remix mod, in that Tactis remix as well as
    Back to Brynnlaw, both occupy the house in the docks district
    close to the thieves guildhall.'
    br
    primary_discussion 'https://forums.beamdog.com/discussion/38638/review-back-to-brynnlaw'
    primary_discussion 'https://github.com/Pocket-Plane-Group/Back_to_Brynnlaw'
  }
  fancy_spacer
  # ========================================================================== #
  # === Escape from Brynnlaw
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Escape from Brynnlaw') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Head to the southeast of the city after killing Desharik and
    his pirate buddies.'
  }
  fancy_spacer
    # ========================================================================== #
  # === (22) Amber the NPC
  #
  # Latest version is v8, December 2023.
  # ========================================================================== #
  # https://www.gibberlings3.net/mods/npcs/amber/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Amber the NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "Amber is a Tiefling Fighter/Thief character."
    br
    e 'Three mini-quests are included in this MOD.'
    br
    e 'Amber has her own website:'
    br
    primary_link 'http://vmarttil.kapsi.fi/amber/'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://www.gibberlings3.net/mods/npcs/amber/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (36) Homeward bound
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Homeward bound") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/zp9rumY.jpg',
                     'round_black5 mar0_5em mars3em',
                     'drag_bg2_mod_homeward_bound'; drag_for :drag_bg2_mod_skitias_npcs
  ptext {
    e 'Homeward bound'
    br
    primary_discussion 'http://www.shsforums.net/topic/30937-homeward-bound/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (35) Skitia's NPCs                                       (Skitia tag)
  #
  # Last update:    02.10.2023
  # Latest version: 1.13
  #
  # mkdir 35_Skitia-NPCs-1.13-released-on-02.10.2023; cd 35_Skitia-NPCs-1.13-released-on-02.10.2023
  # wget https://github.com/Skitia/SkitiaNPCs/archive/refs/tags/v1.13.zip
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#drag_bg2_mod_skitias_npcs
  # ========================================================================== #
  # https://github.com/Skitia/SkitiaNPCs/releases
  # wget https://github.com/Skitia/SkitiaNPCs/archive/refs/tags/v1.11.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Skitia's NPCs") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/zp9rumY.jpg',
                     'round_black5 mar0_5em mars3em',
                     'drag_bg2_mod_skitias_npcs'; drag_for :drag_bg2_mod_skitias_npcs
  ptext {
    e 'This mod adds <b>five new NPCs</b>:'
    br
    e '<b>Emily</b> (an archer), Helga (a cleric), Kate (a fighter),
    Recorder (a bard) and Vienxay (a mage/thief).'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/78071/v1-00-skitias-npcs-for-bg2-ee-and-eet/p1'
    primary_link 'https://github.com/Skitia/SkitiaNPCs'
    primary_link 'https://github.com/Skitia/SkitiaNPCs/releases'
    primary_link 'https://github.com/Skitia/SkitiaNPCs/archive/master.zip'
  }
  # ========================================================================== #
  # === The Ascension mod                                (ascension tag)
  # ========================================================================== #
  # https://github.com/InfinityMods/Ascension/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Ascension mod (Last update: <b>19.02.2022</b>, Version: 2.0.23)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "The <b>Ascensions mod</b> changes the end of the Throne of Bhaal
    expansion to feature extended roleplaying and tactical opportunities.
    It was written by <b>David Gaider</b> and members of the IEEAIS group;
    with permission from Wes Weimer the project has been modernized and
    is now supported at G3."
    br
    e 'It is a fairly ok-ish MOD, but it should be installed first,
    in order to avoid problems with other mods. Unfortunately in March
    2023, installation of this mod has failed.'
    br
    e 'It also features tougher enemies, such as Tougher Abazigal,
    Tougher Balthazar, Tougher Demogorgon, Tougher Gromnir, Tougher
    Illasera and Tougher Yaga-Shura.'
    br
    e 'The <b>Ascension mod</b> can be downloaded from here:'
    br
    primary_link 'https://www.gibberlings3.net/mods/quests/ascension/'
    primary_link 'https://github.com/InfinityMods/Ascension/releases'
    primary_link 'https://github.com/InfinityMods/Ascension/releases/download/2.0.23/ascension-2.0.23.zip'
    br
    anm 'There is a new release of Ascension available, version
    <b>2.0.24</b>.'
  }
  fancy_spacer
  # ========================================================================== #
  # === All Things Mazzy                                      (mazzy tag)
  # ========================================================================== #
  # https://github.com/Ratatoskr589/All-Things-Mazzy/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'All Things Mazzy (Last update <b>21.03.2023</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'This mod is about Mazzy.'
    br
    e 'Unfortunately this mod did not work for me in <b>March 2023</b>.
    It may be slightly buggy, but it appears to work for others,
    so quite possibly - and somewhat likely - the mod works fine.'
    br
    e 'Discussion about this mod can be seen here:'
    br
    primary_link 'https://forums.beamdog.com/discussion/71473/megamod-3-13-mazzy-romance-clara-npc-darkside-anomen-flying-aerie-for-the-evil-more-done/p1'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://github.com/Ratatoskr589/All-Things-Mazzy'
    primary_link 'https://github.com/Ratatoskr589/All-Things-Mazzy/archive/refs/tags/v3.13.tar.gz'
  }
  fancy_spacer
  # ========================================================================== #
  # === (29) The BG2 Fixpack mod                                 (fixpack tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The BG2 Fixpack mod (Last update: <b>19.02.2022</b>, Version: 2.0.23)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The <b>BG2 Fixpack mod</b> should be installed rather early on, as it
    may fix some other downstream problems. In March 2023 it appears as
    if most of its content no longer works; or has been integrated by
    other mods.'
    br
    e 'The <b>BG2 Fixpack mod</b> can be downloaded from the following
    location:'
    br
    primary_link 'https://www.gibberlings3.net/mods/fixes/bg2fixpack/'
    primary_link 'https://github.com/Gibberlings3/BG2-Fixpack'
  }
  fancy_spacer
  # ========================================================================== #
  # === (30) Project Infinity            (Infinity tag, Project Infinity tag)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Project Infinity (Last update on: <b>22.08.2022</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "<b>Project Infinity</b> is a very useful <b>mod manager</b> for
    Baldur's Gate Enhanced Edition. It supports every Infinity Engine
    game and version."
    br
    e 'In March 2023 this mod appears to be not installable - when
    clicking on the .exe file nothing happens.'
    br
    primary_link 'https://github.com/ALIENQuake/ProjectInfinity'
    primary_link 'https://github.com/ALIENQuake/ProjectInfinity/raw/master/ProjectInfinity.exe'
  }
  fancy_spacer
  # ========================================================================== #
  # === (32) Mur Neth NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Mur Neth NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Mur Neth NPC - unclear whether this can be installed or not.'
  }
  fancy_spacer
  # ========================================================================== #
  # === (33) Sword Coast Stratagems              (Sword Coast Stratagems tag)
  #
  # See the entry at:
  #
  #   https://github.com/Gibberlings3/SwordCoastStratagems
  #
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Sword Coast Stratagems mod "\
          "(Last update: <b>21.09.2021</b>, Version: v34.3)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "The <b>Sword Coast Stratagems</b> is a collection of interconnected
    mini-mods for Baldur's Gate II. It is primarily a tactical and
    AI-enhancement mod: the idea is to make the game's combat more
    interesting, tactically challenging, and realistic by more
    effective use of, and choices of, creatures' abilities.
    It also contains a few rule tweaks and ease-of-use features."
    br
    e 'Personally I am not convinced that this is a good mod. It
    makes too many modifications, some of which cause awkward
    results onto the game or change it in peculiar ways.'
    br
    primary_link 'https://forums.beamdog.com/discussion/79509/new-version-of-sword-coast-stratagems-v33-now-available'
    primary_link 'https://www.gibberlings3.net/mods/tweaks/scs/'
    primary_link 'https://github.com/Gibberlings3/SwordCoastStratagems'
    primary_link 'https://github.com/Gibberlings3/SwordCoastStratagems/releases/download/v34.3/stratagems-34.3.exe'
  }
  fancy_spacer
  # ========================================================================== #
  # === (24) Mystigan                                           (Mystigan tag)
  #
  # Last update: 07.07.2022
  # Version:     1.62
  #
  # mkdir 24_Mystigan_v1.62_released_on_07.07.2022; cd 24_Mystigan_v1.62_released_on_07.07.2022
  # wget https://akadis.baldursgateworld.fr/Mystigan/zip/Mystigan1.62.zip
  # ========================================================================== #
  # https://akadis.baldursgateworld.fr/Mystigan/MystiganEn.html
  # wget https://akadis.baldursgateworld.fr/Mystigan/zip/Mystigan1.62.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Mystigan") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e ''
    primary_link 'https://akadis.baldursgateworld.fr/Mystigan/MystiganEn.html'
  }
  fancy_spacer
  # ========================================================================== #
  # === (36) Walahnan
  #
  # Last updated: 
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/82441/mod-walahnan-the-chronomancer-npc
  # https://downloads.weaselmods.net/download/walahnan-bg2ee/
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Walahnan") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Walahnan is a powerful chronomancer and a man who suffers from
    germophobia.'
    br
    primary_link 'https://forums.beamdog.com/discussion/82441/mod-walahnan-the-chronomancer-npc'
    primary_link 'https://downloads.weaselmods.net/download/walahnan-bg2ee/'
  }
  fancy_spacer
  # ========================================================================== #
  # === (36) Planar Sphere Mod
  #
  # Last updated: 
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Planar Sphere Mod (last release in )") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "The <b>Planar Sphere Mod</b> allows you to turn the sphere into
    a full-blown training facility for Cowled Wizard apprentices."
    br
    e 'The mod still works in the year 2023 - you have to download
    the correct file from github.'
    br
    e "In the main quest you have to find a Red Wizard spy at
    Waukeen's Promenade. Go there to the Den of the Seven Dales
    Inn - the spy is a Cowled Wizard."
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://sorcerers.net/Games/BG2/index.php'
    primary_link 'http://www.shsforums.net/files/file/131-planarsphere/'
    br
    e 'More information about this mod can be found here:'
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Planar_Sphere_Mod'
    primary_link 'https://forums.beamdog.com/discussion/75761/mod-spotlight-planar-sphere-mod/p1'
    primary_link 'https://sorcerers.net/Games/dl/eyJpdiI6IjhRd0ZoemsrRXhGOUE2MTdldDRSNUE9PSIsInZhbHVlIjoicDcwcnd1NmRmdXc4YkxDaGNTNmtVK0tXaDhIUGMrZ2xWZGYxWVI5dmluZFV0TkNxb1A1U1ZvdDBPb2JIamF1dCIsIm1hYyI6ImFkMTUyMGY4MmU5YzdjYmNmYmQ3Y2EzMjI2YTliNDk0ZWU1NWRiN2ZjNmY3OTA4ZWIzZGMyZmVlNzQxMWU2NjcifQ=='
  }
  fancy_spacer
  # ========================================================================== #
  # === Wings                                                      (wings tag)
  #
  # Latest upstream release: 12.10.2024
  # Latest version:          1.08
  #
  # mkdir 11_Wings_mod_v1.08_released_on_12.10.2024
  # wget https://github.com/Skitia/Wings/archive/refs/tags/v1.08.zip
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/83120/wings-v1-05/p1
  # https://github.com/Skitia/Wings/releases
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Wings mod') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'wings') {
    e 'A big portion of this mod takes place after the slavers part was
    completed, in SoA.'
    br
    e 'After the slaves were freed in the slavers compound, twentyfour
    hours later, traveling between districts of Athkatla with Aerie in
    the party, an alley encounter is triggered.'
    br
    e 'Twentyfour hours later, Trent, the anti-slavery agent, may
    contact the party - or you may have to talk to him. He may
    be at the Gate district.'
    br
    e 'Discussion about the wings mod:'
    br
    primary_link 'https://forums.beamdog.com/discussion/83120/wings-v1-05'
    primary_link 'https://forums.beamdog.com/discussion/26945/wings-version-0-91b/p1'
    primary_link 'https://github.com/Skitia/Wings/releases'
    primary_link 'http://www.shsforums.net/topic/57919-mod-in-progress-wings-aerie-expansion-for-bg2ee/'
    br
    e 'A walkthrough can be found here:'
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Wings_walkthrough'
  }
  fancy_spacer
  # ========================================================================== #
  # === (37) The Darkest Day                                            (TDD)
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'The Darkest Day (Last update <b></b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The Darkest Day is a mega-mod. It includes new worldmap areas, quests,
    items, NPCs, kits, spells, and rule changes, and is notorious for giving
    your party excessive amounts of XP and overpowered items.'
    br
    e 'This mod does not appear to work that well anymore, though,
    and appears to have been abandoned.'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://web.archive.org/web/20111108161336/http://www.teambg.org/forum/index.php?action=downloads;sa=downfile&id=123'
    primary_link 'http://www.downloads.teambg.org/TDDv1.14.rar'
  }
  fancy_spacer
  # ========================================================================== #
  # === (38) Spell Revisions Mod
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Spell Revisions Mod (Last update: <b>01.09.2022</b>, Version: 2.0.23)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'This mod includes some spell-related changes.'
    br
    e 'It is unclear whether this mod still works as of March 2023.'
    br
    e 'To install it do:'
    br
    cmd '  weinstall spell_rev'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://github.com/Gibberlings3/SpellRevisions'
    br
    e 'Documentation for this mod can be found here:'
    br
    primary_link 'https://gibberlings3.github.io/SpellRevisions/'
  }
  fancy_spacer
  # ========================================================================== #
  # === SoD-to-BG2EE-Item-Upgrade mod                                (sod tag)
  #
  # Installs a keyring.
  #
  # Last update:    06.05.2023
  # Latest version: 2.0.6
  #
  # mkdir 13_SoD-to-BG2EE-Item-Upgrade-mod-v2.0.6_released_on_06.05.2023; cd 13_SoD-to-BG2EE-Item-Upgrade-mod-v2.0.6_released_on_06.05.2023
  # wget https://github.com/Gibberlings3/SoD-to-BG2EE-Item-Upgrade/releases/download/v2.0.6/sod2bg2_iu-v2.0.6.exe
  # ========================================================================== #
  # https://github.com/Gibberlings3/SoD-to-BG2EE-Item-Upgrade
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"SoD-to-BG2EE-Item-Upgrade mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'This mod upgrades various items, such as the <b>Helm of Opposition</b>
    and other items.'
    br
    e 'Items that are installed by this mod are as follows:'
    br
    table2('mars2em marb1em','','font-size: 1.2em;',
      'KeyRing',"Table by Jailkeep Golem in Irenicus' dungeon",
      'Tongue of Acid +3, Guardian Devil, Echo of the Fiend +3 (random)',
      "Shadow Dragon (Thaxll'ssillyia), Shade Lord's Dungeon",
      'Vexation +2',"Pirate Captain in Hideout of Sea's Bounty Tavern",
      'Crown of Lies','Firkraag (the dragon in the Windspear Hills Dungeon)',
      "Star-Strewn Boots",'Unseeing Eye, Beholder Area in Sewers (Unseeing Eye sidequest)',
      '"Green" Dragonscale Armor','Kyland Lind, Druid Grove Area',
      "Stalker's Gauntlets",'Shade Lord, Umar Hills Dungeon',
      'Coalesced Shadow Ioun Stone','Shade Lord, Umar Hills Dungeon',
      'Sundermaul +3','Therndle Daglefodd, Underdark, reward for rescuing
       the Svirfneblin child',
      'Cloverleaf',"Haer'Dalis' starting equipment",
      'Uncursed Staff +1',"Sorcerous Amon, Den of Seven Vales in Waukeen's Promenade",
      'Backwhacker +2','Cohrvale, Slums',
      'Bow of the Banshee +2','Gallchobhair, Temple Distric sewers',
      'Nimblefinger Gloves',"Renal Bloodscalp, reward for killing Mae'Var
       after proving his treachery",
      'Screaming Bagpipes',"Pooky, Den of Seven Vales in Waukeen's Promenade",
      'Bullet of Darkness +3',"Enge's Shop, Waukeen's Promenade",
      'Void-Tipped Arrow +3',"Enge's Shop, Waukeen's Promenade",
      'Cloak of Minor Arcana',"Mekrath, Sewers, Haer' Dalis sidequest",
      "Element's Fury +2, Acid-Etched Dagger +2 (random)","Pai'Na, Lower Tombs
       in Graveyard District",
      'Storm Pike +2','Anarg, Bridge District (Fallen Paladins quest)',
      'Trollblood Ioun Stone',"Nalia's starting equipment",
      'Green Dragon Scales',"Green Dragon, Watcher's Keep, Test of Bravery"
    ) 
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://www.gibberlings3.net/mods/items/sod-to-bg2ee-item-upgrade/'
    br
    primary_link 'https://github.com/Gibberlings3/SoD-to-BG2EE-Item-Upgrade'
  }
  fancy_spacer
  # ========================================================================== #
  # === Fade NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Fade NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The Fade NPC mod adds <b>Fade</b>, <b>a chaotic neutral thief</b>,
    to BG2 as a joinable NPC.'
    br
    e 'A walkthrough can be found here:'
    br
    primary_link 'https://baldursgate.fandom.com/wiki/Fade_NPC_walkthrough'
  }
  # ========================================================================== #
  # === Strategies against poison (poison tag)
  # ========================================================================== #
  fancy2 'Strategies against poison (poison tag)'
  ptext(id: 'poison') {
    e '- The Ring of Anti-Venom provides the user with complete immunity to poison.'
    e '- The Periapt of Proof Against Poison provides protection against poison.'
    e '- Helm of the Rock adds 25% poison resistance.
    The lich Vongoethe in Amkethran drops this ring.'
    e '- The scroll Protection From Poison provides protection against
    poison. The Adventurer Mart, Galoomp the Bookkeeper and the
    Temple of Helm sell such a scroll, for instance.'
  }
  # ========================================================================== #
  # === Imnesvale
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Imnesvale') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "When the notes are discovered in a witch's house, the Temple Ruins
    will then be marked on the world map."
  }
  # ========================================================================== #
  # === BG2 EE Portraits
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'BG2 EE Portraits') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://i.imgur.com/1ykgldN.jpg',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_mod_portraits'; drag_for :drag_bg2_mod_portraits
  ptext {
    e 'This mod simply adds loads of new portraits to use in the game. You
    can pick and choose which ones you want.'
    br
    e 'These modifications add a bit more detail to the standard portraits,
    and considering you will be staring at them for most of the game,
    they may be beneficial in regards to enhancing the main gameplay at
    hand. In my personal opinion, though, some of the modified portraits
    are worse than their original counterpart, so you may want to
    look at the portraits prior to installing this.'
    br
    e 'This mod should be installed into <b>Documents/BGEE/Portraits</b> 
    (or create it anew).'
    br
    e 'The mod can be downloaded from the following location:'
    br
    primary_link 'https://www.nexusmods.com/baldursgate2ee/mods/1'
  }
  fancy_spacer
  # ========================================================================== #
  # === Keto the NPC mod
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Keto (a NPC) (Last update: <b>Aug 03, 2020</b>)') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  embed_remote_image 'https://www.pocketplane.net/wp-content/uploads/2004/12/KetoNewlogo.jpg',
                     'round_black3 mar0_5em mars3em',
                     'drag_bg2_keto_the_NPC'; drag_for :drag_bg2_keto_the_NPC
  ptext {
    e 'Keto, a NPC, is a modification adding a single NPC. She is a 
    bard.'
    br
    e 'Unfortunately she is a bit buggy and talks as if she is
    permanently drunk. I only give this mod 2 out of 5 points.'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://www.pocketplane.net/keto-npc/'
    primary_link 'https://github.com/Pocket-Plane-Group/Keto/releases'
    primary_link 'https://github.com/Pocket-Plane-Group/Keto/releases/download/v6/Keto-SoAv6.zip'
  }
  fancy_spacer
  # ========================================================================== #
  # === Improved Asylum
  #
  # Last release: 13.04.2020
  #
  # 11_Improved_Asylum_mod-released-on-13.04.2020.exe
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Improved Asylum mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'This is the <b>Improved Asylum mod</b>.'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://github.com/SpellholdStudios/Improved_Asylum'
    primary_link 'https://forums.beamdog.com/discussion/79992/improved-asylum-breudayael-party'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Wheels of Prophecy mod                               (wheels tag)
  #
  # Latest update:  30.06.2021
  # Latest version: 8.5
  #
  # mkdir 33_The_Wheels_of_Prophecy_mod_v8.5_released_on_30.06.2021
  # ========================================================================== #
  # https://github.com/Gibberlings3/WheelsOfProphecy/releases/
  # https://github.com/Gibberlings3/WheelsOfProphecy/releases/tag/v8.5
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"The Wheels of Prophecy mod (Last update: <b>30.06.2021</b>, Version: 8.5)") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'This mod modifies some <b>Throne of Bhaal</b> content.'
    br
    e 'More links related to this mod can be found here:'
    br
    primary_link 'https://www.gibberlings3.net/mods/quests/wheels/'
    primary_link 'https://github.com/Gibberlings3/WheelsOfProphecy'
    primary_link 'https://github.com/Gibberlings3/WheelsOfProphecy/releases/'
    primary_link 'https://github.com/Gibberlings3/WheelsOfProphecy/releases/download/v8.5/wheels-v8.5.exe'
    primary_link 'https://forums.beamdog.com/discussion/36333/what-exactly-does-wheels-of-prophecy-do'
  }
  fancy_spacer
  # ========================================================================== #
  # === SilverStar NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'SilverStar NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "<b>SilverStar</b> is an elven neutral evil assassin who can join the
    party in Irenicus' lovely underground hole. She is partially insane and
    has some childhood obsession for sweet little lambs..."
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://baldursextendedworld.com/Paulas-Adopted-Mods/'
    primary_link 'https://www.dropbox.com/s/ut17uf5rt27m7en/Silverstar.zip?dl=1'
  }
  fancy_spacer
  # ========================================================================== #
  # === Kitanya NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Kitanya NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "<b>Kitanya</b> is a female elven wizard slayer hunting Irenicus.
    This part includes a romance. The mod was resurrected from
    the vanished rpgdungeon.net and updated for EE games."
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://baldursextendedworld.com/Paulas-Adopted-Mods/'
    primary_link 'https://github.com/PaulaMigrate/Kitanya-Resurrected/archive/master.zip'
  }
  fancy_spacer
  # ========================================================================== #
  # === Saerileth NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Saerileth NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    embed_remote_image 'https://i.imgur.com/Q1GRpOj.gif',
                       'round_black3 mar0_5em mars3em',
                       'drag_bg2_mod_saerileth_npc'; drag_for :drag_bg2_mod_saerileth_npc
    brbr
    e "<b>Saerileth</b> is a <b>female human paladin</b>. She can be found
    in the <b>Temple District</b>, near Pimlico's Estate. That Estate is
    to the northeastern part of the Temple District Map."
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'http://www.baldursgatemods.com/forums/index.php?topic=5253.0'
    primary_link 'https://github.com/PaulaMigrate/Saerileth/archive/master.zip'
  }
  fancy_spacer
  # ========================================================================== #
  # === ruad tag
  #
  # Last Update:    28.01.2021
  # Latest version: v29.4.0
  # 11_ruad-rofhessa-item-upgrade-v29.4.0-released-on-28.01.2021
  # ========================================================================== #
  # https://github.com/SpellholdStudios/RuadRofhessaItemUpgrade
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'ruad') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "This mod is all about Ruad, a new smith in Waukeen's Promenade, who
    improves items as well as forges some quite new ones."
    br
    primary_link 'https://github.com/SpellholdStudios/RuadRofhessaItemUpgrade'
  }
  fancy_spacer
  # ========================================================================== #
  # === Dvaradime tag
  #
  # Last Update:    30.09.2024
  # Latest version: 1.6
  #
  # mkdir 11_Dvaradime_the_NPC_v1.6-30.09.2024
  # ========================================================================== #
  # https://downloads.weaselmods.net/download/dvaradime/
  # https://forums.beamdog.com/discussion/87161/mod-dvaradime-npc-for-bg2ee
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Dvaradime') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Dvaradime'
    br
    primary_link 'https://forums.beamdog.com/discussion/87161/mod-dvaradime-npc-for-bg2ee'
    primary_link 'https://downloads.weaselmods.net/download/dvaradime/'
  }
  fancy_spacer
  # ========================================================================== #
  # === Pai'Na mod                                                (paina tag)
  #
  # Last update:  26.04.2024
  # Last version: 1.9
  # Created by:   TheArtisan
  #
  # mkdir 25_paina_NPC_mod_for_BG2EE_v1.9_released_on_26.04.2024; cd 25_paina_NPC_mod_for_BG2EE_v1.9_released_on_26.04.2024
  # wget https://github.com/ArtemiusI/Pai-Na-NPC-mod-for-BG2-EE/archive/refs/tags/v1.9.zip
  # ========================================================================== #
  # https://forums.beamdog.com/discussion/43113/v1-7-paina-a-half-drow-hivemaster-druid-npc-for-bg2-ee/p1
  # ========================================================================== #
  # https://github.com/ArtemiusI/Pai-Na-NPC-mod-for-BG2-EE/
  # https://github.com/ArtemiusI/Pai-Na-NPC-mod-for-BG2-EE/releases
  # https://github.com/ArtemiusI/Pai-Na-NPC-mod-for-BG2-EE/archive/refs/tags/v1.9.zip
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+"Pai'Na mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e "The Pai'Na mod allows the player to recruit <b>Pai'Na</b> for the party.
    Pai'Na can summon spiders or annoy enemy spell casters via an insect
    plague."
    br
    e 'The latest version is <b>1.9</b>.'
    br
    primary_link 'https://forums.beamdog.com/discussion/43113/v1-7-paina-a-half-drow-hivemaster-druid-npc-for-bg2-ee/p1'
    primary_link 'https://github.com/ArtemiusI/Pai-Na-NPC-mod-for-BG2-EE/'
  }
  fancy_spacer
  # ========================================================================== #
  # === The world map mod                        (world map tag, worldmap tag)
  #
  # Latest version: v13.1.1
  # Latest update:  15.04.2024
  #
  # mkdir 01_The-Worldmap-Mod-v13.1.1-released-on-15.04.2024
  # wget https://github.com/SpellholdStudios/BP-BGT-Worldmap/releases/download/v13.1.1/worldmap-v13.1.1.zip
  # ========================================================================== #
  # https://github.com/SpellholdStudios/BP-BGT-Worldmap
  # ========================================================================== #
  fancy_h1("#{BALDURS_GATE_LOGO}The world map mod") {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'The world map mod.'
    br
    primary_link 'https://github.com/SpellholdStudios/BP-BGT-Worldmap'
    primary_link 'https://github.com/SpellholdStudios/BP-BGT-Worldmap/releases/tag/v13.1.1'
  }
  fancy_spacer
  # ========================================================================== #
  # === Uldar NPC
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Uldar NPC') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'Uldar, the barbarian half-orc, can be found among the slave
    gladiators in the Copper Coronet and he can join you to fight
    the oppressors in Athkatla.'
    br
    e 'The mod can be downloaded from here:'
    br
    primary_link 'https://baldursextendedworld.com/Paulas-Adopted-Mods/'
    primary_link 'https://www.dropbox.com/s/lu3ymv2j8l1w2dh/UldarNPC.zip?dl=1'
  }
  fancy_spacer
  # ========================================================================== #
  # === Helpful knowledge in regards to mods and weidu
  # ========================================================================== #
  fancy_h1(BALDURS_GATE_LOGO+'Helpful knowledge in regards to mods and weidu') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext {
    e 'A file called <b>weidu.log</b> may list each of the mods that are
    installed.'
    br
    e 'Via <b>weidu.exe</b> these mods can be installed. The simplest
    way to get this to work with <b>.tp2</b> files is to copy the weidu.exe
    file and rename it to this scheme:'
    br
    cmd '  setup-NAME_OF_THE_MOD.exe'
    br
    e 'Then it can be double-clicked like any other .exe file on windows.'
  }
  # ========================================================================== #
  # === Where does Baldur's Gate 2 store save files? 
  # ========================================================================== #
  fancy2 "Where does Baldur's Gate 2 store save files?"
  ptext {
    e 'Save games are kept in:'
    br
    cmd "Documents/baldur's gate enhanced edition\save"
    cmd "C:\\Users\\debug\\Documents\\Baldur's Gate II - Enhanced Edition\\save\\"
  }
  # ========================================================================== #
  # === What is the starting reputation in Baldur's Gate 2? 
  # ========================================================================== #
  h2 "What is the starting reputation in Baldur's Gate 2?"
  ptext {
    e "Your <b>PC's alignment</b> determines starting reputation as follows:"
    table2('mars2em pretty_table pad2px','','',
      '<b>Alignment</b>','<b>Reputation</b>',
      'LG','12',
      'NG, CG','11',
      'LN, N, CN','10',
      'LE, NE','9',
      'CE','8'
    )
  }
  # ========================================================================== #
  # === Which triple classes are available in Baldur's Gate 2? 
  # ========================================================================== #
  fancy2 "<b>Which triple classes</b> are available in Baldur's Gate 2?"
  ptext {
    e 'fighter-mage-thief'
    e 'fighter-mage-cleric'
  }
  # ========================================================================== #
  # === Mage spells and their level 
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#mage_spells_and_their_level
  # ========================================================================== #
  fancy2 'Mage spells and their level'
  ptext {
    boldbr 'Mordekanian swords:'
    br
    le2 'Level 7'
  }
  # ========================================================================== #
  # === Links to mods
  # ========================================================================== #
  h2 'Links to mods as well as hints related to mods'
  p_default('mars2em') {
    ntab 'https://forums.beamdog.com/categories/bgii%3Aee-mods'
    ntab 'https://forums.beamdog.com/categories/bgii%3Aee-discussion'
    ntab 'https://steamcommunity.com/sharedfiles/filedetails/?id=2600252516'
  }
  fancy_spacer
  # ========================================================================== #
  # === The lua console                                              (lua tag) 
  # ========================================================================== #
  # http://localhost/programming/ruby/src/games_paradise/lib/games_paradise/www/baldurs_gate2/baldurs_gate2.cgi#the_lua-console
  # ========================================================================== #
  fancy2 'The lua console'
  ptext(id: 'lua') {
    e 'The enhanced editions no longer maintain a file called
    <b>Baldur.ini</b>.'
    br
    e 'It has been changed to <b>Baldur.lua</b>, and it can be found in
    documents/, inside the BGEE directory. So, for instance, on my computer
    system the file may be found here:'
    br
    cmd "C:\\users\\debug\\documents\\Baldurs Gate II - Enhanced Edition\\Baldur.lua"
    br
    e 'Next, append the following String into that file:'
    br
    cmd "  SetPrivateProfileString('Program Options','Debug Mode','1')"
    br
    e 'You should be aware that any guide to editing the baldur.ini
    is no longer relevant, since the .lua uses a different format
    now.'
    br
    e 'Via "<b>Ctl and space bar</b>" you can open the console.'
    br
    e 'Usage examples:'
    br
    cmd "SetPrivateProfileString('Program Options','Debug Mode','1')"
    br
    cmd 'CLUAConsole:CreateItem("itemcode")'
    cmd 'CLUAConsole:CreateItem("CLCK27")'
    cmd 'CLUAConsole:CreateItem("MISC4S")'
    cmd 'CLUAConsole:CreateItem("KEY12")'
  }
  # ========================================================================== #
  # === The Sir Sarles Quest in the Waukeen's Promenade and Telwyn:
  # ========================================================================== #
  fancy2 "The Sir Sarles Quest in the Waukeen's Promenade and Telwyn:"
  ptext {
    e 'The Temple of the Helm (or of other deities) wishes to commission
    the services of the famed sculptor, Sir Sarles.'
    br
    e 'First, the party should venture to the "Jysstev Estate" in the
    Government District to Sir Sarles. Talk to the butler.'
    br
    e "Next, talk to Jerlia, the ore merchant, in \"Waukeen's Promenade\".
    Upon approaching her, Jerlia explains that illithium is very rare and
    she only deals out 50 pounds of the substance each season herself.
    She offers to craft them Illithium Alloy instead, which she can do
    in a day. If the party is diplomatic, and sweetens the pot with
    1,000 gold pieces, she reveals she also buys her illithium from
    a duergar trader, Unger Hilldark, who operates out of the Copper
    Coronet."
    br
    e "Speaking to Unger Hilldark in the Copper Coronet has him reveal
    that he can't give you any illithium, as it was stolen from him
    by an evil demihuman named Neb. If you can kill Neb, you can
    take the ore for yourself. Ungar can be found next to the exit
    on the far west side. Neb's house contains a trapped container
    with 452 gold, a silver necklace, an angel skin ring, and a
    random treasure."
    br
    e 'In the "Unfinished Business Mod", Unger wants of you to find Gorje
    in the Temple Ruins.'
    br
    e "Neb's head can be handed in to Chief Inspector Brega in the Council 
    of Six Building, Government District, for 2500 gold pieces and 
    a Reputation increase of +1."
    br
    e "By removing the Ore from the party's inventory - simply dropping
    it on the floor inside the Jysstev Estate (in the government
    district) and picking it up afterwards suffices - and speaking 
    to Sir Sarles with only the Alloy, the party may give the Alloy 
    to the Temple, and keep the Ore to use to upgrade the Mace of 
    Disruption by taking them both to Cromwell. The only drawback 
    to this route is that it means forfeiting some of the experience
    points that simply giving the ore to Sir Sarles would provide."
    br
    e 'The reward by the Temple of Helm will be a Helm of the Noble.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Gain_the_services_of_Sir_Sarles_for_the_temple'
    ntab 'https://baldursgate.fandom.com/wiki/Waukeen%27s_Promenade'
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-2/quests/sir-sarles.php'
  }
  fancy_spacer
  # ========================================================================== #
  # === Find the kidnappers who buried Tirdir:
  # ========================================================================== #
  fancy2 "Find the kidnappers who buried Tirdir::"
  ptext {
    e 'Click on the half-filled grave to free Tirdir, who was buried alive. 
    He will thank you and give you a Piece of Red Cloth that he tore 
    from his kidnappers before they buried him so you may hunt down 
    the men who have done this, and you earn 6500XP.'
    br
    e "Talk to the grave keeper Sethle nearby. He will tell you that
    his contact can sometimes be found in the Athkatla 'Bridge
    district'. Next, search the Bridge district for men and women
    in red clothing at a house in the south part where
    Am-Si can be found. Confront him and he will flee into 
    the Kidnappers' House."
    br
    e 'Enter the house after him and Am-Si will be killed by
    his co-conspirators for his incompetence. They run out of
    the house, but you can catch up with them on the street.'
    br
    e 'After dealing with them, re-enter the building and
    search it. On the second floor, you can Lady Elgea, 
    who has been kidnapped by the band.'
    br
    e 'The hostage may be freed  during the initial meeting,
    for a reward of <b>16750xp</b>.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Find_the_kidnappers_who_buried_Tirdir'
  }
  fancy_spacer
  # ========================================================================== #
  # === The search guild mod
  # ========================================================================== #
  fancy2 'The search guild mod'
  ptext {
  }
  fancy_spacer
  # ========================================================================== #
  # === Keldorn Firecam the inquisitor
  # ========================================================================== #
  fancy2 'Keldorn Firecam the inquisitor (a NPC)'
  ptext {
    e 'Unfortunately Keldorn can not be affected by haste, which makes him
    a very annoying character to carry about in the group.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Keldorn_Firecam'
    ntab 'https://baldursgate.fandom.com/wiki/Investigate_and_Destroy_the_Cult_of_the_Eyeless'
  }
  fancy_spacer
  # ========================================================================== #
  # === Destroying the Order of Eight Staves:
  # ========================================================================== #
  fancy2 'Destroying the Order of Eight Staves'
  ptext {
    e "This is Neera's companion quest in Throne of Bhaal campaign. To
    kill Vicross make use of true sight scrolls, since she will keep
    on trying to go invisible."
    br
    ntab 'https://baldursgate.fandom.com/wiki/Destroying_the_Order_of_Eight_Staves'
  }
  fancy_spacer
  # ========================================================================== #
  # === Imprisonment (the spell)
  # ========================================================================== #
  fancy2 'Imprisonment (the spell)'
  ptext {
    e 'Imprisonment can be a deadly spell.'
    br
    e 'What helps against it is Spell Immunity - Abjuration. This
    will protect against the Imprisonment spell.'
    br
    e 'The <b>Freedom</b> spell can bring back an imprisoned creature,
    if it is cast in the same area. Only a few merchants have this
    spell - one being Carlig, the other one being Ribald Barterman.'
    br
    e 'If the Imprisonment is cast by an undead creature (e.g.
    Lich), Protection From Undead scrolls shield against it.'
  }
  fancy_spacer
  # ========================================================================== #
  # === How can the "Flail of Ages" be built?                      (flail tag)
  # ========================================================================== #
  fancy2 'How can the "Flail of Ages" be built?'
  ptext {
    e "The <b>Flail of Ages</b> can be forged on the first floor of the
    De'Arnise Keep."
    br
    e "• The Flail Head (Cold) can be found near the northwestern forge on
    the ground floor, behind a hidden door. It is in a container in the
    hidden \"trophy room\" on the first floor of the De'Arnise
    Keep."
    br
    e "• The <b>Flail Head (Acid)</b> is dropped by Glaicus, Lord
    Arnise's bodyguard, on the upper floor."
    br
    e "• The Flail Head (Fire) can be found in the room with the (initially
    inactive) golems on the  upper floor."
    br
    e 'The flail can lateron be upgraded to +5 in <b>Throne of Bhaal</b>,
    at Cespenar in the center of the Pocket Plane.'
    br
    e "• The Flail Head (Poison) can be found in the pool of poison at the 
    second floor of the Watcher's Keep."
    br
    e "• The Flail Head (Electric) can be gained when Abazigal is killed."
    br 
    e 'It can be acquired as well in <b>The Black Pits II:
    Gladiators of Thay</b>, as a reward item after defeating
    Mardii and his Elements in Tier 2 - Battle 4.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Flail_of_Ages'
  }
  fancy_spacer
  # ========================================================================== #
  # === Watcher's Keep
  # ========================================================================== #
  fancy2 "Watcher's Keep"
  ptext {
    e ''
  }
  fancy_spacer
  # ========================================================================== #
  # === The red dragon Saladrex
  # ========================================================================== #
  fancy2 'The red dragon Saladrex'
  ptext {
    e "Mordenkainen's Sword should work fine to kill Saladrex. <b>Feeblemind</b>
    (level 5 spell) is also useful."
  }
  fancy_spacer
  # ========================================================================== #
  # === Chapter 7: The Talisman in Suldanessellar
  # ========================================================================== #
  fancy2 "Chapter 7: The Talisman in Suldanessellar"
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Baldur%27s_Gate_II_Chapter_7'
    br
    e 'In order to obtain the "Talisman of Rillifane", use
    the following combination:'
    br
    cmd '- Corellon'
    cmd '- Rillifane'
    cmd '- Water'
    cmd '- Tree'
    cmd '- Suldanessellar # or simpler: 4-1-3-2'
    br
    e 'In the Temple of Rillifane, place the:'
    br
    cmd '(1) "talisman", the'
    cmd '(2) "moonblade", and the'
    cmd '(3) "goblet"'
    br
    e 'on the altar to summon the Avatar of Rillifane.'
    br
    e 'The goblet is kept by the black dragon nearby, so you have to kill
    the dragon first. The talisman is found within a puzzle box in "The
    House of the Talisman", which is located at the bottom of the map.'
    br
    e 'To kill the dragon use "lower resistance" and "pierce magic", then
    "breach".'
    br
    e 'The Avatar will awaken the guardian spirits of the forest and will
    break the seal on the palace gates.'
    br
    e "Next you will have to put the Stone Horn and the Stone Harp on the
    statues by the pool to reveal a staircase to the Tree of Life. The
    Stone Horn can be found inside the House of the Horn and the Stone
    Harp can be found inside the Harpist's House."
  }
  fancy_spacer
  # ========================================================================== #
  # === Jenia's quest in Trademeet - help Tiris:
  # ========================================================================== #
  fancy2 "Jenia's quest in Trademeet - help Tiris:"
  ptext {
    e 'Helping Tiris in Trademeet is a side quest. It can be started
    if the quests Animal trouble in Trademeet, Dealing with the
    Trademeet genies and Solve the "skinner" murders in the Bridge 
    District have been completed.'
    br
    e 'Ask Darsidian Moor where the body of the skinless creature is
    and he and Rejiek will shed the skins they are wearing and
    attack you.'
    br
    e 'Buy a restoration scroll at the temple of Waukeen in
    Trademeet or use a cleric spell to do so.'
    br
    oop_a('https://baldursgate.fandom.com/wiki/Helping_Tiris_in_Trademeet',
          description: :copy,
          css_class:   'mars2em BOLD',
          new_tab:     true,
          breakline:   true)
  }
  fancy_spacer
  # ========================================================================== #
  # === The Kidnapping of Boo (a side quest, an add-on quest):
  # ========================================================================== #
  fancy2 "The Kidnapping of Boo (a side quest, an add-on quest):"
  ptext {
    e 'Eleanya can be found at the lone fountain, just south-west of
    the Government Park square to which Smethy teleports the party.'
    br
    e "A diplomatic party can agree to play Eleanya's riddling game
    for ownership of Boo."
    br
    e 'The <b>correct answers</b> to the riddle are:'
    br
    cmd '  - "Noise".'
    cmd '  - "Cabbage".'
    cmd '  - "You need no gem".'
    br
    e 'If you only get one riddle correct, then the party will be
    rewarded with 10000 EXP, plus the return of Boo.'
    br
    e "Get at least two riddles correct and the party will be
    rewarded with 15000 EXP and the Jade Hound Figurine, which
    can summon an Astral Hound to fight at the party's side
    once per day, plus the return of Boo."
    br
    e 'Get all three correct, and the party will be
    rewarded with 20000 EXP and Minsc will gain the ability
    "Boolets", which lets him summon a hamster once per
    day. Plus the return of Boo.'
    br
    e 'Get all answers wrong, and you get no EXP, but Boo is
    returned to you.'
    br
    e "Once the noblewoman leaves, one way or the other, two Cowled
    Enforcers will teleport in and thank you for getting rid of
    the arrogant wench."
    br
    e 'They will also ask if you have a magic license; if not,
    they will grant you one, otherwise they give you 1000
    gold pieces.'
    br
    oop_a('https://baldursgate.fandom.com/wiki/The_Kidnapping_of_Boo',
          description: :copy,
          css_class:   'mars2em BOLD',
          new_tab:     true,
          breakline:   true)
  }
  fancy_spacer
  
  
  # ========================================================================== #
  # === The Rhynn Lanthorn (a lantern)
  # ========================================================================== #
  fancy2 'The Rhynn Lanthorn (a lantern)'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Rhynn_Lanthorn'
    br
    e 'This item can be obtained from Bodhi if the party kills her
    with a wooden stake after fighting her - go to her coffin
    for this, which is northeast from where she dies. The
    lantern is needed to gain access to Suldanessellar.'
    br
    e 'Once obtained, the lantern should be brought to <b>Elhan</b>.'
  }
  # ========================================================================== #
  # === Sister Farielle
  # ========================================================================== #
  fancy2 'Sister Farielle'
  ptext {
    e 'Approach her with a non-evil character and she will hand over a
    key.'
  }
  fancy_spacer
  fancy_spacer
  # ========================================================================== #
  # === Nalia is abducted (Nalia tag)
  # ========================================================================== #
  fancy2 "Nalia is abducted (Nalia tag)"
  dtext {
    e 'To solve the quest Nalia being abducted, do the following:'
    br
    e "- Go to the \"Docks\" area in Athkatla. Find Barg near the end
    of the \"Sea Bounty Tavern\" stairs. Speak to him, and he will
    tell you he is deep into pirating, and that Isaea is footing
    the bills. He also burps out that Officer Dirth is a slaver.
    Dirth is in the \"<b>Sea Bounty Tavern</b>\", on the lower floor.
    Kill him (or steal it) and pick up Isaea's Slavery Document off
    his body."
    br
    e '- Next go to the "Government" district and enter the "Roenall
    Estate" just northwest of the main government building. Collect
    "Isaea\'s Financial Statements" from a drawer in the western
    most room.'
    br
    e '- Next go to the "Council of Six Building" nearby. Speak
    to Corgeig Axehand. Corgeig is Isaea Roenall\'s superior
    and initially refers you to Isaea. However, with Barg\'s
    testimony, the Slavery Document, and the Financial
    Statements, Corgeig agrees to investigate.'
    br
    e 'Isaea and Nalia appear on the scene. Isaea, despite
    his protests, is relieved of all duties indefinitely,
    and Nalia is back and ready to rejoin the party.
    Each party member, except Nalia, receives 7000 XP.'
    br
    e 'See also:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Nalia_abducted_by_Isaea_Roenall'
    ntab 'https://baldursgate.fandom.com/wiki/Ruling_the_de%27Arnise_Keep_and_Lands'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Shadow Thieves
  # ========================================================================== #
  fancy2 'The Shadow Thieves'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Baldur%27s_Gate_II_Chapter_3'
    br
    e '<b>Mook</b> will be killed.'
    br
    e 'Once you have defeated Lassal, report to Aran Linvail
    in the Shadow Thief Guildhall.'
    br
    e "Now go to the Graveyard District and enter one of the
    entrances to the Lower Tombs. Fight past Pai'Na's spiders
    and meet Haz at the entrance to the vampire's lair - the
    north side of the lower tomb."
    br
    e "His Golem will break down the door, but you will
    be attacked and Haz will be killed. Follow Lassal
    to the inner sanctum. Defeat the vampires there and
    confront Lassal in the back room. He will flee again.
    Return to the entrance of the vampire's lair and 
    enter the hallway to the east. You will have to
    fight two powerful Tanova's to get through. Lassal
    will finally attack you in the room with the
    spikes in the ground. Beware of traps!"
    br
    e "Once you have defeated Lassal, go to the room
    with the three coffins on the west side of the
    area. Use blunt weapons to destroy the Golem.
    Click on each of the coffins to use a wooden stake
    to finish off the vampires. The top two coffins
    are Gellal's and Durst's and the bottom one
    is Lassal's. Bodhi will appear once you have
    finished off Lassal. Only blunt weapons will
    work against her. Once you have hurt her
    enough, she will leave. Return to Aran Linvail
    in the Shadow Thief Guildhall and he will
    book you passage on a ship which will take
    you to the island where Imoen and Irenicus
    are being held by the Cowled Wizards."
  }
  fancy_spacer
  # ========================================================================== #
  # === The Cowled Menace                                         (cowled tag)
  # ========================================================================== #
  fancy2 'The Cowled Menace'
  ptext {
    e 'This subsection contains hints about <b>The Cowled Menace</b> mod.'
    br
    e 'The quest begins by the party venturing to the <b>Graveyard District</b>,
    the very top-right corner on that map (go right, then north). The party will
    meet someone there (an elven magician), so this marks the beginning of the
    <b>Cowled Menace</b> quest.'
    br
    e 'Additional hints can be found during the <b>Tanner quest</b>, where the
    party will find a letter pointing to Umar Hills, where a shady seller awaits
    a secret word. Going there and interacting with this seller - his name is
    <b>Fael</b> - the party will learn that he is affiliated with the
    <b>Twisted Rune</b>.'
    br
    e 'The general take-away of this is that there is evidently a <b>Twisted
    Rune affiliated-agent</b> in Umar Hills, which is the important part.'
    br
    e "Upon returning from the Shade Lord's temple, the party will have
    a <b>Rogue Stone</b>; Merella had one on her. Clearly she was onto
    Fael before the Shade Lord got to her."
    br
    e "The rogue stone will start glowing and vibrating in the Umar Hills
    town, indicating that something is up. Much like the Enclave in the
    Bridge District, a Rogue Stone allows the party to access a Twisted
    Rune enclave. This enclave is a bit different to the one in the
    Bridge District, with different actors.'
    br
    e 'The entrance to this enclave is located just west of the Inn,
    then more to the south, on the other side of the cliffs next to
    the road leading out of the area. Enter this area (which will
    happen automatically once the party is close) and clear the
    enclave, if you can."
    br
    e "In the meantime, after solving the Tanner murders in the Bridge
    District, you will either get ambushed by the Wizard who helped
    the Tanner later in the same district (he drops information concerning
    the building and the Rogue Stone necessary to enter), or you go to
    the Temple District, into the Guarded Compound, and battle the party
    there. On your way out, a Twisted Rune party will ambush you, revealing
    information if you have found Koshi's letter (2nd floor), or telling
    you to do so if not. The letter reveals that the building next to
    Delosar's Inn is suspicious. Head to that building in the Bridge
    District, enter through the door with a Rogue Stone found on the
    Tanner Mage's body or anywhere else, and defeat the Twisted Rune
    members inside."
    br
    e 'As soon as you have done pretty much any of the steps above, you
    will have pissed off the Twisted Rune, and will be ambushed by them
    in several places, among which are <b>Brynnlaw</b>, Trademeet, and
    various random encounters in and out of Athkatla.'
    br
    e "Now, once you've cleared either one of the Twisted Rune enclaves
    (you choose which one first), you will meet <b>Laeral Silverhand</b>,
    who was already investigating the Twisted Rune when you arrived and
    blasted them off. She will be focusing her efforts in Baldur's Gate
    as she thinks they are expanding, while you keep on investigating
    in Athkatla for evidence that links the Twisted Rune with the Cowled
    Wizards. What you do next is up to you."
    br
    e "If you haven't done so already, your first option is to
    head to the Twisted Rune enclave you haven't cleared yet,
    and clear it. Once they are dead, you will again meet Laeral
    and will now know who among the Cowled Wizards has had
    dealings with the Twisted Rune. Her name is Zallanora.
    Laeral will tell you that Zallanora will probably ambush you
    at some point since you pissed her or her allies off royally.
    Which leads us to your second option..."
    br
    e "Your second option is to investigate the Cowled Wizards
    directly. You won't get very far by just talking to them in
    the Council Building, so you really have to fight them until
    the end so that you get to battle their leaders. How to do
    this: simply cast spells anywhere outdoors in the city, and
    battle through their ranks until the bosses come out. You
    will fight the contact, Zallanora, who will flee. If you have
    Bribed the Cowled Wizards, Zallanora will instead appear in
    the Twisted Rune fight accessed  in the Umar Hills, making the
    fight much harder as she is a level 36 wizard with better AI
    than vanilla. In SCS she is a standard level 36 wizard as SCS
    replaces the AI I gave her. Don't worry, if you've already
    bribed the Cowled Wizards and done that fight, you can still
    progress in Chapter 6."
    br
    e 'Regardless of the option you choose, you have to battle Zallanora
    at some point and have her flee, either in Umar Hills or Athkatla,
    before you can continue. Paying the spellcasting license also works,
    but at the cost of skipping one fight overall. Now you simply wait
    for her to regroup with the Twisted Rune and ambush you.'
    br
    e "Thus, the only (vanilla) way to move forward with the quest at
    this point is to actually reach chapter 6 and come out of the
    Underdark. Unless you somehow can reach Small Teeth Pass, that is.
    Anyway, that's not possible in vanilla, so chapter 6 it is."
    br
    e 'The above information has been adapted from:'
    br
    ntab_ntab 'https://raw.githubusercontent.com/Gibberlings3/CowledMenace/refs/heads/master/SPOILERS-SECTION.md'
  }
  fancy_spacer
  # ========================================================================== #
  # === Skull of the Lich
  # ========================================================================== #
  fancy2 'Skull of the Lich'
  ptext {
    e 'The Skull of the Lich is a component that must be given to
    Cespenar in the Pocket Plane in order to improve the abilities
    of the powerful blade Spectral Brand.'
    br
    e "The Skull of the Lich can be found inside a container in
    \"Odamaron's Lair\" (within Sendai's Enclave)."
    br
    e "The spectral brand can be obtained on the third floor of
    Watcher's Keep from the cambion Aesgareth with the Deck
    of Many Things."
  }
  fancy_spacer
  # ========================================================================== #
  # === Obtaining the coordinates of the game
  # ========================================================================== #
  fancy2 'Obtaining the coordinates of the game'
  ptext {
    e 'Press "X" if you are playing the Enhanced Editions.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Szass Tam
  # ========================================================================== #
  fancy2 'Szass Tam'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/Szass_Tam'
  }
  fancy_spacer
  # ========================================================================== #
  # === How to defeat The Ravager:
  # ========================================================================== #
  fancy2 'How to defeat The Ravager:'
  ptext {
    e 'Use a weapon like the <b>Soul Reaver</b>.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Throne of Bhaal - "The Graveyard Lich"
  # ========================================================================== #
  fancy2 'Throne of Bhaal - "The Graveyard Lich"'
  ptext {
    ntab_ntab 'https://baldursgate.fandom.com/wiki/The_Graveyard_Lich'
    br
    e 'If the party saves Marlowe and kills the lich (Vongoethe will summon
    several skeletons, Skeleton Archers, and Banshees which can cast Wail
    of the Banshee) you will get 15,000 XP and a Reputation point.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Korgan and his quests:
  # ========================================================================== #
  fancy2 'Korgan and his quests:'
  ptext {
    ntab 'https://baldursgate.fandom.com/wiki/The_Hunt_for_Valygar_Corthala'
    ntab 'https://baldursgate.fandom.com/wiki/Korgan_Bloodaxe'
    ntab 'https://baldursgate.fandom.com/wiki/Help_Korgan_Recover_the_Book_of_Kaza'
    br
    e 'Quest #1: Help Korgan Recover the Book of Kaza'
    br
    e 'Korgan wants to go to the "Temple District" to
    the home of the Book Dealer after the visit to the
    tomb. Here he should meet the book-collector
    called Pimlico himself.'
    br
    e 'This has to go through a fight on the roof
    of the Copper Coronet (8750 exp). To the
    Slums!'
  }
  fancy_spacer
  # ========================================================================== #
  # === Triple-classing in BG2
  # ========================================================================== #
  fancy2 "Triple-classing in BG2"
  ptext {
    e 'The only possibilities for triple-classing are:'
    br
    cmd '(1) Fighter/Mage/Thief, and'
    cmd '(2) Fighter/Mage/Cleric.'
    br
    e 'Only half-elves can take this triple class combination.'
    br
    e 'Max intelligence is a must, as is 16 CON. Because you require so
    many different stats to be viable, it may be worth dumping DEX down to 7
    and relying on the Gauntlets of Dexterity to bolster that. This allows
    you not to skimp on STR or WIS. There is no way your charisma will be
    above 3 on this character, though.'
    br
    e "Warhammers are the most versatile weapon type you'll have access
    to, so pick it up. Slings are a must as well, obviously."
  }
  fancy_spacer
  # ========================================================================== #
  # === The Crooked Crane Inn
  # ========================================================================== #
  fancy2 "The Crooked Crane Inn"
  ptext {
    e "The Crooked Crane Inn is an inn in Athkatla's City Gates district."
    br
    e 'In the north there is a secret room with a <b>lich</b>.'
    br
    e 'See also:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Crooked_Crane_Inn'
    ntab 'https://sorcerers.net/community/threads/the-lich-underneath-the-crooked-crane-inn.2967/'
  }
  fancy_spacer
  # ========================================================================== #
  # === Abazigal the chromatic blue dragon Bhaalspawn:
  # ========================================================================== #
  fancy2 "Abazigal the chromatic blue dragon Bhaalspawn:"
  ptext {
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/ToB/chapter-9/quests/kill-abazigal.php'
    br
    e 'This blue dragon is really strong. The fastest way to kill this dragon
    in human form is via fire shield. Protection from magical weapons has
    to be used as well. Protection from lightning gear helps too (or the
    spell protection from lightning, which is a 4th level priest spell).'
    br
    e 'Spell Immunity: Abjuration should be cast before talking to
    this dragon, to prevent these spell effects from getting
    dispelled.'
    br
    e 'All party member should be under effect of "remove fear".'
    br
    e "Also, Mordenkainen's Swords are completely immune to
    Abazigal's weapon-based attacks. The Harper Pin also
    will yield 100% electricity resistance."
  }
  fancy_spacer
  # ========================================================================== #
  # === The Silver Sword
  # ========================================================================== #
  fancy_h1('The Silver Sword') {{
    use_this_image: BALDURS_GATE_LOGO
  }}
  ptext(id: 'The_Silver_Sword') {
    ntab 'https://baldursgate.fandom.com/wiki/Silver_Sword'
    br
    e 'This +3 sword is gained by bringing the Silver Blade,
    Silver Hilt and 7500 gp to Cromwell in the Athkatla Docks.'
    br
    e 'Sarevok would benefit from this sword quite a bit,
    for instance.'
  }
  # ========================================================================== #
  # === How to defeat Melissa
  # ========================================================================== #
  fancy2 "How to defeat Melissa in Baldur's Gate II"
  ptext {
    e '- Very early on, hit the space-key and clone all mages
    via simulacrum. Try to position the simulacrum a bit
    before the real mage, as additional protection.'
    br
    e '- A spike trap can be set early on.'
    br
    e '- After the first battle, you can lay Spike Traps at
    the same spot Melissa started at. A clone can be used
    to do this.'
    br
    e '- If you are in dire need of a rest, there is a way to regain spell slots
    and daily item abilities while in the final battle. Using the 9th level
    spell "Wish" in conjunction with a Potion of Insight, one can repeatedly
    wish until the option appears to have the party be restored as if they
    had rested for 8 hours. This option has a 20% chance to show up, so it
    is advisable to cast it multiple times from Project Image or Simulacrum,
    if possible with scrolls of Wish, in order to "erase" most of the
    randomness.'
    br
    e "- Mages should reorient their spellbooks to tear down magical defenses
    via:
      Dispel Magic, Breach, Pierce Magic,
      Ruby Ray of Reversal.
    Also, summon creatures for help, in particular the Planetars. You
    won't need many offensive spells; Melissan and her summoned creatures
    will be immune or next to immune to most of them."
    br
    e '- Healers concentrate on spells for healing and protection,
    including negative Plane protection, heal spells and
    resurrection spells and summoning (Summon Deva).'
    br
    e '- Bring along as many Wands of Spell Striking if
    you can.'
    br
    e '- Bring the healing potions you have gathered throughout the
    game.'
    br
    e "- If your fighters are unable to hit and thus hurt Melissa,
    use a Breach spell or a Wand of Spell Striking. It is important
    to stay on top of her, or she will cast Time Stop and
    proceed to beat one of your characters into the ground."
    br
    e '- Always kill wraiths first, due to their level
    drain ability.'
  }
  
  # ========================================================================== #
  # === The prophecy of Sekolah
  # ========================================================================== #
  fancy2 'The prophecy of Sekolah'
  ptext {
    e 'The Senior Priestess Sallinithyl tends to disappear.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/The_prophecy_of_Sekolah'
    ntab 'https://forgottenrealms.fandom.com/wiki/Sallinithyl'
  }
  # ========================================================================== #
  # === Companion quests in Throne of Bhaal
  # ========================================================================== #
  fancy2 'Companion quests in Throne of Bhaal'
  ptext {
    e "<b>Neera</b>:  Walk near the merchant in outside Saradush to trigger
    the dialog. Also in Bathazar's city there is an event when you
    enter the Inn."
    br
    e '<b>Dorn</b>: keep him in the party for some period of time, for
    about 1-2 weeks. The event triggers as you travel the world map.'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Dorn%27s_bloody_path#Throne_of_Bhaal'
    br
    e "Rasaad: triggers between the oasis and Bathazar's city."
    e 'See:'
    ntab 'https://gamefaqs.gamespot.com/ps4/258145-baldurs-gate-ii-enhanced-edition/faqs/78723/chapter-8-companion-quests'
    br
    e "Hexxat: triggers in Bathazar's city when you enter the inn."
  }
  fancy_spacer
  # ========================================================================== #
  # === Yoshimo's Heart
  # ========================================================================== #
  fancy2 "Yoshimo's Heart"
  ptext {
    e "Yoshimo's Heart needs to be taken to any temple of Ilmater.
    There is a temple dedicated to this deity on top of the Copper
    Coronet in the Athkatla Slums, and another one in 
    \"Waukeen's Promenade\". For this simple deed, the party
    will receive 200,000 XP, and it will help Yoshimo's soul
    greatly."
    br
    e 'See '+HtmlTags.a(
      'https://baldursgate.fandom.com/wiki/Yoshimo%27s_Heart'
    )
  }
  fancy_spacer
  # ========================================================================== #
  # === Immunity to Fear
  # ========================================================================== #
  fancy2 "Immunity to FearGems in Baldur's Gate II"
  ptext {
    e '<b>Demon Fear</b> can be extremely annoying. It can easily
    disrupt the whole party in its own right.'
    br
    e 'One useful strategy here is to make use of a level 12 mage. In the
    room before entering the room with Demon Fear, have the mage cast
    the level 6 spell called "contingency". Then choose the Level 2 Mage
    spell called "Resist Fear" and set it to go off whenever an enemy
    is seen. Chain Contingency presumably works as well and may get
    some other useful spell off too, whatever you choose, but once
    Resist Fear is working, the room is very easy.'
    br
    e 'If your mage has a Stoneskin Contingency set up already, have
    some fun and beat him up to get rid of it.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Gems in Baldur's Gate II
  # ========================================================================== #
  fancy2 "Gems in Baldur's Gate II"
  ptext {
    e "What is the use case of of gems in Baldur's Gate II? (gems tag)"
    br
    e "- Gems can be sold. Other than that they are useless. Past
    the Waterstar Gem the gems seem to be worthy, gold-wise. The
    rogue stone has special uses in Baldur's Gate 2."
    br
    e 'Typical <b>cost table for gems</b>, in gp and where it may be found:'
    br
    table3('mars1em pretty_spacer FS1em','','',
      '<b>Name of the gem</b>','<b>cost of the gem</b>','<b>where the
       gem can be found normally</b>',
      '<b>Turquoise Gem:</b>','5',"can be found in Mae'Var's Guildhall,
       in the barrels on the first floor, and the <b>red kidnappers</b>
       in the bridge block area",
      '<b>Fire Agate Gem:</b>','10','unknown',
      '<b>Lynx Eye Gem:</b>','15','',
      '<b>Andar Gem:</b>','30','unknown',
      '<b>Jasper Gem:</b>','35',"can be found in Cromwell's Home",
      '<b>Skydrop Gem:</b>','40',"unknown",
      '<b>Waterstar Gem:</b>','80','unknown',
      '<b>Garnet Gem:</b>','175',"unknown",
      '<b>Sphene Gem:</b>','225',"unknown",
      '<b>Water Opal:</b>','350',"unknown",
      '<b>Moonbar Gem:</b>','375','not known where it can be found',
      '<b>Beljuril</b>:','600','very rare gem; can be found in Windspear
       Hills; could be used for the Iron Horn of Valhalla',
      '<b>Star Sapphire</b>:','1200','could be used for the Dagger
       of the Star +5 or the Wondrous Gloves',
      "<b>King's Tears</b>:",'1200','could be used for Bag of Plenty +2
       recipe; can be found by The Master Brain and in the Planar Sphere
       (Engine room)',
      '<b>Emerald:</b>','1500','could be used for Cespenar Wondrous Gloves
       recipe. Two emeralds are dropped by Lehtinan after the Free
       Hendak and the slaves quest has been completed.',
      '<b>Rogue Stone:</b>','5000','unknown',
      '<b>Diamonds:</b>','','unknown'
    )
    br
    e "Star Sapphires can be found in the De'Arnise Keep (ground floor, in a toilet) as
    well as in a locked chest in the house north-east of the <b>Five Flagons Inn</b> in
    the Bridge District of Athkatla."
    br
    e "In <b>SoA</b>, the King's Tears can be found by the <b>Master Brain</b> and
    in the engine room of the Planar Sphere. <b>Merella</b> will also drop a King's
    Tear when she dies."
    br
    e 'See the following link:'
    br
    ntab 'https://baldursgate.fandom.com/wiki/Gems'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Asylum - how to escape                                (asylum tag)
  # ========================================================================== #
  fancy2 "The Asylum - how to escape from it"
  dtext {
    ntab 'https://baldursgate.fandom.com/wiki/The_Asylum'
    ntab 'https://baldursgate.fandom.com/wiki/Escaping_the_asylum'
    ntab 'https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-4/areas/asylum-dungeon-1.php'
    ntab 'http://mikesrpgcenter.com/bgate2/maps/ar1516.html'
    ptext {
      e 'Note that one of the <b>kobolds</b> carries a wooden stake.'
      br
      e 'The Statue item riddle (Reward: 20,000 experience points, Sapphire
      Stone, and a Dusty Rose Ioun Stone):'
      br
      e 'Riddle 1: Try to defeat me but try in vain. When I win, I end
      your pain.'
      br
      cmd 'Solution: Grinning Skull'
      br
      e 'Riddle 2: I have two heads but one body. The more I stand
      still, the faster I run.'
      br
      cmd 'Solution: Hourglass'
      br
      e 'Riddle 3: Always I do tell the truth, yet cannot speak. Look to
      me and see what really is.'
      br
      cmd 'Solution: Mirror'
      br
      e 'Riddle 4: Name me and so shall you break me.'
      br
      cmd 'Solution: The Gagged Man.'
      br
      e 'Riddle 5: I will save your life, but yet you can die
      by me. I settle disputes yet not with words.'
      br
      cmd 'Solution: Sword Medallion.'
      br
      e 'Riddle 6: To those within the dungeon I am joy. To
      those fully beneath my gaze, I can be Hell.'
      br
      cmd 'Solution: Sun Medallion'
      br
      e 'Riddle 7: I have seen the mountains rise. I have seen
      the fall of Netheril. You shall die but still shall
      I march on.'
      br
      cmd 'Solution: Sundial'
    }
  pre '

Riddle 8: Here, in this place, you swallow me. Yet, if I were more, I
          would swallow you.
  Solution: Jar of Water.

Riddle 9: Two brothers we are, great burdens we bear, all day if we are
          bitterly pressed; yet this will I say - we are full at day, 
          and empty when we go at rest.
  Solution: Worn-out Boots.

Riddle 10: No beginning. No end. I am a symbol of the world\'s cycles.
  Solution: Golden Circlet

Riddle 11: At night I come without being fetched, at day I
           am gone without being stolen.
  Solution: Star Medallion 

One of the kobolds will drop a wooden stake.

The minotaur horns can be found here:

- One horn can be found in a vase, next to the four minotaurs.

The twelve riddles in The Asylum:

See: https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-4/areas/asylum-dungeon-1.php

"They follow and lead, but only as you pass. Dress yourself in
darkest black, and they are darker still. Always they flee the
light, though without the sun there would be none."
– Shadows.

"I have holes throughout, from back to front and top to bottom to
core. More nothing that something within, and yet I hold water."
– A sponge. # 2

"I am free for the taking through all of your life, though given
but once at birth. I am less than nothing in weight, but will
fell the strongest of you if held."
– Breath. # 5

"Alive as you but without breath, as cold in my life as in my death;
never a thirst though always I drink, dressed in mail but never a 
clink."
– Fish.

"Of all your possessions, I am the hardest to guard. If you have
me, you will want to share me. If you share me, you no longer
have me."
– A secret.

"I can have no color, though there may be darkness within. I have
no weight and hold nothing, and if placed in a container, it
becomes all the lighter."
– A hole.

"Lighter than what I am made of, more of me is hidden than is
seen. I am the bane of the mariner, a tooth within the see.
Speak my name."
– Ice.

"The more that there is, the less that you see. Squint all you wish when
surrounded by me."
– Darkness.

"They come to witness the night without being called, a sailor\'s
guide and a poet\'s tears. They are lost to sight each day without
the hand of a thief."
– Stars.

"A spirited jig it dances bright, banishing all but darkest night.
Give it food and it will live; give it water and it will die."
– Fire.

"The life I lead is mere hours or less, I serve all my time by
being consumed. I am quickest when thin, slowest when fat, and
wind is the bane of the gift that I bring."
– A candle.

"The man who invented it, doesn\'t want it for himself. The man
who bought it, doesn\'t need it for himself. The man who needs
it, doesn\'t know it when he needs it."
– A coffin.

For answering all riddles correctly, each party member receives
5,000 XP and you also get a Ring of Regeneration.

The mithral token machine ("Boot Machine"):

    Number of tokens  Item received
           5           Boots of the North – The Frost\'s Embrace
          10           Boots of Grounding – Talos\'s Gift
          15           Boots of Speed     – The Paws of the Cheetah
          20           Chainmail +4       – Jester\'s Chain 

The riddles of the Apparition in The Asylum, aka the second test

When the party arrives at the second test area, you must kill a Spore Colony, after which
the apparition will once again appear to ask you a riddle. The answer to this riddle is
"A Splinter", and after answering correctly, the you will be teleported to the next area.
'
    # ================================================================ #
    # === The third test in the asylum (the dining room)
    # ================================================================ #
    fancy3 'The third test in the asylum (the dining room)'
    ptext {
      e 'The third test area occurs in a small room with
      a large banquet table. First, search the table to
      find a <b>Cloak of Reflection</b>. Next speak to
      the apparitions sitting in chairs around the
      room to be presented with more riddles.'
      br
      e 'The correct sequence is 3,6,7,3:'
      br
      cmd '"Nothing", "river", "Fear" and "Memory". # aka 3-6-7-3'
    }
    ptext {
      e 'If you fail on any of the first few questions, you will be
      teleported to area #7. If you fail on the final question
      (Memory), you will be teleported to area #4. If you answer
      all questions correctly, you will be teleported to area #5.'
    }
    # ========================================================================== #
    # === The Troll Altar
    # ========================================================================== #
    fancy5 'The Troll Altar'
    ptext {
      e 'When the party arrives at the altar, the apparition will appear
      and wants to take the party to the next area.'
      br
      e 'Here one could reject this for the moment. Then one can 
      place the Troll head onto the altar. The room will shake a bit,
      after which a Bone Club +2, +3 vs. Undead will appear on the
      altar. After looting the club, the party can tell the apparition
      that they are now ready to leave and the party will be
      teleported to the next area.'
    }
  }
  fancy_spacer
  # ========================================================================== #
  # === Healing potions in Baldur's Gate
  # ========================================================================== #
  fancy2 "Healing potions in Baldur's Gate"
  dtext {
    e 'The best (standard) healing potion is the <b>Superior Healing
    Potion</b>. It can heal up to 40 HP and it can be purchased in the
    Temple of Waukeen in Amkethran.'
    br
    e 'The Potion of Extra Healing can heal up to 27 HP. It is
    sold by <b>Arledrian</b>, Khan Zahraa, the Potions Merchant
    in Ust Natha Bazaar and by Reirra.'
    br
    e "Of these Arledrian is probably the easiest one to get to: he
    resides on the second floor of Gaelan Bayle's Home."
  }
  fancy_spacer
  # ========================================================================== #
  # === Cursed items and curses in the game in general
  # ========================================================================== #
  fancy2 "Cursed items and curses in the game in general"
  dtext {
    e 'Cursed items can be become normal items, by removing
    the curse, in a temple.'
    br
    e 'Alternatively, the spell "Remove Curse" could be used,
    which is a spell for clerics at level 3.'
  }
  fancy_spacer
  # ========================================================================== #
  # === Building golems (golems tag)
  # ========================================================================== #
  fancy2 "Building golems (golems tag)"
  dtext {
    e "The juggernaut golem: this page can be obtained
    from <b>Abazigal's lair</b> (in Throne of Bhaal)."
  }
  fancy_spacer
  # ========================================================================== #
  # === How to approach the Windspear Hills, including Firkraag: (Windspear Hills tag)
  # ========================================================================== #
  fancy2 "How to approach the Windspear Hills, including Firkraag: (Windspear Hills tag)"
  dtext {
    ntab 'https://baldursgate.fandom.com/wiki/Windspear_Hills'
    ntab 'https://baldursgate.fandom.com/wiki/Rescue_Garren%27s_child_from_Firkraag'
    ntab 'https://baldursgate.fandom.com/wiki/Firkraag'
    br
    e 'The dragon <b>Firkraag</b> typically begins the battle by casting
    Remove Magic on any nearby party member with buffs, a useful strategy
    is to approach him with only one party member, following up with the
    rest of the party after Remove Magic is used. This allows up to
    five fully buffed party members to engage the dragon, making
    the fight substantially easier.'
    br
    e 'Also, fire resistance 100% is important, as well as immunity
    to fear (level 1 cleric or level 2 mage).'
    br
    e "You can either take the melee approach or the magic
    approach. The magic approach may be more effective, but
    you may be a bit limited in the arcane department. Minsc
    and Valygar are probably only good for 3-4 hits each so
    you may want to hold them back with bows or throwing
    axes. Have your kensage protect himself with Stoneskin,
    Mirror Image (I forget whether dragons can see through that) and
    PfMW (don't cast PfMW at the beginning since he will probably
    buffet you and waste half the spell). Jaheira can join in with
    her Ironskins. Preferably you would be Improve Hasted but
    with only two level 6 slots I would keep them both for
    PfMW so use normal haste."
    br
    e 'You would cast Lower Resistance 3 times (very important),
    then Malison and Doom, then pelt him with damage spells
    (or instant death spells - see Chromatic Orb). This may
    still be simpler but your kensage is the only one casting
    so its going to be 5 or 6 rounds at least, try putting
    two Chromatic Orbs in a minor sequencer.'
  }
  fancy_spacer
  # ========================================================================== #
  # === How to fight against vampires                           (vampires tag)
  # ========================================================================== #
  fancy2 "How to fight against vampires"
  dtext {
    e 'The Vampire Domination gaze attack is very nasty, so counter-strategies
    against this are the Enrage ability, a Chaotic Commands spell or the
    Helm of Charm Protection. To protect yourself against the drain strikes
    use the priest level 4 spell called Negative Plane Protection.'
    br
    e 'Characters utilizing the protected from undead scroll
    will not be attacked by vampires at all.'
  }
  fancy_spacer
  # ========================================================================== #
  # === The Twisted Rune Building, Shangalar's hideout
  # ========================================================================== #
  fancy2 "The Twisted Rune Building, Shangalar's hideout"
  dtext {
    ntab 'https://baldursgate.fandom.com/wiki/Twisted_Rune_Building'
    br
    e "This house is in Athkatla's Bridge District, serving as a base
    of operations for the Twisted Rune during the time of Shadows of
    Amn."
    br
    e 'The entrance is southeast of the Temple of Helm, behind a
    locked door. This door cannot be passed without holding a
    Rogue Stone, which gets consumed by the portal. The
    Staff of the Magi can be found here.'
  }
  fancy_spacer
  # ========================================================================== #
  # === How to create mods in Baldur's gate2
  # ========================================================================== #
  fancy2 "How to create mods in Baldur's gate2"
  dtext {
    e 'Check for a specific item in the party:'
    br # if party.has_item?
    cmd '  PartyHasItem("l#rocfi1") # Name goes in the () part.'
    cmd '  PartyHasItem("belt02")'
    cmd '  PartyHasItem("belt03")'
    cmd '  PartyHasItem("belt04")'
    cmd '  PartyHasItem("POTN37")' # Potion of mind focusing.
    cmd "  PartyHasItem(\"MISC4V\") # Mae'Var's Letter"
    br
    e 'A more complete example:'
    br
    cmd '  IF ~OR(2) PartyHasItem("l#rocfi1") PartyHasItem("l#rocfi2") Global("L#ROCFighterForge","GLOBAL",0)~ THEN GOTO L#ROCFI.00'
    br
    e 'A multicheck example:'
    br
    cmd 'IF'
    cmd2 'GlobalTimerExpired("EdwinMae","GLOBAL")'
    cmd2 'Global("MaeVarExposed","GLOBAL",0)'
    cmd2 'Global("Complain","LOCALS",0)'
    cmd2 'InParty(Myself)'
    cmd2 'See(Player1)'
    cmd2 'CombatCounter(0)'
    cmd2 'Delay(10)'
    cmd2 "!PartyHasItem(\"MISC4V\") // Mae'Var's Letter"
    cmd1 'THEN'
    cmd2 'RESPONSE #100'
    cmd2 'StartDialogueNoSet(Player1)'
    cmd1 'END'
    br
    e "Delay a script's execution for 60 seconds:"
    br
    cmd '  Delay(60)'
    br
    e 'Check for the party having 10.000 gp:'
    br
    cmd '  PartyGoldGT(9999) # greater than x'
    br
    e 'Deduct gold from the party via TakePartyGold():'
    br
    cmd '  TakePartyGold(10000)'
    br
    e 'Set a global variable:'
    br
    cmd '  DO ~SetGlobal("TalkedToSarles","GLOBAL",1)~ GOTO 2'
    br
    e 'Check whether a NPC is in the party:'
    br
    cmd '  InParty(Myself)'
    br
    e 'Add XP to the whole party:'
    br
    cmd '  AddexperienceParty(500)'
    br
    e 'Disallow monks from using a specific item:'
    br
    cmd '  WRITE_LONG 0x1e THIS BAND BNOT BIT29'
    br
    e 'Check how often one has talked to a NPC yet:'
    br
    cmd '  IF ~NumTimesTalkedTo(0)'
    br
    e 'Spawn a new enemy:'
    br
    cmd '  CreateCreature("DASSIN",[766.269],0) // Shadow Thief'
  }
  fancy_spacer
  # ========================================================================== #
  # === Links to useful resources
  # ========================================================================== #
  fancy3 'Links to useful resources:'
  ptext {
    oop_a 'https://gibberlings3.github.io/iesdp/scripting/triggers/bgeetriggers.htm',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'http://www.shsforums.net/topic/7219-weidu-how-to-create-a-simple-npc/',
           description: 'How to create a simple NPC (http://www.shsforums.net/topic/7219-weidu-how-to-create-a-simple-npc/)',
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://weidu.org/~thebigg/README-WeiDU.html#sec2',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://github.com/Gibberlings3/modding-resources',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
    oop_a 'https://forums.beamdog.com/discussion/72025/how-to-make-the-dialog-for-an-item-forge',
           description: :copy,
           css_class:   'mars2em BOLD',
           new_tab:     true,
           breakline:   true
  }







--------------------------------------------------------------------------------
Interesting equipment in Baldur's Gate II (items tag, equipment tag, case tag):

  Gem Bag:                            This bag can be bought in the Mae'Var's Guildhall,
                                      in the Bridge District at a Storekeep, in
                                      Gaelan Bayle's Home, in Trademeet at Kich
                                      (northern part of Trademeet) and in the Umar
                                      Hills at Min Minling.
  Moon Dog Figurine:                  only for rangers, such as Minsc. This figurine summons
                                      an animal that fights for the party. The figurine can
                                      be obtained by solving the following quest:
                                        https://baldursgate.fandom.com/wiki/Ranger-Protector_of_the_Umar_Hills
  The Hands of Takkok:                dropped by a halfling in "Lavok's Sphere". They
                                      will set the strength of the wielder to 18/00. They
                                      are also known as "Gauntlets of Ogre Power".
  Crom Faeyr:                         a +5 warhammer. Your STR will be set to 25 wielding
                                      it. Made by Cromwell from 4 components, which are
                                      the Hammer of Thunderbolts, Gauntlets of Ogre
                                      Power, Girdle of Frost Giant Strength, and
                                      the Crom Faeyr Scroll for 10,000 gp.
                                      The Crom Faeyr Scroll is dropped by the dragon
                                      Thaxll'ssillyia in the Temple Ruins of Amaunator.
  Spectral Brand:                     Can be obtained from the maze in the Watcher's
                                      Keep. It is a +4 scimitar, but it can be upgraded
                                      to a +5 scimitar lateron if the Skull of the Lich
                                      has been obtained from Sendai's Enclave. The
                                      scimitar can be used to summon a blade and let it
                                      fight for the party. Jaheira can use it as well.
                                      See here for more details:
                                        https://baldursgate.fandom.com/wiki/Spectral_Brand
  Golden Ioun Stone:                  gives +1 INT, sold by Lazarus in the Arcana
                                      Archives.
  Talos's Gift:                       boots offering 50% resistance to electrical damage.
  Defender of Easthaven:              a powerful defensive flail, which arguably is
                                      better than a shield. Joluv sells it inside
                                      the Copper Coronet for 35700 gp (depending
                                      on reputation).
  Firetooth:                          a +4 crossbow. It can be bought from Sister Garlena on
                                      the top of Watcher's Keep. 
  Hammer of Thunderbolts:             +3 weapon, one-handed hammer. Can be found in the
                                      "mindflayer dungeon". It can be upgraded into
                                      the powerful Crom Faeyr for 10.000 gold coins at
                                      some point later in the game. Oddly enough only
                                      Cromwell in Athkatla seems to be able to upgrade
                                      this Hammer. The Girdle of Frost Giant Strength
                                      is required, which can only be obtained in ToB.
                                      See:
                                        https://baldursgate.fandom.com/wiki/Hammer_of_Thunderbolts
                                        https://baldursgate.fandom.com/wiki/Crom_Faeyr
  Wand of Wonder:                     This wand can do any of the following:
                                      Flesh to Stone, Lightning Bolt, Normal Haste,
                                      Stinking Cloud, Stoneskin, Web, or the target gets
                                      a Strength bonus of 4 for 4 rounds.
  Iron Horn of Valhalla:              The Iron Horn of Vahalla is crafted by Maheer
                                      the Storekeep (aka "Weaponsmith") in Waukeen's
                                      Promenade after the party gives him the Bronze
                                      Horn of Valhalla, a beljuril, and 5,000 gp.
                                      For the Iron Horn you need the Silver Horn,
                                      which can be found inside the chest that lies
                                      at the foot of the bed, on the 2nd floor of
                                      the Horn House in the "Bridge District", right
                                      after the table displaying two fish. The prior
                                      upgrade can simply be bought for 2.000 gp at
                                      Maheer, and a diamond.
                                      See: https://baldursgate.fandom.com/wiki/Iron_Horn_of_Valhalla
  Boots of Speed:                     They can be obtained from:
                                        → the Bounty Hunter in the Astral Prison
                                        → the "Mithral Token Machine"
                                        → and by killing Renal Bloodscalp in the
                                          Shadow Thieves' Guildhall.
                                        → Lazarus (a shop keeper)
  Doomplate +3:                       This plate mail can be found in the Labyrinth. Three
                                      gems have to be found.
  Peridan:                            a +2 long sword. It provides immunity to fear,
                                      which can be quite useful in some areas. It also
                                      bestows some regeneration, so it is a nifty weapon
                                      that should be retained.
  Thayan Circlet:                     dropped by Vicross; +15% probability that a Wild
                                      Mage's wild surge will have positive effect. 
  Short Sword of Mask:                a +4 short sword; can be bought at the watcher's
                                      keep, for about 39529 GP. There is a 15% chance
                                      that a hit with this weapon can entangle a target
                                      for 24 seconds or four rounds, against the effect,
                                      no save can be made.
  Axe of Hrothgar:                    gives +1 WIS and CHA, sold by Joluv the bonus
                                      merchant.
  Staff of Air:                       Is dropped by the Master of Thralls in the
                                      Planar Prison.
  Gem of Seeing:                      Picked up during the quest Rasaad's Journey.
  Helm of Balduran:                   can be found in chapter I in a chest in the
                                      northern area of the first dungeon.
  Xarrnous second sword arm:          these gauntlets lower the wearer's THAC0
                                      by -1. They can be found at a female Thrall
                                      in the Planar Prison.
  Nymph Cloak:                        gives +2 CHA, sold by "Gorch" in Mae'Vars
                                      guildhall.
  Ring of Human Influence:            gives the wearer charisma 18; it is dropped by
                                      Kalah when he is killed at the end of "Investigate
                                      the circus tent" quest.
  Harmonium Halberd:                  gives +1 STR, sold by Diedre, the bonus merchant
                                      at the Adventurers Mart.
  Robe of Vecna:                      Lowers the amount of time needed to cast spell
                                      by 4 units. Very useful to have.
  Carsomyr:                           Also called The Holy Avenger. Only non-evil characters 
                                      can use this weapon. It can be obtained by slaying the
                                      red dragon Firkraag. In Throne of Bhaal, Cespenar can
                                      upgrade Carsomyr +5 to its +6 version if the protagonist
                                      is willing to use the Eye of Tyr and spend 5,000 gp.
                                      See: https://baldursgate.fandom.com/wiki/Carsomyr
  Paladin's Bracers:                  can be found in the Watcher's Keep, 1st level.
                                      Paladin-only item. Can be further upgraded to
                                      the Blessed Bracers.                                      
  The Army Scythe +1:                 also called Crossbow of Speed. In the Underdark
                                      there are also Drow Crossbows of Speed available,
                                      but they will turn into dust once moving out of
                                      the Underdark again. Not bad but not anywhere
                                      near as useful as the +4 crossbow. 
  Human Flesh:                        basically a Leather Armor +1. It can be upgraded
                                      to Human Flesh +5 if brought to Fael, along with
                                      the Blood of a Silver Dragon which can be
                                      acquired by slaying Adalon in the Underdark.
                                      See https://baldursgate.fandom.com/wiki/Human_Flesh.
  Lilarcor:                           it is a +3 twohander. Can be found early on.
  Jester's Chain:                     a chainmail +4; can be obtained from a machine
                                      in Spellhold when inserting twenty mithral
                                      tokens. Quite useless compared to other armours,
                                      though.
  Celestial Fury:                     a nifty +3 katana. It is dropped by "Koshi" in the
                                      Guarded Compound in Athkatla's Temple District.
  Helm of the Noble:                  Charisma +1 and -1 bonus to armor class. It is
                                      gained as a reward from the first mission for the
                                      Temple of Helm in the Athkatla Temple District in
                                      Athkatla.
  Ring of the Ram:                    does 5-30 points of magic damage to a single
                                      target, bypassing their Magic resistance. It
                                      can be obtained from Tolgerias' corpse, in
                                      Lavok's Sphere. 
  Ring of Regeneration:               can be found at the "Statue of Riddles",
                                      if one answers all 12 questions correctly,
                                      found in the Asylum Dungeon.
  Mace of Disruption:                 Found in a blood pool in Bodhi's Hideout during
                                      chapter 3. Can be upgraded by Cromwell by bringing
                                      him real illithium ore, to a +5 weapon effectively,
                                      for 7,500 gp.
                                      See: https://baldursgate.fandom.com/wiki/Mace_of_Disruption
  Ring of Holiness:                   also known as The Honorary Ring of Sune,
                                      this magical ring gives clerics, druids and
                                      shamans one extra divine spell for each
                                      spell level up to four, totaling in 4
                                      extra spell slots when the priest has
                                      reached level 7. 
  Belm:                               The Scimitar of Speed +2. It can be found in the
                                      ogre tower near the village with animals.
  Duskblade:                          a +2 halberd with some cold extra damage.
  Cloak of Displacement:              sold in Trademeet by one of the merchants
                                      there. It provides a +4 bonus against missile
                                      weapons, as well as a +2 bonus to "Death,
                                      Breath and Wand" saving throws.
  Foebane:                            this is a powerful upgrade-able bastard sword
                                      which inflicts extra damage against certain
                                      enemy types and has a signature drain HP
                                      on-hit ability. It can be found on the first
                                      floor of Watcher's Keep. It is dropped by one
                                      of the "statues" at 8 on the First Level of
                                      Watcher's Keep, close to the altar. When a
                                      target is hit via Foebane a "Larloch's Minor
                                      Drain" is automatically cast, so this weapon
                                      also heals the user. If Fflar's Scabbard is
                                      combined with Foebane then the latter will
                                      become a +5 weapon. The scabbard can be found in 
                                      a locked chest on the second level of the
                                      Saradush prison.
                                      See: https://baldursgate.fandom.com/wiki/Foebane
                                      This very useful ring gives the wearer an extra
                                      level 5, 6 and 7 spell slot. It is dropped by
                                      Nadinal in the "Galvarey Estate" when you return
                                      in connection with the Harper Hold quests. It can
                                      also be crafted in the mod "NPC strongholds", for
                                      the mage stronghold in the Slums district.
  Efreeti Bottle:                     in possession of Taquee, a djinni in Trademeet;
                                      it can be pickpocketed from him.
  Glasses of Identification:          These glasses identify three items per day; sold
                                      by "Arledrian" in the Slums district, at
                                      the second floor of "Gaelan Bayle's home".
                                      Another one can be found by using the
                                      "limited wish spell". It's under one time
                                      use spells then "see things as they truly
                                      are" or something like that.
  Blade of Roses:                     gives +1 CHA, sold by Bernard in the Copper Coronet.
  Vhailor's helm:                     provides simulacrum once per day. Very useful in
                                      general, in particular on warrior-like classes
                                      without simulacrum. It can be purchased, at
                                      "Deidre" in the "Adventurer's Mart", for about
                                      20.000 gp.
  Bag of Holding:                     found in Spellhold Bodhi's Hunt Level 1.
  Club of Detonation:                 Initially a +3 club, but it can be upgraded to
                                      a +5 weapon. It can be found in the Watcher's
                                      Keep, on the fifth floor, by the Aurumach Rilmani. 
                                      See: https://baldursgate.fandom.com/wiki/Club_of_Detonation
  Daystar:                            this +2 sword can be found after defeating the lich in
                                      the gates-district. Daystar is a +4 sword against demiliches
                                      and liches. It can be found in the secret room of the
                                      "Crooked Crane Inn" in the Athkatla City Gates area.
                                      The room is inhabited by a lich, which makes it difficult
                                      to obtain the blade early on.
  Malla's Soul Stone:                 Gives +1 CON and +1 DEX. Dropped/given by Van'Gothe 
                                      the Lich, not usable by Good characters.
  Gauntlets of Extraordinary
  Specialization:                     +1/2 attack/round, +1 THACO, +2 damage.
                                      Y'Tossi on the 5th level of Watcher's Keep
                                      drops it.
  Boots of Etherealness:              These boots allow the wearer to become ethereal
                                      once per day for 5 rounds. Not as good as boots
                                      of the cheetah, but it can be useful as a 
                                      defensive item or when preparing for combat.  
  Girdle of Frost Giant Strength:     STR 21, found in the Underdark after defeating
                                      the Demon Knights, summoned by offering an
                                      animal in the Kuo-Toan dungeons of the Underdark.
                                      It can lateron be used to create the Crom
                                      Faeyr weapon. Sets the strength to 21.
  Girdle of Stone Giant Strength:     STR 20, found in "Suldanesselar", an elven city
                                      in the Forest of Tethir, worn by one Rakshasa.
  Dagger of the Star +4:              This dagger can be found in the Watcher's Keep at
                                      the fourth floor at the east side. It can lateron
                                      be upgraded to a +5 weapon, for 5 star sapphires.
                                      Star sapphires can be found on the Watchers's
                                      Keep's 2nd floor and 3rd floor (AR3013).
                                      There is a chance to turn invisible using this
                                      dagger; at +5 it is 15% and a 5% chance this
                                      dagger deals 1d8 points of fire and electrical
                                      damage after each successful attack.
  Shadow Dragon Scales:               a +6 studded leather with an additional 50%
                                      protection against acid. Cromwell can craft
                                      it for 5000 Gold Pieces.
  Staff of Arundel:                   a +3 Quarterstaff sold by Joluv.
  Tankard:                            restores 3x 2D8 hit points per day. Found
                                      in a quest.
  Book of Infinite Spells:            anyone can cast one spell a day; taken from
                                      "Perth the Adept" in Brynnlaw. Available spells
                                      are: Burning Hands, Farsight, Fireball,
                                      Invisibility, Lightning Bolt, Protection From
                                      Evil, Spell Turning, Stinking Cloud, True
                                      Seeing, Wyvern Call.
  Soul Reaver:                        an enchanted two-handed sword +4.
  The Answerer:                       dropped by Jamis Tombelthen in the Oasis
                                      area. 
  Roranach's Horn:                    dropped by Gromnir Il-Khan when he is killed in
                                      the first chapter of Throne of Bhaal. This helmet
                                      offers the wearer 50% resistance against damage
                                      from crushing attack types. It can also be used
                                      by Cespenar to upgrade the Staff of the Ram. 
  Sword of Grief:                     Abazigal drops this sword. It can be upgraded
                                      via "Heart of the Damned". Note that the Heart
                                      of the Damned can only be used once. It has a
                                      10% chance of inflicting 2d12 Poison damage
                                      with no save on hit, when upgraded, this
                                      two-handed sword is also capable of draining
                                      one level from its target each hit unless the
                                      victim makes successful saves vs. death at +5
                                      penalty.
  Silver Ioun Stone:                  gives +1 WIS, sold by tavern keeper in Amkethran.
  Robe of Goodman Hayes:              this robe provides permanent Chaos Shield 
                                      the on wearer, in return for +1 penalty to 
                                      Armor Class. When Improved Chaos Shield is 
                                      cast, its +25 bonus to the Wild surge roll 
                                      should overwrite that of the Robe of Goodman
                                      Hayes' Shield for the duration of the spell.  
  Ring of Invisibility:               The wearer becomes invisible once per day, until
                                      an attack is made. Can be found at Brennan Riesling
                                      in the Den of the Seven Vales as well as by the
                                      lich in the Crooked Crane Inn.
  Gloves of Pickpocketing:            can be obtained in the Copper's Coronet; yields
                                      +20 pick pocket skill; can be found in "Yarin's
                                      room". 
  Sensate Amulet:                     gives +2 CHA and protection from evil. Can be found 
                                      in Yaga-Shuras Fortress. Can also be bought from
                                      the adventurer's mart, for about 19.000 gold
                                      coins.
  Cloak of Non-detection:             also known as Whispers of Silence, this cloak can
                                      be found in in Waukeen's Promenade, by Amon in the
                                      Den of the Seven Vales.
  Gauntlets of Aln Zekk:              these gauntlets are a quest reward in
                                      the quest called "Rasaad's Journey".
                                      See: https://baldursgate.fandom.com/wiki/Gauntlets_of_Aln_Zekk
  Elder Brain Blood:                  In one of the add-on mods this quest item
                                      will increase the intelligence of the main
                                      actor upon use.
  Dragon's Bane +3:                   a +3 halberd normally, but +6 against dragons.
                                      It can be found in one of the treasure pools
                                      in the Beholder Hideout. 
                                      See: https://baldursgate.fandom.com/wiki/Dragon%27s_Bane
  Mauler's Arm +2:                    sets strength to 18; a +2 maze sold by Bernard
                                      in the Copper Coronet, for 2975 gold coins, 
                                      depending on one's reputation.
  Sword of Chaos +2:                  is given by a Djinni early on in the game.
  Helm of Glory:                      gives +1 CHA, sold by Ribald in the Adventurers
                                      Mart secret stash or acquired by the Temple 
                                      of Helm quest.
  Ring of Regeneration:               carried by Ribald Barterman, if you pickpocket
                                      him.
  Scroll Case:                        can be used to store 100 scrolls. Bernard in the
                                      "Copper Coronet" sells it, as well as Lady Yuth
                                      in the Adventurer Mart, Galoomp's Store
                                      in the Waukeen's Promenade, Wallace (×1) in
                                      Trademeet or Ikert in the Docks District.
  Plate of Balduran:                  gives +1 CHA, sold by Diedre the bonus merchant 
                                      in the Adventurer's Mart.
  Girdle of Bluntness:                can be obtained in chapter I, in the dungeon.
                                      It yields +4 AC versus blunt weapons.
  Staff of Power:                     A unique Quarterstaff +2 that can only be used
                                      by classes which can use mage spells, but not
                                      priest spells. It grants +2 to AC and +2 to
                                      saving throws. 
  Wong Fei's Ioun Stone:              dropped by Sendai. Adds +15 hp and adds
                                      Regeneration. 
  Studded Leather of Thorns +6:       dropped by Sendai after the party defeats her.
                                      See: https://baldursgate.fandom.com/wiki/Studded_Leather_of_Thorns
  Staff of Rhynn:                     a +4 Quarterstaff, sold by "Ribald" in the 
                                      Waukeen's Promenade (Adventurer Mart). This
                                      can be useful for defeating liches early on
                                      in the game.
  Runehammer:                         The Runehammer can be upgraded to a +5 weapon
                                      if the "Rune of Clangeddin" is supplied. The
                                      hammer is dropped by Yaga-Shura when he is
                                      killed, in Throne of Bhaal. It deals extra
                                      damage against undead.
  Boots of Celeritous Stealth:        if you have Boots of Stealth, Boots of Speed, a
                                      Rogue Stone, and 10,000 gp, Cromwell or Cespenar
                                      can combine these items to produce the Boots of
                                      Celeritous Stealth.
  Shuruppak's Plate:                  armour with -2 AC, that also provides +1 DEX.
                                      Dropped by Yaga-Shura.
  Girdle of Hill Giant Strength:      sets to a strength of 19. Sold by Ribald at
                                      the "Adventurer's Mart" in Waukeen's Promenade
                                      in Athkatla, for ~16500 gold coins.
  Angurvadal:                         This +4 longsword sets STR to 22 for 1 turn. The
                                      +5 sets STR to 22 while equipped. Found in Watcher's
                                      Keep. It is upgradable by Cespenar.
  Girdle of Fire Giant Strength:      STR 22, found in Yaga-Shuras fortress.
  Boneblade:                          a +4 dagger. It is dropped by Qilue in her home in
                                      the Drow city of Ust Natha, after she is assasinated.
  Blade of Searing:                   an enchanted bastard sword +3. Can not be
                                      upgraded.
  Blackrazor:                         a +3 long sword. Proccing it gives +4 STR, although
                                      temporarily. Found at the end of SoA during the
                                      "Greed encounter", at the "demon of greed". A creature
                                      hit by this weapon has a 15% chance to have 4 class
                                      levels drained.
  Potion of Genius or Mind Focusing:  Several places offer them. For instance, the
                                      Temple of Ilmatar in the Slums and in the
                                      Waukeen's Promenade. Also Min Minling in the
                                      village of Imnesvale in the Umar Hills,
                                      outside the Umar Inn. 
  Ninjatō of the Scarlet Brotherhood: +3 speed ninjato. It is sold by Joluv, inside
                                      the "Copper Coronet", in the middle of the
                                      tavern, for 26660 gp.
  Axe of the Unyielding:              initially +3; can be upgraded to +5 via "Baalor's
                                      Claw" (from the Marching Mountains temple) and then
                                      yields +1 CON in that event. Forged by Cespenar.
                                      It can be obtained from the Watcher's Keep fourth
                                      floor.
  The Equalizer:                      pommel of the equalizer is needed for this
                                      weapon.
  Bracers of Defense:                 AC: 3 (also sold by Ribald).
                                      See:
                                        https://baldursgate.fandom.com/wiki/Bracers_of_Defense_AC_3
  Breath potion:                      is carried by Ekim Cyre in Abazigal's Lair
                                      Entrance.
  Topsiders's Crutch:                 this ring grants infravision.
  Obsidian Ioun Stone:                provides +1 CON, sold by the guy you save from
                                      Yaga-Shuras Soldiers.
  Purifier:                           a +4 bastard sword that can be found on the
                                      3rd floor in the Watcher's Keep maze. It can be 
                                      upgraded by Cespenar, which requires the Eye of
                                      Tyr and some gold. The Eye of Tyr is found in 
                                      Sendai's Enclave in the room of the lich.
                                      It can be upgraded to a +5 weapon. Once
                                      upgraded it gives the wielder 30% magical
                                      resistance and it can be used twice per
                                      day to cast Dispel Magic and once per
                                      day to cast Mass Cure. 
  Hindo's Doom:                       This katana can be upgraded to +4 by Cespenar,
                                      which requires some gold and Hindo's Hand. The
                                      hand can be found in Abazigal's Lair.
  Storm Star +5:                      This is a powerful mace. It can be found in
                                      the the Machine of Lum the Mad in Watcher's
                                      Keep. Then bring Storm Star +3, Starfall Ore,
                                      and 5000 gold to Cespenar. 
  Rod of Resurrection:                can revive characters; purchase locations are
                                      in the Adventurer Mart and in Mekrath's
                                      Laboratory.
  Red Dragon Scale:                   essentially a full plate mail +2.
  Tear of Bhaal, Test of Wrath:       +1 WIS and CHA for the good outcome, or +2
                                      STR for the evil outcome, which is if you
                                      taunt the Sarevok Wraith to attack you
                                      at the end of SoA.


--------------------------------------------------------------------------------
Strategies against monsters in Baldur's Gate 2 in general:

- The clay golem can only be injured by enchanted blunt weapons.
- The stone golem can only be harmed by +2 or greater enchanted weapons.

--------------------------------------------------------------------------------
Is the greenstone ring and the bloodstone amulet useful?

- Not really. Throw the ring away. The Bloodstone Amulet
  is worth about 90 gold coins, though. 
--------------------------------------------------------------------------------
How to get ressed?

- Go to a temple and resurrect them, by selecting the dead characters 
  portrait and performing the "Raise Dead ritual".
--------------------------------------------------------------------------------
Is the Agni Mani Necklace useful?

- No. Sell it or better discard it. It is as useless as the Laeral's Tear
  Necklace.
--------------------------------------------------------------------------------
How backstab works:

  https://baldursgate.fandom.com/wiki/Backstab

Backstabs can only be performed with fists or melee weapons that
a pure Thief would be able to use:

- long swords
- short swords
- katanas
- wakizashis
- ninja-Tos
- scimitars
- daggers
- clubs
- quarterstaves

Staff of the Ram is a useful item for backstabbing. The Black Blade of
Disaster is even better.


--------------------------------------------------------------------------------
Free Haer'Dalis from Imprisonment by Mekrath: 

  https://baldursgate.fandom.com/wiki/Free_Haer%27Dalis_from_Imprisonment_by_Mekrath

- Watch the terrible performance of the actors in the basement (in the "Bridge"
  District).

  When the play is stopped by the unhappy audience, Raelis Shai will ask if there
  any adventurers who'd be willing to help them.

- Go backstage and speak to Raelis Shai in the bridge district. Agree 
  to find the potential companion Haer'Dalis and the gem for her.

- Next, enter the sewer in "Athkatla Temple". The entrance into 
  Mekrath's Laboratory is behind a secret wall in the northwestern 
  section of the area.

- In one of the rooms, you will find Haer'Dalis, but his
  mind is controlled by the wizard Mekrath, who can be
  found in another room in the same area.

- You have two options, you can do a favor for the mage
  to find his mirror, which was stolen by monsters, which
  can be found in the southeast portion of the sewers and
  he will then release his control on the Haer'Dalis or
  you can try to kill him in combat.

- Once Haer'Dalis is no longer mind-controlled, he offers
  to join the party. You can either let him in your party
  or meet him back at the stage of the Five Flagons Inn.

  If you have a full party but want to have Haer'Dalis in your
  party, do not bother to take him yet as he will leave when
  you get back to Raelis Shai. Take the Portal Gem from the
  altar and bring it to Realis Shai.

- Talk to Raelis Shai and she will give you a reward and they
  reveal who they really are.
--------------------------------------------------------------------------------
Anomen:

  https://baldursgate.fandom.com/wiki/Anomen_Delryn#Quests

Anomen is a companion in Baldur's Gate II.

Anomen Returns Home After his Sister's Death.

Head to the "Delryn Estate" in the Athkatla "Government" and speak 
to Anomen's father, Lord Cor. He will tell Anomen that his sister 
was murdered by his rival Saerk Farrahd and he will demand that 
Anomen avenge her death.

If obeying the law, speak to Bylanna in the Athkatla Government
building and she will tell that there is nothing that can be
done. Athough Saerk will get away with murder, Anomen will
have kept true to his vows and your party will gain an
additional 7,500 XP. 

His wisdom will become 16 if he manages to pass his knighthood
test.

  https://baldursgate.fandom.com/wiki/Anomen_Delryn#Quests
  https://baldursgate.fandom.com/wiki/Anomen_Returns_Home_After_his_Sister%27s_Death

--------------------------------------------------------------------------------
Sarek Farrahd's estate (part of Anomen's quest):

There are the rich, and then there are the filthy rich. The latter
are those who got rich in a filthy way. They enjoy showing off
their wealth by living in a mansion the size of a small city
district with enough guards to form a private army guarding
themselves and their belongings.

But not enough to guard them from a tenacious adventurer with a grudge.

And if you're coming here, it is because somebody holds a grudge.
You will be coming here in connection with the Anomen is Called
Home quest - either to seek revenge for Anomen's dead sister,
whom you suspect was murdered at the order of Saerk Farrahd,
or to stop Anomen from murdering Saerk.

[Saerk Farrahd's Estate, First Floor]

--------------------------------------------------------------------------------
Reputation change in Baldur's Gate 2 (reputation tag):

  https://baldursgate.fandom.com/wiki/Reputation

- Reputation can be gained by donating gold at temples, up to a score of
  18.
- Beggars and the like, especially in the Bridge District, can be killed
  for a drop in reputation. There are also a few houses scattered around
  that are inhabited, and you can safely kill their owners for a
  reputation decrease.
- After the Spellhold dungeon, you will gain the ability to become the
  Slayer. Each time you do so, your rep drops by 2. I've used this
  ability to avoid losing evil characters. Just don't drop too low
  or some really weird things can happen, apparently.
- Charm some commoners/Nobles and lead them to empty buildings where they
  are to be killed.
- Donating 500 gold coins in a temple is enough to raise the reputation
  by +1, if your party's reputation is very low already.
- The maximum (positive) reputation is 20.
- Getting caught picking pockets will lower the reputation by 2. This is
  best done by pick pocketing an isolated person, so that the nearby
  townspeople won't join in trying to chase you with pitchforks.

  Shoplifting will lower reputation as well. Find a secluded merchant,
  preferably at the night - ideally a merchant that you don't want
  to shop from later:

    Promenade has plenty of those
    Bel Dalemark in the Bridge
    fences: in Docks, Slums...
 
--------------------------------------------------------------------------------
Solve the 'skinner' Murders in the Bridge District: 

Bridge District; 68250 XP, 500 gold

- Lieutenant Aegisfield in the north end of the "Bridge District"
  will tell your party about a murderer who skins his victims.

- Speak to "Rose Bouquet" next to the Five Flagons Inn and ask
  her what she knows about the murders. She will tell you
  that she smelled Guril berries or something like that.

- Ask the merchant Bel Dalemark nearby what smells like Guril
  berries and he will give you samples of three things that
  smells like that: Guril berries, Solik berries, and Oak Bark.

- Show these three items to Rose and she will identy the Oak
  Bark as the correct smell. Bel Dalemark has told you that
  Oak Bark is used by the tanner.

- Speak to Rampah, the beggar, northwest of the Five Flagons Inn.
  Pay him some money to buy the Exotic Hide that he found by
  the murder victim.

- Show the Exotic Hide to Bel Dalemark and he will tell you to ask 
  Rejiek the tanner about it. Then, from the Five Flagons Inn, go 
  down to the docks and follow the path to Rejiek the tanner's 
  house (it is marked on the map).

- With both the hide and the smell pointing to Rejiek, he will admit 
  his guilt flee downstairs. You wil recieve 23250 experience.

- Follow him to the next level and you will find lots of bodies. 
  Beware of the traps there. You will also find a shirt made from 
  human flesh and a letter from Rejiek's master.

- On the next level, a mage named Vellin Dahn will flee with Rejiek
  and you will have to fight some enemies.

- Report your finding to Aegisfield at the north end of the Bridge
  District to receive a 500 gold reward and 45000 experience.

See:

  https://baldursgate.fandom.com/wiki/Solve_the_%22skinner%22_murders_in_the_Bridge_District

--------------------------------------------------------------------------------
Hexxat's fourth quest, in the Throne of Bhaal campaign:

  https://forums.beamdog.com/discussion/25663/hexxat-quest-in-throne-of-bhaal-spoilers
  https://www.gamebanshee.com/baldursgateii/quests/hexxat.php
  https://www.gamebanshee.com/baldursgateii/walkthrough/korkorranstomb.php

To continue on the left side, go to the library but not the very
far left shelf, but the one before that.

The door puzzle is a bit tricky: the open/close doors are paired off.
There are the two where you're introduced to the concept initially.
If you look at Naisiem's picture, the two middle open doors are paired
with the closed doors straight past them. That's all of them.

I initially couldn't get those open until I killed the mage surrounded
by spiders. It's possible I did something else in the interim to make
them open, but I'm not sure what it would have been. 

The doors operate only AFTER disabling the barrier. The door to the
room with the barrier switch (down the bottom/southern path) operates
using the same rules, but you have to close the doors using the first
door for it to trigger correctly (if that makes any sense). So, just
make sure you close the doors behind you as you head south to the
switch room. 

Enter the room with the two doors. Hexxat tells you that the two doors
are linked, so that opening one closes another. I'm calling the door
you use to enter Door A, and the door that leads to the necrotic barrier
room Door B.

Have Hexxat enter that room, and then, do NOT open Door A! You can
close Door B manually, without needing to manipulate Door A. Do so,
and the doors out of the barrier room will open so you can keep going. 

--------------------------------------------------------------------------------
Paladin Stronghold Duties:

Rescue Garren's child as intended and do not propose to obtain the landdeed for
Firkraag. Then kill the dragon Firkraag.
--------------------------------------------------------------------------------
Guarded Compound:

  https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-2/areas/temple-district-guarded-compound.php
--------------------------------------------------------------------------------
The Slavers and the Slaver Stockade:

  https://baldursgate2.fandom.com/wiki/Free_Hendak_and_the_Slaves

- When you leave the sewers, you will be confronted by Captain Haegan.
  Kill him and take his key.
- Use the key to open the door in the northeast wall, defeat the
  Trolls, and free the girl.
- Free two more children in cells to the northwest of the exit from
  the sewers.
- Return to Hendak in the Copper Coronet and he will give you a
  reward from the spoils he found from the slavers.
The Dueling Families of Trademeet:

  https://baldursgate2.fandom.com/wiki/The_Dueling_Families_of_Trademeet

--------------------------------------------------------------------------------
The Renfeld quest:

Bring the Poisoned Man to his Friends is a side quest which can be 
started when traveling between the areas of Athkatla in Baldur's 
Gate II: Shadows of Amn.

In one random encounter between areas, you will come across a band 
of thugs attacking a man. The thugs will turn on you and you must 
defeat them.

The poisoned man will ask you to bring him to his friend in the 
Athkatla Docks to the orange building most southwest of the area.

Bring Renfeld's Body to Rylock in front of the building in the 
southwest. The man will then reward you.

This quest is prerequisite for "Find out What Happened to Montaron",
after you bring the body to Rylock (oddly, there seems to be no
timer in this part), attempt to head back north, Xzar will appear
near the stairs to the Sea's Bounty Tavern.
--------------------------------------------------------------------------------
The Illithid Hideout in the Sewers of the main city (mindflayers in the sewers):

  https://baldursgate.fandom.com/wiki/Illithid_Hideout_in_the_Sewers

To open the secret door you need Sewer Key from Tazok in the "Domain of
the Dragon"; his corpse contains that key. The Illithid Correspondence
can be found there as well, but it is not a quest item. The Hammer of
Thunderbolts can be found in this hideout.

--------------------------------------------------------------------------------
Kangaxx and the golden skull (kangaxx tag):

  https://baldursgate.fandom.com/wiki/Restore_Kangaxx%27s_body
  https://baldursgate.fandom.com/wiki/Golden_Arm_and_Leg
  https://baldursgate.fandom.com/wiki/Kangaxx#strategy
  https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-2/areas/sewers-unseeing-eye-cult.php
  https://sorcerers.net/Games/BG2/Walkthrough2/SoA/chapter-2/areas/sewers-unseeing-eye-lair.php

- In the "docks" area: enter the building right between the Sea Bounty and
  Mae'Var's Guildhall. Descend the stairs and click on the sarcophagus where
  Kangaxx is situated in. Kangaxx will ask you to retrieve his other body
  parts so that he may be freed from his eternal imprisonment. In order for
  this to work, one has to acquire his legs, arms and torso. 

- First, go to the Athkatla "Temple" District and descend into the sewers.
  Then go to the "Old Tunnels" in the northwest corner and click on the
  sarcophagus in the north corner.

  Once you have defeated the lich who guarded the body parts,
  click on the sarcophagus once again to retrieve:
      → the Golden Arm and Leg.
  You will need to progress up to a certain stage in the side-quest
  "Find and Destroy the Cult of the Unseeing" in order to access
  the area. Gaal gives you a key. Now it is time to destroy this
  cult.

- Go to the hallway through which you entered the stronghold.
  Open the door on the left side of the entrance hallway (on
  the very same map as Gaal), which requires a key. Go down
  the hallway until you reach the end, where you will find
  Sassar. He will talk to you, tell you a bit about the Cult,
  and say you should retrieve the rod - but not for Gaal.

  After that, go down the south hallway, where you will
  reach the lower levels.

- Three huge spiders will appear. Up ahead is a statue. If 
  you click on it at any time, then two huge spiders and a 
  Wandering Horror will appear. There is a trapped treasure 
  stash in the face of the statue which you can loot without 
  any enemies appearing. Go down the east hallway to find
  six Yuan-ti and one Yuan-ti mage. You may also get many 
  gibberlings or six mummies instead.

  After you have defeated them, continue through the hallway.
  You will reach a large room. There is a broken bridge
  than needs repairing to get across. There is a petrification
  trap on the stairs up to the bridge so make sure to disarm
  that. On the other side there is a stash with Ashideena,
  a warhammer +2 on the southeastern side of the bridge.

- Click on the broken bridge and a guardian speaks to you, aka
  "The bridge has fallen and ends in death". The guardian will
  ask three riddles.

  The correct answers are:

    "Life" "Time", "The current one." # aka 7-9-4

  The two halves of the bridge will then be connected. Go across
  it. On the other side of the structure, there will be a certain
  number of Gauths and/or Beholders, depending on your party's
  level. Skeleton summons work very well against them. 

- Go past the area with the Beholders. Follow the hallway 
  leading north from that area. There is a petrification 
  trap on the center jetty at the end of the hallway.
  Follow the central jetty until you come to a temple.
  The Diseased One will speak to you. After that, enter the 
  temple. You will be attacked by an Emphatic Manifestation. 
  The only way to defeat it is to cast a healing spell or 
  use the rod of resurrection on it. The party will 
  receive 25,750 experience points at this stage.

- After that, an avatar of a fading god will speak with the
  protagonist. It will tell the protagonist about the rod, then
  give half of it in form of the Rift Device Part to him/her.
  On the altar behind it is a treasure stash.

- Retrieving the second half of the rod:

  Exit the Lower Reaches. Once you are back in the tunnel
  that you entered the Lower Reaches through, the man Sassar
  will speak to you again and tell you the next stage of
  the plan - to retrieve the second half of the rod.
  You need to speak to Tad, by the Pit of the Faithless.

  Then go back to where you met Gaal but keep going on this time 
  until you reach Tad. Speak to Tad. Select the first dialogue 
  option ("The eye is blind"; what Sassar tells you to say). 
  He will let you go into the Pit.

- Enter the Pit. Once you are there, battle your way northeast
  through the undead and enter the Lair of the Unseeing Eye.

  Inside the lair many Gauths and Beholders can be found. In the
  centre of the lair there will be a number of blind priests eager
  to fight. In one of the chambers you can find Dragon's Bane, a
  halberd +3. The second Rift Device Part is located in a chamber
  to the south east, it is found inside a node.

  As soon as you pick it up, the two parts of the rod will combine
  into the Rift Device which will appear in Gorion's Ward's
  inventory. The party will receive 26,250 experience points.
  Equip it at once.

- Destroying the cult

  Before the party can head out of the chamber, "the Unseeing Eye"
  will attack. The child of Bhaal can use the rod to weaken his foe
  and easily finish it. Killing it will net 30,000 experience points
  to the party.

- Go west from the Unseeing Eye until you reach a small stairway 
  out. That will deposit you back in the cult stronghold.

- Go back to the diseased ones in the lower levels. You will be taken
  inside the forgotten temple. The avatar of Amaunator will appear
  again and take the rift device off you and give you the Saving 
  Grace shield for your services.

- If you go back to Gaal and the other unseeing eye priests, they
  will be angry you killed their god and will all attack you. Kill
  them if you wish, it is not essential. Gaal carries a girdle of
  fortitude, though.

- Go back to the Temple district and return to the Temple you 
  were hired by, down the staircase. If you are a cleric you 
  will be offered a position in the temple you worked for. If 
  you are not a cleric, you will be rewarded with Ardulia's 
  Fall. 45750 XP per party member and +1 reputation will also
  be awarded, and that brings the end to the quest. 

- Next, the party will find the Golden Torso, in the building "south 
  of Delosar's Inn", in the Athkatla "Bridge" District, guarded 
  by another powerful lich.

- Finally, return to Kangaxx in the "docks" area with the body parts 
  and he will be freed. As a reward, being the evil lich that he is, he
  will try to kill the party for making the effort. First you must beat
  him in his skeleton form. After doing enough damage, he will take a
  demi-lich form. Defeat him and you will receive the Ring of Gaxx,
  which is a very powerful item.

  The 5th level wizard spell called "Spell Immunity" (level 5) may help
  against Kangaxx - use it for "protection against necromancy and
  abjuration". Protection against abjuration protects against imprisonment.
  Then, cast "Melf's Minute Meteors" (level 3), which will hurt Kangaxx,
  as well as cast "Improved Haste". You can also buy the level +4 staff
  in the adventures mart. The sword Daystar works very well against the
  demilich too. Potion of firebreath may help as well. Protection from
  Undead scroll is also useful. 

Jaheira is summoned to the Harper Hold (The Harper's quest):

  https://baldursgate.fandom.com/wiki/Summoned_to_the_Harper_Hold

The Harpers Hold is in the Docks area. Go there when Jaheira left the
party, fight the mercs on the bottom floor, then go up to reunite
with Jaheira.

--------------------------------------------------------------------------------
Renal Bloodscalp's quest:

  https://baldursgate.fandom.com/wiki/Find_Proof_of_Mae%27Var%27s_Treachery
  https://baldursgate.fandom.com/wiki/Renal_Bloodscalp

First talk to Renal. He will give you a letter of transfer and ask
you to spy on Mae'Var in his guild to the east of the docks.

If your reputation is 10 or higher, you will be given the task to
steal from the Temple of Talos. If your reputation is 9 or lower,
you will have to steal from the Temple of Lathander. Make sure
it is nightfall before you do either of the two tasks. 

If your reputation is 10 or higher, you will be given the task to
steal from the "Temple of Talos".

- Thus, enter the Temple of Talos in the Athkatla Temple. Pick
  the lock of the chest in Weathermistress Ada's chamber and take
  the Necklace of Talos from the chest. Give the necklace to Mae'Var
  in his Guildhall (in the Dock area) and he will tell you to
  report to Edwin, his second man in command.

The second task:

- Go to the third floor of the guildhall and speak to Edwin,
  a former companion in Baldur's Gate. He will require that you
  kill a Cowled Wizard named "Rayic Gethras" for him, who lives
  in the "docks" district. Enter "Rayic Gethras"' house to
  the west and defeat the wizard on the third floor. Return
  to Edwin to report your success.

The third task:

- Edwin will next ask you to retrieve some documents from
  a merchant named Marcus. Enter the "Sea Bounty Tavern"
  which is just west of the guildhall. You have many ways
  to deal with Marcus: 

  - If the party member that speak's to him has a charisma
    greater than 10, you can purchase them from him for
    250 gold. Potions or spells can be used to temporarily
    raise attributes before speaking with him.
    Then, give the documents to Edwin and he will tell
    you to report to Mae'Var for your final assign.

The fourth and final task:

- Return to the cellars of Mae'Var's Guildhall and speak with
  Mae'Var. He will require that you kill a traitor named
  Embarl. Enter the second floor of the Sea Bounty and
  speak to Embarl. He overheard Mae'Var say that he wants
  to kill Renal Bloodscalp but he has no proof. Ask him
  to give you his dagger and let him leave. Give the
  dagger to Mae'Var as proof that you killed Embarl. 

- Speak to Edwin once more and he will reveal that he wishes
  to betray Mae'Var. He will give you Mae'Var's Strongbox
  Key and he will offer to join your party. Go down a floor
  and use the key to open the strongbox in the north chamber.
  Take Mae'Var's Letter from the box. It is recommended to
  shop from Gorch at this point as this will be the last
  opportunity to do so, e. g. buy a nymph cloak.
--------------------------------------------------------------------------------
Cernd's Child Quest in Trademeet:

This quest is only available when you have cernd in your party.

Go to Waukeen's Promenade and enter Cernd's former home, which is
on the western side of the promenade. A beggar named Catis will
tell Cernd that Fennecia, his former servant, might know where
his wife is.

Speak to Fennecia in her home marked on your map, which is also
in the promenade. She will tell Cernd to get out of her house.

After moving Cernd out of the house, talk to Fennecia again. She
will tell you that Cernd's wife stayed with a noble named Deril
and that she died under suspicious circumstances. She will also
tell you that Cernd's child is in Deril's home.

Enter the Deril Estate in the Athkatla Government. After Cernd
threatens the servent Glut, Deril will appear. If you advise
Cernd to threaten Deril into giving him the child, Deril will
give Cernd the child and disappear. You may also choose to
fight Deril instead. Lagole Gon, Deril's lich friend, will
not join in the fight at all unless attacked, so you may
choose to involve him in the fight for extra XP. 

Cernd will leave your party immediately after the peaceful
dialogue option or after a fight with Deril alone. If you
choose to attack Lagole Gon as well, you will instead have
a window after the battle to de-equip Cernd and manually
pick up the baby before Cernd leaves. Cernd will take the
child to the Druid Grove on his own and he will ask to
meet him there. He will offer his services to the party once
again if you travel to meet him at the Grove, and you will
receive experience as a reward. 

See https://baldursgate.fandom.com/wiki/Cernd%27s_Child.
--------------------------------------------------------------------------------
Rasaad's Quest in Baldur's Gate 2: The Enemies of My Friend 

  https://baldursgate.fandom.com/wiki/Rasaad_yn_Bashir#Quests_2
  https://baldursgate.fandom.com/wiki/Rasaad%27s_Journey
  https://baldursgate.fandom.com/wiki/Rasaad%27s_Journey#Heretic_Temple
  https://baldursgate.fandom.com/wiki/Rasaad%27s_Journey#Throne_of_Bhaal

After recruiting Rasaad in Trademeet, take him to the City Gates
of Athkatla.

If you don't want Rasaad to stay, use the option BLA.

To finish his last quest in ToB, put the wheel that you find on
the dragons corpse into the hotbar and move that character near
the entrace where the previous portal has been. Then use it.
Cromwell:

Cromwell is a lawful neutral dwarf fighter who can forge many
powerful items for the party for sums of gold. He is found
in the Athkatla Docks, where he has a workshop near Mae'Var's
Guildhall. He can forge ankheg plate mail more than once.

--------------------------------------------------------------------------------
Seek Out and Investigate the Fallen Paladins:

  https://baldursgate.fandom.com/wiki/Seek_Out_and_Investigate_the_Fallen_Paladins 

(Do this quest before recruiting Dorn, if you want to recruit him.)

- Sir Ryan Trawl in the High Hall of the Radiant Heart in the Temple
  District will ask you to investigate a group and gain their trust.
  You must kill their leader and his followers. The fallen paladins
  are under command of Anarg.
- In the east corner of the Athkatla Bridge behind Balthis Estate, you
  will see a group of the fallen paladins, led by Reynald de Chatillon,
  fighting a group of thieves.
- Aid the fallen paladins, Reynald will thank you and ask you to
  retrieve Anarg's Cup from the High Hall of the Radiant Heart
  in order to gain their trust.
- Return to the High Hall of the Radiant Heart in the Temple District
  and convince Sir Ryan Trawl that you need Anarg's Cup to gain
  Anarg's trust. He will give you the cup reluctantly asking that
  you return it when you have dealt with the fallen paladins.
- Return to Reynold with the cup and he will summon Anarg, who
  already knows that you are working for the Radiant Heart:
    - If you accept Anarg's offer to join the fallen paladins,
      the result will be the same as above and you will receive 7250 XP
    - If you decline Anarg's offer, Anarg's aggressive response that
      follows will cause Reynold to decry the leader's actions and
      leave.
- Speak with Sir Ryan Trawl in the High Hall once more to return
  the cup and report your success. He will give you the Gloves
  of Healing and 17,500 XP each as a reward and +1 point of
  reputation.





--------------------------------------------------------------------------------
The Watcher's keep (Watcher's keep tag, watcher tag):

  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Entrance
  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Altar_Level
  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Machine_of_Lum_the_Mad
  https://sorcerers.net/Games/BG2/Walkthrough2/watchers-keep/2-elemental-level.php
  https://sorcerers.net/Games/BG2/Walkthrough2/watchers-keep/3-maze-level.php
  https://mikesrpgcenter.com/bgate2/maps/ar3003.html
  https://sorcerers.net/Games/BG2/Walkthrough2/watchers-keep/4-machine.php
  https://baldursgate.fandom.com/wiki/Demogorgon

Click on the sarcophagus a few times in order to take a note of
a verse from the holy book written down.

Take the "candle" from the chest in the kitchen and the (2) "bell"
from the shelf in the room next to the kitchen.

Place both the:
   (1) "candle" and the
   (2) "bell"
on the altar in front of the big statue, then the nearest set of
statues will attack your party (unless already destroyed). When all
three items were placed (the book is a violet, roundish icon and
the bell can be found on a shelf in the room next to the kitchen),
you have to do the correct ritual at the alter. The ritual proceeds
via the following five questions (3-3-2-1-3):

  (1) Ring Bell
  (2) Ring Bell
  (3) Light Candle
  (4) Open Book
  (5) Ring Bell

After finishing the ritual you will have to fight the rest of
the statues.

The Elemental level is the second level of the Watcher's keep.

  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Elemental_Level

In the Air Chamber you must turn the wheel to start the giant
fan. Several Air Elementals will appear to attack your party.
Defeat the Guardian of Air and you will receive the Air
Scepter. With the Air Scepter you can open the two doors off
of the Air Library.

The Giant Snake will drop the Slime Scepter. The Ice Golem will
yield the Ice Scepter. The Chromatic Demon will have the Portal
Key, the Circlet of Netheril as well as Ixil's Spike.

The Maze Level is the third level (maze tag):

  http://mikesrpgcenter.com/bgate2/maps/ar3003.html
  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Compass_Level
  https://baldursgate.fandom.com/wiki/Watcher%27s_Keep_Imprisoned_One

The starting room for the Maze is 11, which leads to 3 (northwest).

Speak to Yakman by his camp and he will tell you about the level.
It is a maze of portals filled with demons. He will also tell you
how to fix the broken portal that leads to the next level. You
can cure him of his madness with a "level 6 Hea"l spell for 5000
xp for each party member.

The demon "Karashur" is in room 13, which can be reached from either 6 or
10. From room 6, go southwest to reach room 8. From 13 we can only go 6
or 10. So 8→6→9→5→10→13. To go to 15 from 13, go: 13→10→5→7→14→15. 14→15
is the exit area, so we have to reach 14.

The demon "Tahazzar" is in room 12, which can be reached from
3→8 (9→4→6→4→8→12); from 7→5→3→8 is also possible. From 12 we
can reach 8.

The correct rooms are:

  3→9→5→7→14→15; from 8→6→9 or 12→8→3→9→5→7→14→15, 10→13;
  from 6→13; from 11→3 from 07→05 is possible (southeast).
  From 13 you can go to 6, which eventually can be used to
  reach 14.

The Scepter of Radiance requires 3 gems to become whole again.
These three gems can be obtained from Tahazzar, Ka'rashur and
Aesgareth - the latter who is in room 14. Playing against him
follows this draw-a-card pattern:

    Construct > Strife > Triumph > Plague 

Losing Vitality means a permenant loss of 13 hit points. Loss
of experience is listed as level drain, but is actually 20k xp.

  https://baldursgate.fandom.com/wiki/Scepter_of_Radiance

There are magic golems lateron which are hard to destroy. Use
non-magical weapons against them, in order to destroy them. In
some areas you can also look for normal weapons that are 
hidden nearby.

The Illithid Encampment in the Watcher's Keep:

  https://www.mikesrpgcenter.com/bgate2/maps/ar3021.html

The Githyanki Encampment:

  https://sorcerers.net/Games/BG2/Walkthrough2/watchers-keep/4a-githyanki-area.php

In the Githyanki Encampment you can find Saladrex' Lair.

The Red Oil can be found in a pool there.

The Purple Oil can be found in the room with the Dragon's Head,
in the Githyanki Encampment

In the room with the six torches - light the torches in the
following way:

  upper row: blue-purple-red
  lower row: red-red-purple

Strike the machine of Carston six times with the glass hammer.

To operate the machine of Lum the Mad, do:

  - Short, Medium, Square:    User gets +1 to Strength.                    # 7, 8, 2
  - Long, Red, Circle:        User gets +1 to Constitution.                # 9, 4, 1
  - Blue, Square, Short:      User gets +1 to Dexterity.                   # 5, 2, 7
  - Long, Circle, Blue:       User gets +1 to Intelligence.                # 9, 1, 5
  - Circle, Square, Triangle: User gets +1 to Wisdom.                      # 1, 2, 3
  - Short, Red, Green:        User gets +1 to Charisma                     # 7, 4, 6
  - Long, Blue, Green:        User gets permanent +5% to Magic Resistance. # 9, 5, 6
  - Medium, Green, Triangle:  Party gets the Storm Star +3 mace.           # 8, 6, 3
  - Triangle, Red, Medium:    This opens the portal.                       # 3, 4, 8

Imp Riddle ("How many children do my parents have?":

  First answer is: 7.
  Coins to take:   2, 3, 1

The Final Seal:

  https://sorcerers.net/Games/BG2/Walkthrough2/watchers-keep/5-final-seal.php

To walk through via spirit warrior ("The Eternal Warrior"), do:

  Shortform solution to this riddle:

    2-2-2-3-3
    1-1-3-3-2
    4-3-1-3-4
    2-3-3-1-3
    2-4-2-1-2

  Go East.                                    # 2
  Attack the Goblin.                          # 2
  Go East.                                    # 2
  Examine the Treasure Chest.                 # 3
  Attack the Skeleton.                        # 3
  Open the chest.                             # 1
  Exit to the North.                          # 1
  Attack the War Dog.                         # 3
  Search the room.                            # 3
  Exit to the west.                           # 2
  Search the room.                            # 4
  Go West.                                    # 3
  Go North.                                   # 1
  Attack the Ghost.                           # 3
  Open the chest.                             # 4
  Go East.                                    # 2
  Go East.                                    # 3
  Open the desk drawer.                       # 3 
  Go North.                                   # 1
  Use the scroll with the gibberling picture. # 3
  Go West.                                    # 2
  Examine the chest.                          # 4
  Go through the ominous archway.             # 2
  Pass through the Arch and enter the crypt.  # 1
  Use the Wand of Missiles, then kill the mummy. # 2

Against Demogorgon it is recommended to avoid Time Stop, as he can simply
attack while time is stopped.

As Demogorgon summons two mariliths, you can bait the mariliths into
chasing upstairs, then fight against summoned units there such as
two magical swords.

Then you can fight Demogorgon without supporting units on his side.
