# AUTOMYSTICA.docx
AUTOMYSTICA
Build. Adapt. Survive.
Event Overview
AUTOMYSTICA is an IoT and Automation Challenge where participants are given a real-world scenario and must engineer a working automated solution using Wokwi simulation, embedded programming and a web dashboard.
Unlike a conventional project competition, participants will not be asked to come up with their own problem or project. Instead, they will be given a specific situation and a set of requirements that their system must satisfy.
The real challenge begins when, after the participants have developed their initial solution, a new limitation or unexpected condition is introduced.
Teams must then understand the new situation, modify their solution and make the system work under the changed conditions.
The event therefore tests not only whether participants can build a working IoT system, but also whether they can think, troubleshoot and adapt when the conditions change.
The complete challenge can be summarized as:
Understand → Build → Automate → Visualize → Adapt → Demonstrate
The event is designed around the idea that in real-world automation, making a system work once is not enough — an engineer must be able to make it work when conditions change.
The existing concept also follows the complete IoT pipeline of sensing, decision-making, actuation, communication and visualization. 
1. EVENT DETAILS
Detail
Information
Event Name
AUTOMYSTICA
Theme
IoT + Automation Challenge
XTASY Edition
XTASY 4.0
Event Date
10 September 2026
Coordinator
Khushi Barde — 8767356261
Co-Coordinator
Anushka Dorlikar — 7559443674
Team Format
Duo
Registration Fee
₹90 per team
Primary Platform
Wokwi
Final Output
Working IoT automation system + web dashboard
2. WHAT IS AUTOMYSTICA?
Imagine that you are an automation engineer.
You are given a situation such as:
A greenhouse is experiencing excessive temperature while soil moisture is simultaneously decreasing. An automated system is required to monitor the environment and control the necessary equipment.
You are then told exactly what the system is expected to do.
You build it.
You program it.
You test it.
You connect it to a dashboard.
You think you're done.
Then comes the twist.
The coordinators introduce a new limitation:
"The system can no longer operate both actuators simultaneously."
Now your original solution may no longer be sufficient.
You have to rethink your automation logic, modify your code/system and make it work under the new condition.
That is AUTOMYSTICA.
3. WHAT WILL BE GIVEN TO PARTICIPANTS?
Every team will receive a scenario-based challenge.
The challenge will contain only the information necessary for them to understand and solve the problem.
Each scenario will have four main components:
1. Scenario
A short real-world situation explaining what is happening and what needs to be solved.
2. Required Outputs
What the system must produce or control.
For example:
Fan ON/OFF 
Pump ON/OFF 
Alarm 
LED indication 
Motor control 
3. Automation Conditions
The exact conditions under which the system should perform an action.
For example:
If temperature exceeds the given threshold → Fan ON.
If temperature returns below the safe threshold → Fan OFF.
If soil moisture falls below the given level → Pump ON.
Participants must translate these requirements into their automation logic.
4. Dashboard Requirements
The information that must be displayed on the web dashboard.
For example:
Current temperature 
Soil moisture 
Fan status 
Pump status 
System status 
Alert indication 
Relevant graph/trend 
The existing Automystica draft similarly specifies scenario, inputs, outputs, automation conditions and dashboard requirements as the structure of a problem statement. 
4. THE CORE EVENT FLOW
The event will consist of one continuous engineering challenge, divided into stages for execution.
STAGE 1 — UNDERSTAND THE SCENARIO
Teams receive their assigned scenario.
They first need to understand:
What is the problem? 
What should the system do? 
What are the required outputs? 
Under what conditions should the outputs operate? 
What information must be shown on the dashboard? 
This stage tests problem understanding and planning.
Teams should not immediately start coding.
They need to first understand what they are actually being asked to build.
5. STAGE 2 — BUILD THE AUTOMATION
Teams then create their solution using Wokwi.
They will select and connect the required components and develop the control logic.
The general architecture will be:
Sensors → ESP32 → Automation Logic → Actuators
For example:
Temperature Sensor
↓
ESP32
↓
Temperature Condition
↓
Fan
The participants will have to:
Select appropriate components from the allowed components 
Create the circuit in Wokwi 
Write the required program 
Implement the automation conditions 
Simulate different sensor conditions 
Verify that the required outputs respond correctly 
The existing event concept already specifies ESP32/Arduino, sensors, actuators and Wokwi-based circuit/program development as the practical component. 
6. STAGE 3 — THE DASHBOARD
Once the automation system is working, participants will integrate their system with a web dashboard.
The dashboard should represent the actual data generated by their simulated system.
It should not simply contain manually entered or static values.
The current draft specifically establishes that dashboard values should represent actual simulated/communicated data. 
Depending on the assigned scenario, the dashboard may display:
SENSOR DATA
Temperature 
Humidity 
Soil moisture 
Water level 
Light intensity 
Occupancy 
etc. 
SYSTEM STATUS
Normal 
Warning 
Critical 
ACTUATOR STATUS
Fan: ON/OFF 
Pump: ON/OFF 
Light: ON/OFF 
Alarm: ON/OFF 
ALERTS
For example:
⚠ HIGH TEMPERATURE
⚠ LOW WATER LEVEL
⚠ CRITICAL CONDITION
GRAPHS
Where useful, teams may display sensor trends through charts/graphs.
The purpose is to demonstrate the complete connection:
Sense → Decide → Act → Communicate → Visualize
7. 🔴 THE TWIST — THE SIGNATURE OF AUTOMYSTICA
This is the most important part of the event.
Once teams have successfully developed their initial solution, the coordinators will introduce a new limitation or unexpected condition.
This will be the AUTOMYSTICA TWIST.
The limitation will change the situation that the participants were originally solving.
Examples of possible limitations
These are examples for understanding the event concept only. These are not the final limitations.
Example 1 — Power Limitation
Original requirement:
Fan and pump can operate normally.
New limitation:
The system cannot operate both actuators simultaneously.
The team must modify its automation logic to decide which action should receive priority.
Example 2 — Sensor Limitation
Original requirement:
System uses the temperature sensor to control cooling.
New limitation:
The primary temperature sensor is unavailable/unreliable.
The team must modify the system to handle the changed condition.
Example 3 — Emergency Condition
Original system:
Temperature and humidity are controlled independently.
New situation:
Both parameters have crossed their critical thresholds simultaneously.
The team must decide how the system should respond.
Example 4 — Resource Limitation
Original requirement:
Pump can operate whenever soil moisture is below the required threshold.
New limitation:
The pump can operate only for a limited duration at a time.
The team must modify the control logic accordingly.
The exact limitations will be designed later by the coordinators.
The important principle is that the limitation should not simply ask participants to add another feature.
It should force them to rethink or adapt their existing solution.
8. STAGE 4 — ADAPTATION
After the limitation is announced, teams will get a limited amount of time to respond.
They must:
Understand the new condition. 
Identify what part of their solution is affected. 
Modify their circuit/code/logic if required. 
Test the modified system. 
Demonstrate that the system now works under the new condition. 
This is the part that differentiates Automystica from a normal Wokwi competition.
The question changes from:
"Can you build it?"
to:
"Can you adapt it?"
9. FINAL DEMONSTRATION
After the adaptation stage, each team will demonstrate its final solution to the judges.
The demonstration should show:
1. The original scenario
What problem were they solving?
2. The original solution
How did they approach the problem?
3. Working automation
Show the Wokwi circuit and demonstrate the required behaviour.
4. The limitation
What new condition was introduced?
5. Their adaptation
What did they change and why?
6. Final working system
Demonstrate that the modified system successfully handles the limitation.
7. Dashboard
Show the relevant sensor values, actuator states, system status and alerts.
8. Technical explanation
Judges can question the team about their design and decision-making.
10. WHAT WILL THE JUDGES ACTUALLY LOOK FOR?
The judging should focus on engineering ability, rather than simply whether a team managed to complete a circuit.
A possible evaluation structure is:
Criteria
Marks
Understanding of the scenario
10
Circuit & component selection
15
Automation logic & programming
20
Correctness of simulation
15
Adaptation to the limitation
15
Dashboard & data integration
15
Technical explanation & innovation
10
TOTAL
100
The current draft already uses a 100-mark technical evaluation covering problem understanding, Wokwi implementation, code/automation, simulation, dashboard, data integration and technical explanation. 
The important addition is Adaptation to Limitation.
That should become one of Automystica's defining judging parameters.
11. WHAT PARTICIPANTS ARE EXPECTED TO KNOW
Participants should have basic knowledge of:
IoT fundamentals 
ESP32/Arduino 
Sensors 
Actuators 
Basic programming 
Conditional logic 
Automation 
Wokwi 
Basic web/dashboard development 
Basic data communication 
They don't necessarily need advanced knowledge of every technology.
The challenge is intended to test their ability to apply technical knowledge to a given situation.
12. WHAT MAKES AUTOMYSTICA DIFFERENT?
Automystica is not:
❌ An idea pitching competition
❌ A normal project exhibition
❌ A simple circuit-building competition
❌ A dashboard-design competition
❌ A quiz
Instead, it is a time-bound engineering challenge.
Participants are given:
A situation
Then:
A technical requirement
Then:
A working challenge
Then:
A sudden limitation
And finally:
A test of whether their system can survive the change.
13. DIFFERENCE BETWEEN YOUR THREE MAIN TECHNICAL EVENTS
This should also be communicated internally so nobody accidentally markets the events as the same thing.
🔧 HACK THE HARDWARE
Given hardware → Build → Program → Physical arena → Compete
Can you build and control it?
💡 TRIGUNA
Agricultural challenge/domain → Develop an innovative solution → Pitch
Can you identify and propose something worth building?
TRIGUNA is explicitly focused on real-world agricultural problems, technical feasibility and economic impact. 
⚙️ AUTOMYSTICA
Given scenario → Engineer solution → Automate → Dashboard → Limitation → Adapt
Can you engineer a system that survives changing conditions?
This distinction is extremely important for XTASY 4.0.
14. WHAT MAKES IT "SQUID GAME"?
The Squid Game theme should not just be visual decoration.
It should be incorporated into the gameplay.
The central idea is:
You think you've cleared the challenge. Then the rules change.
For Automystica, the equivalent is:
🟢 GREEN LIGHT
Build your system.
🔴 RED LIGHT
A new condition has been introduced.
🦑 THE TWIST
A limitation is revealed.
🟢 GREEN LIGHT
Adapt your system.
🏆 FINAL
Prove that your system survives.
This gives the event an actual connection to the XTASY 4.0 theme without making the technical challenge gimmicky.
15. WHAT WE NEED TO PREPARE AS ORGANIZERS
Before the event, the Automystica team needs to finalize:
Problem Scenarios
A set of different real-world scenarios.
Required Outputs
What each system must control.
Automation Conditions
Exact conditions that the participants need to implement.
Dashboard Requirements
What information must appear on the dashboard.
Allowed Components
Which ESP32/Arduino boards, sensors and actuators participants can use.
Limitations
A set of carefully designed Twist/Crisis conditions.
Time Limits
Time for initial build, limitation and adaptation.
Judging Rubric
Final scoring sheet for judges.
Technical Setup
Internet connectivity 
Wokwi access 
Dashboard development environment 
Master display/projector 
Final demonstration system 
Submission mechanism 
16. IMPORTANT DESIGN PRINCIPLE FOR THE PROBLEM STATEMENTS
Every problem statement should be simple enough to understand quickly but complex enough to require engineering thinking.
The structure should always remain:
SCENARIO
What is happening?
REQUIRED OUTPUTS
What should the system control?
AUTOMATION CONDITIONS
When should it act?
DASHBOARD REQUIREMENTS
What should the user see?
LIMITATION
What changes later?
That's it.
We do not need to overload the participants with a huge technical specification.
The challenge should be:
Understand the situation → decide how to solve it → build → adapt.
17. SHORT DESCRIPTION FOR WEBSITE / REGISTRATION
AUTOMYSTICA — Build. Adapt. Survive.
Automystica is a time-bound IoT and Automation Challenge where teams are given real-world scenarios and must develop a working automated solution using simulation, embedded programming and a web dashboard. But the challenge doesn't end when the system works — an unexpected limitation is introduced, forcing teams to adapt their automation logic and overcome the new condition. The team that demonstrates the most effective, reliable and well-engineered solution emerges victorious.
Date: 10 September 2026Team: DuoRegistration Fee: ₹90 per team
18. ONE-LINE POSTER VERSION
Build the system. Face the twist. Adapt or fail.
Or, if you want the strongest Squid Game feel:
BUILD. ADAPT. SURVIVE.
I would personally use BUILD. ADAPT. SURVIVE. as the main Automystica tagline.
Final understanding of the event
If I had to explain Automystica to a new volunteer in 20 seconds, I'd say:
"We give every duo a real-world scenario. They get the required outputs, automation conditions and dashboard requirements, and they have to build the complete IoT automation system in Wokwi and connect it to a dashboard. Once they have a working solution, we introduce a new limitation — like a power, sensor or resource restriction. They then have limited time to modify their system and overcome it. Finally, they demonstrate the original solution, the twist and their adapted solution to the judges."
That is the Automystica we should now build everything around.

