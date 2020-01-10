
def talk_to_people(player):
    """Dictionary to pull random facts about the trail when the traveler reaches marked mile-posts along the way."""
    talking_dictionary = {
        # ' You\'re about to begin a great adventure, traveling the Oregon Trail.\n
    102: ' Hiya Traveler!! You\'ve reached the Kansas River crossing. This crossing \n is near, what will be known as Topeka, Kansas. Travelers cross the Kansas\n River to start their trek across Kansas and points out west. Be careful, \n the water can be deep in parts, and good luck on your journey',  
    185: ' Welcome to The Big Blue River Crossing! Did you know that this is the \n home of Alcove Spring and Waterfall, a popular area for pioneer wagons \n to ford the Big Blue River? This location is also the site of the first \n recorded death in the Donner Party - 70 year old Sarah H. Keyes, who died \n from consumption, I hope your travels have better results. ',
    304: " Howdy Traveler! Welcome to Fort Kearney,  a US Army post, located here \n on the south bank of the Platte River. We are the best supply outpost \n around these parts. Actually we're the only outpost around these part \n for the next 300 miles, so stock up if you need to, you have a long journey \n ahead of you.", 
    554: ' Hi there stranger! This is Chimney Rock, an important landmark on the \n Oregon Trail. It\'s a spectacular natural formation of solid rock and can \n be seen from miles around.  It also signals the end of the prairies as the \n trail is becoming more steep and rugged heading west towards the Rocky Mountains.\n Not much to do around here, but you won\'t ever forget this place.', 
    640: ' You\'ve reached Fort Laramie, a US Army post near the junction of the \n North Platte and Laramie Rivers.  It was founded as a fur-trading post in \n 1834, and named after a French trapper named Jacques Laramie, who is famous\n around these parts. Fort Laramie is an important stop for resting and getting\n supplies, so you should probably replace anything you\'ve lost before you head\n into the mountains.', 
    830: ' Well hello there! Independence Rock is an important landmark and resting\n place along the Oregon Trail. It\'s a large natural formation, almost 200 \n feet tall. It\'s made of soft stone -  many travelers carve their names or \n initials into it. ** Fun Fact ** It gets its name from the fact that, in order\n to stay on schedule, travelers try to reach it no later than July 4--Independence\n Day, hope you made it here in time, otherwise you could be in a world of hurt.',
    932: ' Hi ya! Are you cutting through the South Pass? Well, that\'s a good thing\n since this is the only place along the Continental Divide that wagon trains \n can safely cross. It is the lowest point  between the Central and Southern \n Rocky Mountains, so get on your way - there\'s adventure waiting for you on the \n other side',
    989: ' Wow! You\'ve made it to Fort Bridger, and about halfway to your destination.\n A mountain man named Jim Bridger began this fort as a trading post in 1842, \n now it\'s one of the most important outfitting points along the Oregon Trail. \n Stock up on your supplies while you\'re here, from what I hear conditions \n can get pretty treacherous going forward, and you\'ll want to be prepared.',
    1151:' Welcome to the Green River Crossing! The Green River is a tributary to the \n Colorado River, flowing south from the Continental Divide along a twisted, rugged \n path, estimated to be more than 700 miles in length.  It\'s extremely dangerous to \n cross, but you must cross it if you want to contiue going west.  Good luck with \n that, you\'re going to need it.', 
    1259:' Aaaaah! Soda Springs is natual bubbling pools of carbonated water, caused by\n ancient volcanic activity. Local Indians, fur traders and trappers visit the \n pools of water for medicinal and bathing.  But don\'t drink too much of the water\n - it could make you sick.', 
    1359:' Fort Hall is an outpost on the banks of the Snake River.  Some people abandon\n their wagons here, and continue the rest of their way on foot, with their animals.\n But that\'s silly, Dr. Marcus Whitman showed us all that you can lead a wagon train\n westward from here, so you should do that. This is a great place to buy supplies \n and rest up.',
    1543:' Welome to the Snake River Crossing. The Snake River gets its name from the way\n it twists and turns through this rugged country, sometimes through steep gorges. \n You\'ve safely made it here, but crossing the Snake River can be very dangerous. \n Be careful my new friend.', 
    1648:' Fort Boise was built by the Hudson\'s Bay Company in 1834 as a fur-trading \n outpost. Now that the fur trade is dwindling, Fort Boise is becoming \n important supply post for travellers.',
    1808:' Grande Ronde in the Blue Mountains, The Grand Ronde (French for \'great ring\')\n is a river that runs parallel to the Blue Mountains. The Grande Ronde valley a \n beautiful place to stop and rest, and enjoy the fact that your journey \n is almost over.', 
    1863:' Fort Walla Walla was established in 1818 as a fur-trading post where the Columbia\n and Walla Walla Rivers meet. This is the last fort you\'ll come to in the game. \n You\'re almost at the end, don\'t screw it up now!',
    2040:' Whoo Hoo!  You\'ve survived to the end of the trail!!!  Oregon City has always \n been a natural place of commerce between Indians and whites, the town also uses \n the nearby river as a dependable source of power for mills for its economic \n development. This area is growing rapidly as an economic center of the territory. \n Go on an make your claim on some land, there\'s a lot of it out \n there to choose from.'

}      
    return talking_dictionary