# HACK THE HARDWARE.docx
HACK THE HARDWARE
Build It. Control It. Conquer the Arena.
Event Overview
HACK THE HARDWARE is a hands-on hardware and robotics challenge organized by the Department of Industrial Internet of Things as part of XTASY 4.0.
This is the second edition of Hack the Hardware.
The event is designed to take participants from learning the fundamentals of a Bluetooth-controlled bot to actually building, programming and operating one in a competitive arena.
The event begins with a two-day preparatory workshop for second-year IIoT students, where participants learn the fundamentals required to build and control the bot.
On the main event day, participants put that knowledge to the test.
Teams are provided with the required bot kits and must first assemble and program their bot. Once their bot is ready, teams enter the final arena challenge, where they must navigate the bot through a maze while maintaining control and avoiding collisions with the arena walls.
The final winner is determined based on the team's performance across the defined evaluation parameters.
The overall journey is:
LEARN → BUILD → PROGRAM → CONTROL → COMPETE
1. EVENT DETAILS
Detail
Information
Event Name
HACK THE HARDWARE
Edition
2nd Edition
XTASY Edition
XTASY 4.0
Event Date
10 September 2026
Coordinator
Arpit Kharwade — 9156867498
Co-Coordinator
Shantanu Bhure— 9673707772
Registration Fee
Solo – Rs. 70 ; Duo – Rs. 100
Event Type
Hardware + Robotics Challenge
Core Technology
Bluetooth-controlled bot
Final Challenge
Bot navigation through a physical arena/maze
Equipment
Bot kits provided by organizers
Note: The team size and registration fee for Hack the Hardware have not been specified yet, so these should be added once finalized rather than assumed.
2. WHAT IS HACK THE HARDWARE?
Imagine being given a set of hardware components and being told:
"You know how this bot works. Now build it yourself."
You assemble the components.
You program the controller.
You test the movement.
You troubleshoot the bot.
And then comes the real challenge:
Take your bot into the arena.
The bot must navigate the maze while being controlled through Bluetooth.
The team has to maintain:
Control 
Accuracy 
Coordination 
Speed 
Awareness of the arena 
Proper bot movement 
And every unnecessary collision with the walls can affect the team's performance.
So this is not simply a "make a bot" activity.
It is a combination of:
Hardware Assembly + Programming + Control + Precision + Competition
3. PRE-EVENT WORKSHOP
Before the final competition, a two-day workshop will be conducted for second-year IIoT students.
The purpose of this workshop is to give the participants the technical foundation required for the final challenge.
During the workshop, participants will learn how to:
Understand the bot components 
Assemble the bot 
Connect the required hardware 
Understand the control mechanism 
Program the bot 
Establish Bluetooth-based control 
Test basic movement 
Troubleshoot common hardware/programming issues 
The workshop is intended to ensure that participants understand the technology before they face the competition.
Important distinction
The workshop is a learning phase, while the event day is the competition phase.
The workshop teaches participants:
"How does the bot work?"
The competition asks:
"Can you make it work under pressure?"
4. WHO WILL ATTEND THE WORKSHOP?
The preparatory workshop is intended specifically for second-year IIoT students, as this is the academic cohort for which the workshop is being conducted.
The final Hack the Hardware competition, however, will be open to participants as decided by the overall XTASY participation rules and registration structure.
This distinction should be kept clear in all communication so that nobody assumes the workshop and the final competition have identical eligibility.
5. WHAT WILL BE PROVIDED?
The required bot kit for the competition will be provided by the organizers.
Participants will therefore not be expected to independently arrange the complete bot hardware.
The kit will contain the components required to assemble the bot according to the competition design.
The exact component list should be finalized by the technical team and communicated to participants if necessary.
The basic concept is:
Provided Kit
↓
Assembly
↓
Programming
↓
Testing
↓
Arena Challenge
6. MAIN EVENT DAY — THE COMPETITION
The competition will consist of two major phases.
PHASE 1 — BUILD & PROGRAM
Teams receive their bot kit.
They must assemble the bot and program it according to the instructions and requirements provided by the organizers.
Participants will need to:
Identify the components. 
Assemble the bot correctly. 
Make the required connections. 
Upload/program the required code. 
Establish Bluetooth control. 
Test the bot's movement. 
Ensure that the bot responds correctly to the controller. 
The goal is to produce a functional, controllable bot before entering the arena.
7. PHASE 2 — THE FINAL ARENA
Once the bot is assembled and programmed, the competition moves to the most exciting part:
THE ARENA
A physical maze/arena will be prepared by the organizers.
Teams will place their bots at the designated starting point and attempt to navigate the bot through the arena.
The challenge is to reach the designated endpoint while maintaining control and avoiding unnecessary contact with the arena walls.
The arena becomes the actual test of everything the participants learned during the workshop and build phase.
8. WHAT WILL THE PARTICIPANTS HAVE TO DO IN THE ARENA?
The basic objective is:
Navigate the bot from the starting point to the finish point through the maze.
Participants will control the bot using the designated Bluetooth control mechanism.
They will need to demonstrate:
CONTROL
Can the team accurately control the bot?
PRECISION
Can they navigate narrow sections without hitting the walls?
SPEED
Can they complete the challenge efficiently?
CONSISTENCY
Can they maintain proper control throughout the entire arena?
DECISION-MAKING
Can they choose the appropriate path and respond to the arena conditions?
9. WALL COLLISIONS MATTER
The arena is not simply a race track.
Contact with the maze walls will be considered during evaluation.
This is important because otherwise participants may simply try to drive the bot as quickly as possible.
Instead, the challenge becomes a balance between:
SPEED + CONTROL + PRECISION
A team that is extremely fast but repeatedly crashes into the walls should not automatically have an advantage over a team that navigates the arena smoothly and accurately.
The exact scoring weight for collisions, time and other parameters should be finalized by the technical/organizing team before the event.
10. HOW WILL THE WINNER BE DECIDED?
The winner will be the team achieving the highest overall score based on the finalized evaluation parameters.
The scoring can take into consideration parameters such as:
Parameter
What it evaluates
Completion
Whether the bot successfully completes the arena
Time
How efficiently the team completes the course
Wall Collisions
Accuracy and control during navigation
Bot Performance
Proper functioning of the bot
Control & Handling
Smoothness and precision of movement
Overall Performance
Combined performance in the challenge
The exact marks/weightage should be finalized before publishing the official rules.
11. THE IMPORTANT COMPETITION PRINCIPLE
The event should not become simply:
"Fastest bot wins."
The actual challenge should be:
"Who can build a reliable bot and control it most effectively?"
This gives participants a reason to care about both phases.
Build Phase
Tests:
Hardware + Programming
Arena Phase
Tests:
Control + Precision + Performance
So the winner should be the team that can successfully connect all of these skills.
12. WHAT MAKES HACK THE HARDWARE DIFFERENT?
Hack the Hardware is fundamentally a hands-on physical engineering competition.
Participants aren't just answering questions.
They aren't only pitching ideas.
They aren't simply designing a simulation.
They are actually handling hardware and making a physical machine perform a task.
This makes the event different from the other XTASY technical events.
TRIGUNA
Think of something worth building.
AUTOMYSTICA
Engineer a solution to a given problem and adapt when conditions change.
HACK THE HARDWARE
Build the machine and control it in the real world.
This distinction should be maintained in all promotional material.
13. THE SQUID GAME CONNECTION
Since XTASY 4.0 has a Squid Game theme, Hack the Hardware can use the theme naturally without changing the technical challenge.
The strongest connection is:
You have learned the rules. You have built your machine. Now survive the arena.
You could divide the competition into themed stages:
🟢 GREEN LIGHT — BUILD
Assemble and program your bot.
🔴 RED LIGHT — TEST
Test your bot and ensure that it responds correctly.
🟢 GREEN LIGHT — ARENA
Enter the maze.
🔴 RED LIGHT — COLLISION
Every mistake matters.
🏆 FINAL — CONQUER THE ARENA
Complete the challenge with the best overall performance.
This can be reflected through the arena design, countdowns, announcements, signage and visual identity without making the event feel childish.
14. THE ARENA SHOULD BE THE STAR
If the budget and space allow, I would make the arena visually impressive.
The maze should have:
Clearly defined starting point 
Clearly defined finish point 
Visible boundaries 
Challenging turns 
Narrow sections 
Different paths 
A designated control area for participants 
A clear spectator boundary 
The objective is to make it visually obvious to anyone walking past:
"Something is happening here."
This is particularly useful because Hack the Hardware can become one of the most spectator-friendly events of XTASY.
People can literally watch teams trying to navigate the bot.
15. OPTIONAL ARENA DESIGN PRINCIPLE
You could divide the arena into different sections.
For example:
ZONE 1 — CONTROL
Basic turns.
↓
ZONE 2 — PRECISION
Narrower path.
↓
ZONE 3 — DECISION
Multiple possible paths.
↓
ZONE 4 — FINAL
Difficult turns leading to the finish.
This doesn't necessarily mean adding complicated hardware or sensors.
The difficulty can come simply from arena geometry.
That keeps the event affordable and manageable.
16. WHAT PARTICIPANTS NEED TO KNOW
Participants should have basic familiarity with:
Basic electronics 
Microcontrollers 
Motor control 
Programming 
Bluetooth control 
Basic troubleshooting 
However, the preparatory workshop is intended to teach the required bot-building and control concepts to the relevant participants.
The competition should therefore focus on application and execution, rather than testing theoretical knowledge.
17. WHAT THE TECHNICAL TEAM NEEDS TO FINALIZE
Before the event, the technical team should prepare:
BOT DESIGN
Exact bot architecture 
Components 
Motor configuration 
Controller 
Bluetooth module/control mechanism 
Power supply 
Wiring 
WORKSHOP
Two-day workshop structure 
Teaching material 
Assembly instructions 
Programming instructions 
Testing procedure 
Troubleshooting guide 
COMPETITION
Assembly instructions 
Programming requirements 
Allowed modifications 
Testing rules 
Arena dimensions 
Arena layout 
Starting conditions 
Maximum attempt/time 
Collision rules 
Restart rules 
Disqualification conditions 
SCORING
Finalize:
Completion score 
Time score 
Collision penalty 
Failure/restart penalty 
Any bonus parameters 
18. IMPORTANT RULES TO DECIDE BEFORE REGISTRATION
These don't need to be finalized in this document yet, but the organizers should eventually decide:
Can participants modify the provided kit?
For example:
No hardware modifications allowed.
or
Minor modifications permitted within specified limits.
Can participants modify the code freely?
This should be clearly defined.
How many arena attempts does each team get?
For example:
One official attempt.
or:
Practice attempt + official attempt.
What happens if the bot stops working?
Define whether:
The team gets a restart. 
The timer continues. 
A technical reset is allowed. 
The attempt ends. 
What counts as a collision?
For example:
Any physical contact with the arena wall.
This needs to be unambiguous.
What happens if a team doesn't finish?
Should they receive:
Partial score based on distance completed? 
Time-based score? 
No completion points? 
These decisions should be made before the final rulebook.
19. SUGGESTED EVENT-DAY FLOW
The exact timings can be finalized later depending on the number of teams.
The general flow should be:
Registration → Briefing → Kit Distribution → Assembly & Programming → Testing → Arena Briefing → Arena Attempts → Score Compilation → Winner Announcement
The important thing is that participants clearly understand the transition:
BUILD AREA
Teams work on their bots.
↓
TEST AREA
Teams verify their bots.
↓
ARENA
Only competition attempts happen here.
This separation will help prevent chaos on the event day.
20. WHAT MAKES THE EVENT IMPRESSIVE?
There are three things that can make Hack the Hardware stand out.
1. THE BUILD
Participants physically create their bot.
2. THE ARENA
The bot has to perform under real conditions.
3. THE PRESSURE
Time, collisions and competition determine the outcome.
So the event should feel like:
"You built it. Now prove it."
rather than:
"Come and drive a remote-controlled car."
That distinction is extremely important for your branding.
21. SHORT DESCRIPTION FOR WEBSITE / REGISTRATION
HACK THE HARDWARE — Build It. Control It. Conquer the Arena.
Hack the Hardware is a hands-on robotics and hardware challenge where participants put their engineering skills to the test. After learning the fundamentals of building and controlling a Bluetooth-controlled bot through a preparatory workshop, teams must assemble and program their bot during the competition and then take it into a physical maze arena. With time, control and wall collisions influencing their performance, teams must navigate the arena with precision and efficiency. The team that demonstrates the strongest overall performance takes the win.
Date: 10 September 2026Event: Hardware & Robotics ChallengeBot Kit: Provided by organizers
22. SHORT POSTER DESCRIPTION
Build the bot. Master the controls. Conquer the maze.
A hands-on hardware challenge where your engineering meets the arena. Assemble. Program. Navigate. Compete.
23. ONE-LINE TAGLINE OPTIONS
For the media team, these could work:
Best overall:
BUILD IT. CONTROL IT. CONQUER THE ARENA.
More aggressive:
BUILD. CONTROL. SURVIVE.
More technical:
FROM CIRCUIT TO COMPETITION.
Squid Game themed:
GREEN LIGHT. BUILD. RED LIGHT. DON'T CRASH.
Short and punchy:
YOUR BOT. YOUR CONTROL. YOUR ARENA.
My pick for XTASY 4.0 would be:
BUILD IT. CONTROL IT. CONQUER THE ARENA.
It tells someone immediately what the event actually involves.

# TRIGUNA.docx
TRIGUNA
AGRICULTURE INNOVATION CHALLENGE
Event Structure & Master Operations Document
Organized By: Department of Industrial Internet of Things (IIoT)Event: TRIGUNAEdition: 2026Event Date: 10 September 2026Event Type: Innovation Challenge & Pitching CompetitionTheme: Agriculture, Sustainability & InnovationParticipants: 1st, 2nd & 3rd Year Students – All BranchesParticipation: Solo or TeamMaximum Team Size: 3 MembersRegistration Fee: ₹70 Solo | ₹100 Team
Coordinator: Kshitij Adakane – 9405476977Co-Coordinator: Sumedh Nirwan – 7263817410
1. EVENT OVERVIEW
TRIGUNA is an agriculture-focused innovation challenge designed to encourage students to identify genuine problems faced by farmers and develop practical, technically feasible and economically viable solutions.
The event focuses on the intersection of agriculture, technology, sustainability, frugal engineering and innovation. Participants are expected to move beyond theoretical ideas and develop solutions that can realistically address problems encountered in agricultural and rural environments.
The competition is structured as an innovation and pitching challenge, where participants select a relevant agricultural problem domain, develop a solution, demonstrate its feasibility and present the idea before a panel of judges.
The central philosophy of TRIGUNA is:
Identify a real problem → Understand its root cause → Develop an innovative solution → Demonstrate feasibility → Present the impact.
The event particularly encourages solutions that are affordable, practical, scalable and suitable for real-world agricultural conditions.
The competition framework emphasizes real-world relevance, technical feasibility and economic value rather than purely theoretical concepts. 
2. EVENT OBJECTIVES
The major objectives of TRIGUNA are:
To encourage students to identify authentic agricultural and rural problems. 
To promote innovation in agriculture through engineering and technology. 
To develop practical and affordable solutions for farmers. 
To encourage students to think about feasibility, cost and implementation. 
To introduce students to real-world problem-solving and product development. 
To promote sustainable and resource-efficient agricultural practices. 
To encourage interdisciplinary collaboration between students from different branches. 
To develop students' skills in technical communication, pitching and defending an idea. 
To identify promising ideas that may have potential for further mentorship, prototyping and development. 
3. CORE PHILOSOPHY
TRIGUNA is not intended to be a conventional idea-pitching competition where participants simply present theoretical concepts.
The proposed solution should be connected to a clearly identifiable agricultural problem and should demonstrate how the solution can work in practical conditions.
Solutions should consider factors such as:
Farmer affordability 
Rural infrastructure limitations 
Power availability 
Ease of operation 
Maintenance requirements 
Environmental conditions 
Scalability 
Economic benefit 
Long-term sustainability 
Purely abstract ideas, theoretical literature surveys, generic concepts or software mockups without meaningful functionality should not receive strong evaluation. 
4. TARGET PARTICIPANTS
TRIGUNA is open to:
1st Year Students 
2nd Year Students 
3rd Year Students 
Students from all academic branches 
Participants may participate:
Individually, or 
In teams of up to 3 members. 
All participants compete under a common evaluation framework.
5. EVENT FORMAT
TRIGUNA follows a Problem-to-Pitch Innovation Model.
Overall Journey
Problem Domain → Problem Identification → Research & Understanding → Solution Development → Prototype/Simulation → Feasibility Analysis → Pitch → Jury Defense
Participants are provided with a defined set of agriculture-focused challenge domains.
Each participant/team selects one challenge domain and develops an innovative solution around it.
The team then prepares a pitch explaining:
What is the problem? 
Who is affected? 
Why does the problem exist? 
What is the proposed solution? 
How does the solution work? 
Why is the solution technically feasible? 
How much does it cost? 
What benefit does it provide? 
How can it be implemented or scaled? 
6. OFFICIAL CHALLENGE THEMES / PROBLEM TRACKS
TRIGUNA consists of six major agriculture innovation tracks. Every participating team selects one track and develops its solution within that domain. 
PS-1: THE ₹3,000 SMART FIELD
Precision Irrigation & Pest Alert
This track focuses on affordable agricultural automation and crop monitoring for small and marginal farmers.
The challenge revolves around developing solutions such as:
Precision irrigation systems 
Automated irrigation controllers 
Soil/environment monitoring 
Crop pest or disease early-warning systems 
Low-cost agricultural sensor systems 
The solution should prioritize affordability and reliability, particularly under rural power limitations.
Technology pathways may include:
IIoT sensor nodes 
Microcontrollers 
IoT systems 
Tinkercad/Wokwi simulations 
Automated control systems 
Frugal engineering pathways may include:
Gravity-based systems 
Mechanical mechanisms 
Float valves 
Passive irrigation solutions 
For standard solutions under this track, the proposed Bill of Materials should remain below ₹3,000. 
PS-2: THE 6-HOUR SHIELD
Allied Dairy & Fisheries
This track focuses on technological solutions for challenges faced in dairy and fisheries.
Possible areas include:
Milk preservation 
Low-cost cooling systems 
Off-grid cooling 
Fish pond monitoring 
Dissolved oxygen monitoring 
Emergency aeration 
Water-quality monitoring 
Example technical approaches include:
Solar-powered cooling 
Peltier-based systems 
IoT monitoring 
DO/pH monitoring 
Automated aeration 
Frugal solutions may include:
Evaporative cooling 
Passive cooling 
Mechanical aeration 
Low-cost monitoring mechanisms 
The emphasis is on solutions that can operate effectively even where continuous grid electricity is unavailable. 
PS-3: SHREE ANNA: GRAIN TO GAIN
Traditional Millets
This track focuses on improving the processing, handling and value realization of traditional millets.
The challenge addresses issues such as:
Low-cost millet processing 
Dehulling 
Grain handling 
Reducing grain breakage 
Packaging 
Preservation 
Improving farmer value realization 
Possible technical approaches include:
Motorized dehulling 
Low-breakage processing mechanisms 
Pedal-operated systems 
Hand-operated mechanisms 
Improved storage and packaging solutions 
The objective is to make millet processing more accessible at the village or small-farmer level. 
PS-4: ZERO-CHEMICAL, ZERO-LOSS
Natural & Regenerative Farming
This track focuses on technologies and mechanisms that support natural and regenerative agricultural practices.
Possible areas include:
Soil health assessment 
Soil biological activity 
Bio-fertilizer management 
Organic pest management 
Natural farming support systems 
Low-cost agricultural diagnostics 
Possible technical approaches include:
Soil monitoring systems 
Optical/spectral analysis 
Bio-slurry management 
Low-cost diagnostic mechanisms 
Natural pest-control systems 
The focus should remain on practical, affordable and field-usable solutions. 
PS-5: MANDI BYPASS: FAIR BID
Digital Marketplaces
This track focuses on improving transparency, fairness and efficiency in agricultural markets.
Possible areas include:
Direct farmer-to-buyer platforms 
Digital auction systems 
Agricultural marketplaces 
Digital crop quality assessment 
Moisture measurement 
Transparent pricing 
Farmer access to buyers 
Possible technology approaches include:
Web applications 
Mobile applications 
IoT moisture meters 
Digital auction platforms 
SMS/IVR-based systems 
Solutions should demonstrate how technology can reduce information gaps and improve the farmer's ability to access fair markets. 
PS-6: OPEN INNOVATION IN AGRICULTURE
Grassroots Open Track
This is the open-ended agriculture innovation category.
Participants may identify an agricultural problem that does not fall directly under the other five tracks.
Potential areas include:
Horticulture 
Apiculture 
Sericulture 
Manual transplanting 
Farm safety 
Agricultural tools 
Post-harvest challenges 
Labour-intensive agricultural activities 
Other authentic rural/agricultural problems 
Participants must demonstrate that the selected problem is genuine and meaningful.
Unlike the standard tracks, the budget for this track can be justified according to the scale and nature of the problem.
However, purely abstract ideas are not acceptable. A working mechanism, application, prototype or meaningful demonstration is expected. 
7. SOLUTION DEVELOPMENT EXPECTATIONS
Participants are encouraged to follow a structured innovation process.
Step 1 – Identify the Problem
Clearly define the agricultural problem being addressed.
The team should identify:
Target user 
Agricultural activity involved 
Specific pain point 
Location/context 
Existing difficulty 
Step 2 – Understand the Root Cause
Participants should explain why the problem occurs rather than simply describing its symptoms.
Step 3 – Develop the Solution
The proposed solution should explain:
Core concept 
Working principle 
Components/technology 
User interaction 
Expected outcome 
Step 4 – Demonstrate Feasibility
Teams should demonstrate their solution through one of the accepted formats:
Physical prototype 
Hardware circuit 
Mechanical mechanism 
Functional simulation 
Wokwi/Tinkercad simulation 
Functional web application 
Functional mobile application 
The coordinator manual specifically allows working hardware, mechanical mechanisms, verified simulations and live web/mobile applications as demonstrations. 
Step 5 – Calculate Economics
Teams should explain:
Approximate development cost 
Bill of Materials 
Operating cost 
Expected savings/income 
Payback period 
Benefit to the target farmer 
For standard tracks, the BOM requirement is below ₹3,000; PS-6 does not have a fixed budget cap but requires commercial justification. 
8. MANDATORY DELIVERABLES
Every participating team should prepare the following:
1. Authentic Problem Definition
The team must clearly establish:
The agricultural problem 
Target user 
Crop/activity involved 
Operational difficulty 
Root cause 
2. Working Technical Solution / Demonstration
The team should demonstrate the solution using an appropriate format:
Hardware 
Mechanical prototype 
Simulation 
Web/mobile application 
Other functional demonstration 
3. Farmer Economics & BOM
The team should provide:
Component-wise cost 
Total implementation cost 
Expected economic benefit 
Estimated payback period 
4. Pitch Deck
Each team must prepare a structured presentation of approximately 6–8 slides. 
9. PITCH PRESENTATION STRUCTURE
The recommended pitch structure is:
Slide 1 – Title & Team Identity
Project title 
Track 
Team ID 
Team members 
Department 
Slide 2 – Real-World Problem
Problem statement 
Target users 
Agricultural context 
Existing difficulties 
Slide 3 – Proposed Solution
Solution overview 
Working principle 
Why the proposed solution is better 
Slide 4 – Working Demonstration
Prototype 
Simulation 
Mechanism 
Application workflow 
Slide 5 – Farmer Economics
BOM 
Cost 
Savings/benefit 
Payback period 
Slide 6 – Rural Feasibility
Reliability 
Power requirements 
Durability 
Maintenance 
Ease of use 
Slide 7 – Conclusion & Roadmap
Expected impact 
Future improvements 
Field-testing plan 
Scalability 
This seven-slide structure is directly aligned with the coordinator manual's recommended pitch architecture. 
10. PRESENTATION TIMING
Each team receives a 10-minute slot:
Segment
Time
Pitch + Demonstration
6 minutes
Jury Q&A / Defense
3 minutes
Team Transition
1 minute
Total
10 minutes
The six-minute pitch is strictly time-bound, followed by three minutes of jury questioning and one minute for transition. 
Suggested Time Management
Introduction & Problem – 1 minute 
Solution – 1 minute 
Technical Demonstration – 2 minutes 
Economics & Feasibility – 1 minute 
Impact & Conclusion – 1 minute 
11. JURY EVALUATION
The competition is evaluated out of 100 marks.
Evaluation Criterion
Marks
Real-World Relevance & Problem Grounding
25
Technical Innovation & Feasibility
25
Farmer Economics & GVA/Impact
25
Presentation, Demonstration & Jury Defense
25
Total
100
The official manual uses these four equally weighted criteria and specifies a qualifying benchmark of 50/100. 
12. EVALUATION GUIDELINES
A. Real-World Relevance – 25 Marks
Judges evaluate:
Is the problem genuine? 
Is the target user clearly identified? 
Is the agricultural context realistic? 
Does the solution address an actual need? 
Is the idea grounded in practical conditions? 
Generic or purely theoretical ideas should score poorly.
B. Technical Innovation & Feasibility – 25 Marks
Judges evaluate:
Technical approach 
Innovation 
Working principle 
Component selection 
Engineering feasibility 
Reliability 
Possibility of implementation 
C. Farmer Economics & Impact – 25 Marks
Judges evaluate:
Initial cost 
Affordability 
Operating cost 
Expected savings/revenue 
Payback period 
Potential agricultural impact 
Scalability 
D. Presentation, Demonstration & Jury Defense – 25 Marks
Judges evaluate:
Clarity of presentation 
Quality of demonstration 
Time management 
Technical explanation 
Ability to answer questions 
Understanding of limitations 
Confidence and justification 
The official framework specifically emphasizes technical defense, farmer cost and operational failure modes during Q&A. 
13. RULES & GUIDELINES
Each team may select only one official challenge track. 
The proposed solution must be relevant to the selected track. 
The problem addressed must have real-world agricultural relevance. 
Purely theoretical ideas should not be considered competitive submissions. 
Teams should be prepared to demonstrate their proposed solution. 
Standard challenge tracks should maintain a BOM below ₹3,000. 
PS-6 follows a justified-budget model. 
Teams must clearly explain the technical feasibility of their solution. 
Teams must explain the expected economic benefit to the target user. 
Participants must follow the prescribed presentation time. 
Judges' decisions regarding scoring and ranking shall be considered final. 
Any additional technical or administrative rules may be announced by the organizing committee before the competition. 
14. EVENT-DAY STRUCTURE
The event should follow the general sequence below:
Phase 1 – Registration & Verification
Participant registration 
Team verification 
Team ID allocation 
Attendance 
Phase 2 – Opening & Briefing
Welcome 
Event introduction 
Rules 
Theme clarification 
Judging criteria 
Presentation instructions 
Phase 3 – Team Preparation
Teams finalize:
Pitch deck 
Prototype/demo 
Economics 
Technical explanation 
Phase 4 – Innovation Pitching
Each team receives its allotted 10-minute slot.
Phase 5 – Jury Defense
Judges question the team regarding:
Technical feasibility 
Cost 
Practical implementation 
Failure conditions 
Farmer usability 
Scalability 
Phase 6 – Evaluation & Tabulation
Scores are collected and verified.
Phase 7 – Result Declaration
Final ranking 
Winner announcement 
Certificates/prizes 
Closing 
15. JURY & SCORING MANAGEMENT
The recommended jury consists of 2–3 domain experts and faculty members. 
For scoring:
Each judge evaluates independently. 
Scores are consolidated by the organizing team. 
Where multiple judges are used, the final aggregate can be calculated using the arithmetic average of judges' scores. 
Scores should be cross-verified before final rankings are announced. 
Tie-Breaking Order
If two teams receive identical aggregate scores, the following priority may be used:
Higher Real-World Relevance & Problem Grounding 
Higher Technical Innovation & Feasibility 
Higher Farmer Economics & Impact 
Jury/faculty consensus review 
16. INFRASTRUCTURE REQUIREMENTS
The organizing team should arrange:
Venue
Smart classroom / seminar hall 
Seating for participants 
Jury seating 
Presentation area 
Technical
Projector/display 
Laptop 
HDMI/VGA adapters 
Internet connection 
Power extension boards 
Speakers if required 
Presentation
Timer 
Microphone if required 
Presentation clicker 
Backup laptop 
Backup copies of presentations 
Demonstration
Demo tables 
Power supply 
Extension boards 
Required safety arrangements 
17. ORGANIZING TEAM RESPONSIBILITIES
Event Coordinator
Responsible for:
Overall event planning 
Faculty coordination 
Jury coordination 
Final decision-making 
Event execution 
Co-Coordinator
Responsible for:
Participant coordination 
Volunteer management 
Registration 
On-ground execution 
Supporting the Event Coordinator 
Registration Team
Responsible for:
Registration records 
Fee collection 
Team details 
Team IDs 
Attendance 
Technical Team
Responsible for:
Projector/laptop 
Internet 
Power 
Demonstration setup 
Presentation support 
Backup arrangements 
Jury Coordination Team
Responsible for:
Jury briefing 
Score sheets 
Team sequence 
Time management 
Score collection 
Media Team
Responsible for:
Posters 
Social media creatives 
Event photography 
Reels/videos 
Winner announcements 
Promotional material 
Volunteers
Responsible for:
Participant guidance 
Seating 
Team movement 
Timekeeping 
Venue management 
Basic technical assistance 
18. FUTURE DEVELOPMENT / POST-EVENT OPPORTUNITY
TRIGUNA may also serve as a platform for identifying promising agricultural innovations that can be developed beyond the competition.
Outstanding ideas may be considered for:
Further mentorship 
Prototype development 
Technical guidance 
Field validation 
Future innovation programs 
Further development opportunities 
This aspect should be presented as an opportunity for promising ideas, rather than as a guaranteed post-event benefit.
19. EVENT IDENTITY
Core Identity
TRIGUNA – Agriculture Innovation Challenge
Suggested Tagline
Find the Problem. Build the Idea. Pitch the Impact.
Event Philosophy
In the game of innovation, only the strongest ideas survive.
The Squid Game theme can be incorporated primarily through the visual identity, branding, graphics and event atmosphere, while keeping the actual competition academically and professionally focused.
20. SHORT DESCRIPTION FOR FUTURE USE
TRIGUNA is an agriculture-focused innovation and pitching competition where students identify real-world agricultural challenges and develop practical, technically feasible and economically viable solutions. Participants compete across multiple agriculture innovation domains including precision farming, dairy and fisheries, millet processing, regenerative farming, digital agricultural markets and open agricultural innovation. Teams are expected to demonstrate their solution through a prototype, simulation, mechanism or functional application and defend their idea before a panel of judges.
21. INTERNAL ONE-LINE EXPLANATION
TRIGUNA is a problem-to-pitch agriculture innovation challenge where participants identify a genuine agricultural problem, develop a practical solution, demonstrate its feasibility, calculate its economic value and pitch it to a jury.
22. MASTER EVENT FLOW
AGRICULTURAL PROBLEM↓SELECT CHALLENGE DOMAIN↓UNDERSTAND THE PROBLEM↓IDENTIFY ROOT CAUSE↓DEVELOP SOLUTION↓BUILD / SIMULATE / DEMONSTRATE↓CALCULATE COST & IMPACT↓PREPARE PITCH↓PRESENT↓JURY DEFENSE↓EVALUATION↓WINNER↓POSSIBLE FURTHER DEVELOPMENT

# VISIONEXPO.docx
VISIONEXPO
POSTER PRESENTATION COMPETITION
Event Structure & Master Operations Document
Organized By: Department of Industrial Internet of Things (IIoT)Event: VISIONEXPOEvent Type: Poster Presentation CompetitionTheme: Industrial Excellence, Lean Manufacturing & Visual CommunicationIn Association With: Bajaj BMSTagline: Visualize. Innovate. Excel.
Event Date: 10 September 2026Coordinator: Pari Chillure (9370685529)Co-coordinator: Sarthak Band (9823554369)
Participation: Individual  Registration Fee: ₹30 
1. EVENT OVERVIEW
VISIONEXPO is a poster presentation competition designed to encourage students to understand, interpret and visually communicate important concepts related to Lean Manufacturing and Industrial Excellence.
The event provides participants with an opportunity to convert technical concepts into creative, informative and visually effective posters.
Participants are assigned or select a specific industrial concept/theme and prepare a poster explaining the concept in a simple, attractive and technically accurate manner.
The competition combines:
Technical understanding 
Visual communication 
Creativity 
Industrial awareness 
Presentation skills 
Practical interpretation of manufacturing concepts 
The event is designed to make industrial engineering and manufacturing concepts more engaging and accessible through visual storytelling.
2. EVENT OBJECTIVES
The primary objectives of VISIONEXPO are:
To encourage students to understand Lean Manufacturing concepts. 
To develop students' ability to communicate technical concepts visually. 
To connect classroom learning with industrial applications. 
To promote awareness of Industrial Excellence practices. 
To encourage creativity in technical communication. 
To develop presentation and explanation skills. 
To encourage students to interpret industrial concepts through practical examples. 
To provide participants with an opportunity to interact with industry professionals. 
To allow students to demonstrate their understanding of concepts covered during their BMS/industrial learning experience. 
3. CORE EVENT PHILOSOPHY
VISIONEXPO is not simply a drawing or art competition.
The primary focus is technical understanding presented through visual communication.
A successful poster should therefore achieve three things:
UNDERSTAND
The participant must understand the assigned industrial concept.
VISUALIZE
The participant must convert the concept into an understandable visual format.
EXPLAIN
The participant must be able to confidently explain the poster and answer questions from the evaluators.
The competition therefore evaluates both what the poster communicates and how well the participant understands and presents it.
4. TARGET PARTICIPANTS
VISIONEXPO is open to students who wish to demonstrate their understanding of Lean Manufacturing and Industrial Excellence concepts.
Participation may be:
Individual, or 
In teams of up to 2 members. 
The exact number of participating teams may be decided by the organizing committee depending on venue capacity and event requirements.
5. EVENT CONCEPT
The event follows a simple Theme → Understand → Visualize → Present → Evaluate model.
Overall Journey
Theme Allocation / Selection↓Understand the Concept↓Research & Prepare Content↓Design the Poster↓Poster Submission / Screening↓Poster Exhibition↓Presentation & Interaction↓Jury Evaluation↓Winner Announcement
The event consists of two primary stages:
ROUND 1 – Poster Concept / Preliminary Screening
Participants submit their initial poster concept or rough draft for evaluation and shortlisting.
ROUND 2 – Poster Exhibition & Presentation
Shortlisted participants present their final posters before the judges and explain the selected concept.
6. OFFICIAL POSTER THEMES
The following themes form the core subject areas for VISIONEXPO.
1. 5S
Focus on workplace organization and efficiency through:
Sort 
Set in Order 
Shine 
Standardize 
Sustain 
Participants should demonstrate how 5S can improve workplace efficiency, safety and organization.
2. POKA-YOKE
Focus on mistake-proofing in industrial processes.
The poster may demonstrate:
Common human errors 
Prevention mechanisms 
Industrial examples 
Simple mistake-proofing techniques 
3. 7 WASTES
Focus on identifying and eliminating the major forms of waste in manufacturing.
The poster should communicate the different categories of waste and their effect on productivity and efficiency.
4. TPM – TOTAL PRODUCTIVE MAINTENANCE
Focus on maintaining equipment effectiveness through proactive and preventive maintenance practices.
The poster may illustrate:
Equipment maintenance 
Breakdown prevention 
Operator involvement 
Productivity improvement 
5. 7 QC TOOLS
Focus on the fundamental quality-control tools used to identify, analyze and solve quality problems.
Participants should present the tools in a clear and visually understandable format.
6. VISUAL MANAGEMENT
Focus on communicating information clearly through visual systems within an industrial environment.
Examples may include:
Visual indicators 
Workplace boards 
Status displays 
Signage 
Color coding 
Performance boards 
7. OHNO CIRCLE
Focus on the concept of observing an actual workplace/process directly to identify problems and waste.
The poster should explain the importance of going to the actual place of work and observing the process.
8. CLIRT
Participants should explain the CLIRT concept and demonstrate its relevance to industrial operations and workplace improvement.
The presentation should focus on understanding and practical application rather than simply defining the term.
9. ECRS
Focus on process improvement through:
Eliminate 
Combine 
Rearrange 
Simplify 
Participants should demonstrate how ECRS can be used to improve an existing process.
10. 7 ABNORMALITIES
Focus on recognizing and identifying abnormalities within an industrial process or workplace.
The poster should demonstrate how abnormalities can be identified and addressed before they lead to larger problems.
11. MOTION ECONOMY
Focus on reducing unnecessary human movement and improving efficiency in manual operations.
Participants may demonstrate:
Unnecessary movements 
Efficient workplace arrangement 
Ergonomic considerations 
Improved work methods 
12. RFT – RIGHT FIRST TIME
Focus on producing the correct output at the first attempt without defects or rework.
The poster should communicate the relationship between:
Quality → Rework Reduction → Productivity → Customer Satisfaction
13. BASIC SAFETY
Focus on fundamental workplace safety practices.
Participants may visually communicate:
Safety procedures 
PPE 
Workplace hazards 
Safe working practices 
Accident prevention 
14. KAIZEN
Focus on continuous improvement through small, incremental changes.
The poster should demonstrate how continuous improvement can improve:
Quality 
Productivity 
Safety 
Cost 
Efficiency 
7. POSTER REQUIREMENTS
Each participating team must prepare a poster based on the assigned/selected theme.
The poster should:
Clearly communicate the selected concept. 
Contain technically accurate information. 
Include appropriate visual elements. 
Use diagrams, illustrations, process flows or examples wherever useful. 
Be understandable to a viewer without requiring lengthy verbal explanation. 
Demonstrate practical industrial relevance. 
Maintain a clean and organized layout. 
The exact poster size and submission format should be confirmed by the organizing committee before registration opens.
The original event draft specifies A3/chart-paper-based poster preparation/display requirements, along with colors, reference material, display boards and name tags as event requirements. 
8. ROUND 1 – PRELIMINARY SCREENING
The first round is intended to evaluate the participants' initial understanding and poster concept.
Participants submit:
Initial poster concept 
Rough design/layout 
Understanding of the selected theme 
Planned visual representation 
Key information to be included 
The organizing/jury team may shortlist entries based on:
Technical understanding 
Relevance to the theme 
Clarity 
Creativity 
Potential quality of the final poster 
Only shortlisted teams proceed to the final exhibition round.
9. ROUND 2 – POSTER EXHIBITION
Shortlisted participants prepare and display their final posters.
The exhibition allows judges and invited industry representatives to:
Observe the poster 
Interact with participants 
Ask questions 
Evaluate technical understanding 
Assess visual communication 
Discuss practical industrial applications 
Participants must be present during the exhibition and should be prepared to explain their poster whenever approached by the evaluators.
10. PRESENTATION & INTERACTION
The final round is not restricted to judging the appearance of the poster.
Participants should be able to explain:
What is the concept? 
Why is it important? 
How is it applied in industry? 
What problem does it solve? 
What is the practical benefit? 
Can they provide a real-world example? 
Judges may ask questions related to the selected theme to verify the participant's understanding.
11. JUDGING FRAMEWORK
The final evaluation should consider both the poster and the participant's understanding.
The recommended evaluation parameters are:
Criterion
Suggested Weightage
Technical Understanding & Accuracy
25
Relevance & Industrial Application
20
Visual Communication & Clarity
20
Creativity & Originality
15
Poster Design & Presentation
10
Explanation & Jury Interaction
10
Total
100
Note: The original event document states that the final judging criteria were to be provided/finalized by the Bajaj representatives. Therefore, this table should be treated as a master-framework recommendation, not a fixed official scoring scheme, until the jury/industry representatives approve it.
12. TECHNICAL UNDERSTANDING
Judges should assess whether the participant actually understands the selected concept.
Evaluation may include:
Correct definition 
Correct principles 
Appropriate terminology 
Accurate examples 
Understanding of practical application 
Ability to answer questions 
A visually attractive poster with incorrect technical information should not receive a high score.
13. INDUSTRIAL RELEVANCE
Participants should connect their theme to an actual industrial environment.
For example, the poster may explain:
Where the concept is used 
What industrial problem it solves 
How it improves a process 
What happens if the concept is not implemented 
How it contributes to Industrial Excellence 
The objective is to move beyond textbook definitions and show practical application.
14. VISUAL COMMUNICATION
The poster should communicate the concept quickly and clearly.
Judges may consider:
Layout 
Readability 
Visual hierarchy 
Diagrams 
Flowcharts 
Icons/illustrations 
Appropriate use of text 
Information organization 
The poster should avoid excessive text where the same information can be communicated visually.
15. CREATIVITY & ORIGINALITY
Participants are encouraged to present familiar industrial concepts in fresh and engaging ways.
Creativity may be demonstrated through:
Unique poster layouts 
Visual storytelling 
Practical examples 
Creative diagrams 
Before/after comparisons 
Process visualization 
Industrial scenarios 
Creativity should support the technical message rather than replace it.
16. AI & CONTENT AUTHENTICITY
The original VisionExpo draft includes a restriction on the use of AI tools such as ChatGPT, Midjourney, DALL-E, Canva AI and similar tools for generating poster content, text or artwork.
Under the original draft framework:
Posters are expected to be self-created. 
AI-generated content/artwork is not permitted. 
Participants should demonstrate their own understanding and creativity. 
External reference material may be used for learning, but the final poster should be the participant's own work. 
Important: This rule should be reconfirmed by the organizing committee before the final event rules are published, especially because AI policies and available design tools may change from year to year.
17. RULES & REGULATIONS
Each participant/team must work on an approved/assigned theme. 
Each team may consist of a maximum of 2 members. 
Participants must prepare an original poster. 
The poster must be technically accurate and relevant to the assigned theme. 
Participants must be present during the final exhibition. 
Participants must be able to explain their poster to the judges. 
The poster should not contain inappropriate, offensive or unrelated content. 
Posters must not damage venue property. 
Participants must follow the prescribed submission and display format. 
Any use of AI tools will be governed by the final AI policy announced by the organizing committee. 
Registration fees, once paid, shall be non-refundable unless otherwise decided by the organizing committee. 
The decision of the jury shall be considered final. 
These points retain the main rule structure from the original VisionExpo draft, while leaving room for the organizing committee to finalize details.
18. EVENT-DAY FLOW
Phase 1 – Registration
Participant verification 
Team confirmation 
Theme verification 
Attendance 
Phase 2 – Briefing
Welcome 
Event introduction 
Rules 
Judging criteria 
Exhibition instructions 
Phase 3 – Preliminary Screening
Submission of initial concept/rough draft 
Evaluation 
Shortlisting 
Phase 4 – Final Poster Preparation
Shortlisted teams prepare their final posters according to the prescribed specifications.
Phase 5 – Poster Exhibition
Participants display their posters at their allotted locations.
Phase 6 – Jury Interaction
Judges move through the exhibition and:
Evaluate posters 
Interact with participants 
Ask questions 
Record scores 
Phase 7 – Score Compilation
The organizing team collects and verifies the score sheets.
Phase 8 – Winner Announcement
Final results 
Winner announcement 
Prize/certificate distribution 
Closing 
19. INFRASTRUCTURE REQUIREMENTS
The organizing team should arrange:
Venue
Exhibition/classroom space 
Display boards 
Tables if required 
Participant identification/name tags 
Poster Display
Display boards 
Clips/pins/tape as appropriate 
Team identification cards 
Theme labels 
Jury Requirements
Jury seating 
Score sheets 
Pens 
Evaluation sheets 
Participant/team list 
General
Registration desk 
Attendance sheet 
Certificates 
Prize arrangements 
Photography/video coverage 
20. ORGANIZING TEAM RESPONSIBILITIES
Event Coordinator
Responsible for:
Overall event planning 
Faculty coordination 
Industry/jury coordination 
Final event decisions 
Event execution 
Co-Coordinator
Responsible for:
Participant coordination 
Volunteer allocation 
Registration support 
Exhibition management 
On-ground execution 
Registration Team
Responsible for:
Registration records 
Fee collection 
Team information 
Attendance 
Team IDs 
Exhibition Team
Responsible for:
Display-board allocation 
Poster placement 
Theme identification 
Participant movement 
Venue arrangement 
Jury Coordination Team
Responsible for:
Jury briefing 
Score sheets 
Evaluation sequence 
Participant interaction 
Score collection 
Media Team
Responsible for:
Promotional creatives 
Poster/reel creation 
Event photography 
Exhibition coverage 
Winner announcement 
21. INDUSTRY INTERACTION
A key feature of VISIONEXPO is interaction with industry representatives.
Where available, representatives from Bajaj BMS may participate in the evaluation and interaction process.
Their involvement can provide participants with:
Industry perspective 
Practical feedback 
Concept validation 
Understanding of real-world applications 
Exposure to industrial expectations 
The exact role and evaluation responsibilities of industry representatives should be finalized with the concerned representatives before the event.
22. FUTURE EDITION STRUCTURE
The VISIONEXPO format can be retained for future editions while changing:
Industrial themes 
Partner/industry organization 
Poster format 
Number of rounds 
Evaluation criteria 
Exhibition format 
Jury composition 
Design restrictions 
Digital/physical submission method 
The fundamental structure can remain:
Learn → Visualize → Create → Exhibit → Explain → Evaluate
This allows VISIONEXPO to become a recurring event while keeping the format familiar to the organizing team.
23. EVENT IDENTITY
Event Name
VISIONEXPO
Event Type
Poster Presentation Competition
Tagline
Visualize. Innovate. Excel.
Core Message
Turn Industrial Concepts into Visual Ideas.
Event Philosophy
Understand the concept. Visualize the process. Communicate the impact.
24. SHORT DESCRIPTION FOR WEBSITE / BROCHURE
VISIONEXPO is a poster presentation competition focused on Lean Manufacturing and Industrial Excellence. Participants showcase their understanding of industrial concepts through creative and informative posters, connecting classroom learning with practical industrial applications. The event combines technical knowledge, visual communication and presentation skills, with participants getting an opportunity to interact with industry representatives and demonstrate their understanding of the selected theme.
25. INTERNAL ONE-LINE EXPLANATION
VISIONEXPO is a technical poster presentation competition where students are given industrial excellence themes, create visually engaging posters explaining the concepts and their applications, and present them before judges and industry representatives.
26. MASTER EVENT FLOW
SELECT / ALLOT THEME↓UNDERSTAND THE CONCEPT↓RESEARCH & PLAN↓CREATE POSTER↓PRELIMINARY SCREENING↓SHORTLISTING↓FINAL POSTER EXHIBITION↓JURY INTERACTION↓EVALUATION↓RESULTS↓WINNER
27. MASTER CHECKLIST FOR FUTURE COORDINATORS
Before announcing VISIONEXPO, the organizing team should finalize:
Event Details
Date 
Venue 
Coordinator 
Co-Coordinator 
Registration fee 
Team size 
Maximum number of teams 
Themes
Final theme list 
Theme allotment/selection method 
Theme change policy 
Poster
Poster size 
Physical/digital format 
Submission deadline 
Display requirements 
Design restrictions 
AI Policy
Whether AI-generated text is allowed 
Whether AI-generated artwork is allowed 
Whether AI-assisted design is allowed 
Verification mechanism, if required 
Jury
Jury members 
Industry representatives 
Final judging criteria 
Score sheets 
Tie-breaking mechanism 
Venue
Display boards 
Tables 
Pins/tape 
Name tags 
Registration desk 
Jury seating 
Media
Poster 
Instagram creatives 
Registration announcement 
Theme announcement 
Shortlisting announcement 
Event coverage 
Winner announcement

