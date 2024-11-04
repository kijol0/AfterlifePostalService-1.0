# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Rika")
define a = Character("???",color="#E4080A")
define b = Character("Pendy",color="#E4080A")

# image character= "pendy normal.png"
# define resize_character=:
# image resize_character = im.Scale(character,400,400)

# The game starts here.

label start:
    "Hi, I'm Rika! Just an ordinary staff from National Postal Service. Nice to meet you~"

    "Can you imagine … that one day, you suddenly have to deal with ghosts after your work shift is over?"

    "Crazy, right?! Haha, now you gotta work extra hours just to deal with them."

    "Well, when did this start happening to me, you may ask …?"

    "Of course, on this eventful night."

label scene1: 
    
    scene bg floor with fade
    
    "It's a rainy night in Rajawali village, the place where Rika works. She cannot go home because she doesn't bring her umbrella. Her homestay is deep within the village, far away from the office that is placed on the edge, a little bit closer to the nearby city."
    
    show rika fun

    e "Huh, how did it come to this …? Today's shift is over, but suddenly I got a bunch of mail that needs to be checked today."
    
    e"… then it starts pouring when I'm done. Aaand I don't have my umbrella. Great."
    
    e"I don't think I'm going home tonight. Road's gonna be muddy."

    "Suddenly, she hears knocking sounds from the front door. Slow knocks, but so loud that it pierces through the sound of rain"
    show rika normal
    e "Eh, a customer?"

    "She slowly walks toward the door. She cannot really see the figure behind the foggy door. The knocking sound doesn't stop. She then unlocks and opens it."
    
    e"Sorry, we are clo—"
    show rika shock
    e"Wha!?"

label scene2:
    scene bg floor with fade
    show rika shock at left 
    with move 
    pause(3.0)
    show pendy normal at right 
    with moveinright 
    pause(3.0)
    

    "She finds out a man wrapped tightly in a white cloth over his whole body. He seems skinny just by looking at his face. His eyes are blank, with dark circles around them."
    
    e"So–sorry, sir. Is this a Halloween costume play? Because I don't think it’s Halloween right now."
    show pendy sad
    a"N–no, miss. I'm so sorry about my appearance, but this is just how I am."
    
    e"W–wait, are you a–a real ghost!?"
    show pendy shock
    a"Wait, miss! Don't be scared, I need your help!"
    show rika normal
    e"Of course I'd be scared! But …, why would you need my help?"

    a"Uhh, it's a long story."

    e"I guess … we can talk about it inside. It's getting cold out here."
    show pendy fun
    a"Thank you, miss! Thank you! If only my hands weren't tied, I want to shake your hands!"
    show rika normal
    e"Umm, I would decline respectfully. Thank you for your good intention though"

label scene3:
    scene black with fade
    "Rika goes inside first. Then, she observes the cloth-wrapped man jumping around and almost bumping into things."

    scene bg room with fade
    show rika normal at right
    
    e"With all due respect, sir. Can you please move normally?"
    show pendy shock at left
    a"No, I can't! These seven knots are binding me, binding my soul to this world!"
    show pendy sad
    e"So, you need me to untie these knots?"
    show pendy normal
    a"No, no, if you untie these in the wrong order, you will be cursed!"
    show rika fun
    e"Wow, okay, no curse, thanks! But, how can I help you, then?"
    
    a"This is a postal office, right?"
    show rika normal
    e"Yes, and?"
    
    a"Can you write a message for me?"
    
    e"To whom, may I ask?"
    
    a"My family, of course. They did the funeral and such."
    hide rika
    hide pendy

    "Thus, Rika turns on her computer and opens a blank text file. She then prepares some questions in mind to know more about her “ghostly client”."

    show rika normal at right
    e"May I know your identity, sir?"
    show pendy normal at left
    b"My name is Pendy, miss. I was 30 before I died due to a tragic accident during a ceremony. I lived with my family at Bhuana Street Number 12, Rajawali Village."

    "Pendy then tells his inquiry for the letter. Rika keeps typing while hearing his story and his needs. Some time has passed, Rika shows the letter draft to the man, which has a few blanks on it."

    e"Sir, I'm going to ask you a few more questions, so that I can complete the draft."

    b"Sure! Is there anything else you would like to know?"

default ask_affection=0

label scene4:
    scene bg room with fade
    show pendy fun
# (Multiple choice box appears, Pendy appears as a “pop-up tutorial” in the dialogue box.)

    b"Phew, let me catch a breath first. It's exhausting to jump around all night, y'know."
    show pendy normal
    b" … Alright. As you can see, there are several options to pick on the multiple choice box."
    b"From all options available during “Q&A session”, you may only choose three."
    show pendy fun
    b"Please try to pick up the most important ones that may help you compose the letter!"

label ask:
    menu optional_name:
        "Say Statement"
        "Ask about his relationship":
            $ask_affection= ask_affection + 1
            jump choice1_a
        "Ask about his funeral process":
            $ask_affection= ask_affection + 1
            jump choice1_b
        "Ask about his hobbies":
            
            jump choice1_c
        "Ask about what will happen next":
            $ask_affection= ask_affection + 1
            jump choice1_d
        "Ask about the afterlife experience":
            
            jump choice1_e

    label choice1_a:
        e"How's your relationship?"
        show pendy sad
        b"I'm actually married. But, we have no kids. Ah, my poor wife."
        e"How about with your family, sir?"
        show pendy fun
        b"I'm really close and warm with my family. I'm starting to miss them already."
        jump ask_evaluation

    label choice1_b:
        e"So, how did your funeral go, sir?"
        show pendy sad
        b"It was a small one. Only my family and relatives attended it."
        e"How's the process of your funeral?"
        
        b"It was arranged by my dad. I think he mostly did the process, like giving me the last bath, wrapping me up with white cloth, and transporting my corpse to the graveyard."
        e"Anyone else beside your dad?"
        show pendy normal
        b"I think my brother also helped during the process, but not that much."
        jump ask_evaluation

    label choice1_c:
        e"Do you have any hobbies, sir?"
        show pendy shock
        b"Uhh, would that help you with the letter, miss?"
        show pendy normal
        e"We will see."
        b"Are you sure?"
    
    default ask2_affection=0
    label ask2:
        menu :
            b"Are you sure?"
            "100 percent sure (spend the chance)":
                $ask_affection= ask_affection + 1
                $ask2_affection= ask2_affection + 1
                jump choice2_a
            "Nah, I'm kidding": 
                jump choice2_b
            

        label ask2_evaluation:
        if ask2_affection>=1:
            jump choice2_a
        else:
            jump choice2_b
        
        label choice2_a:
            b"Well, okay."
            show pendy normal
            b"I used to be a soccer fan. I've been playing soccer for my school's team back in high school."
            e"I gotta ask the “million dollar question”. Who is the Greatest of All Time?"
            show pendy fun
            b"Haha, why do you even ask!? Of course, it's gotta be … SIU—” "
        
            show pendy shock with hpunch
            "Pendy jumps around and rotates mid-air, trying to imitate a certain soccer player. Of course, his major setback causes him to trip and fall."

            e"Oh my goodness! Are you okay, sir?"
            show pendy fun
            b"Ah, hahaha! I was too carried away."
            e"Maybe I shouldn't have asked that."
            b"I guess it's fine. I haven't had a good laugh in a while!"
        jump ask_evaluation
        label choice2_b:
            show pendy fun
            b"Haha, alright. Ask me anything else!"
        jump ask_evaluation

    label choice1_d:
        e"So, what will happen if your knots are untied?"
        show pendy normal
        b "Well, my spirit will be free and I will no longer linger around this world."
        e"Isn't it a bit sad because you won't see them again for quite some time?"
        show pendy sad
        b"A bit, yeah. But, I no longer belong to this world, miss. I'm too tired wandering aimlessly."

        jump ask_evaluation

    label choice1_e:
        e"How are you doing in the afterlife?"
        show pendy shock
        b"Uhh, would that help with the letter?"

        default ask3_affection=0
        label ask3:
        menu :
            b"Are you sure?"
            "Certainly. (spend the chance)":
                $ask_affection= ask_affection + 1
                $ask3_affection= ask3_affection + 1
                jump choice3_a
            "Never mind. (don't spend the chance)": 
                jump choice3_b
            

                label ask3_evaluation:
                if ask3_affection>=1:
                    jump choice3_a
                else:
                    jump choice3_b

                label choice3_a:
                    b" Sure …, I guess. After two years, I can say that it's been a mixed bag."
                    e"Can you elaborate, sir?"
                    b"Well, I've tried my best to just live my “life”. There are times that I find other spirits, or in other words, my friends. But, some have already departed from this world, either because they found peace or were banished by the exorcists."
                    e"Just like in the living world, huh?"
                    b"Yes. I wish I could depart as well, so I'll be able to reunite with them."
            
                label choice3_b:
                    b"Haha, alright. Ask me anything else!"
                    jump ask_evaluation

    label ask_evaluation:
        if ask_affection>=3:
            jump scene_after_ask
        else:
            jump ask

label scene_after_ask:
    scene bg room with fade 
    show pendy normal at left
    show rika normal at right
    e"Alright, I think that's enough. I'll do my best to compose the letter for you, sir."
    b"Okay … umm."
    e"Any problems, sir?"
    show pendy shock
    b"N–nothing! I think I'll just take a look because, umm, I can't really sit."
    e"Okay, but it makes me kind of nervous though."

label scene_post:
    scene black
    " From:Pendy \n
    To:Pendy's Family, \n
    Bhuana Street Number 12, Rajawali Village."

    "Dear my family,"
    "I'm sending this letter from beyond the grave because I need you all to know that_____"
    "I'm truly fortunate to meet this kind person to write this message in my stead. But, I also have something important to ask you to do, especially ______ ."
    "I want to bring the bad news that this whole time, nobody doesn't remember to untie the knots that wrapped up my body. That's why I'm still roaming this earth as a pocong until today. My spirit is still bound to my already-feeble body. So, please help me _____."

    "With love,"
    "Pendy"
label post:
    scene bg room with fade
    default post_affection=0.0
    show pendy normal 
    b"Hmm, you still haven't filled up the blanks."
    b"Maybe the information I gave you earlier is useful, after all."
    show pendy fun
    b"Pick up one of the three choices to fill up each blank. The choice you pick will determine your rating from me."

    "I'm sending this letter from beyond the grave because I need you all to know that _____"
    menu :
        "what will i fill?"
        
        "I wish you all well.":
            $post_affection= post_affection + 0.5
        "I really love you all.":
            $post_affection= post_affection + 1
        "I'm still alive and kicking":
            $post_affection= post_affection + 0
    " I'm truly fortunate to meet this kind person to write this message in my stead. But, I also have something important to ask you to do, especially _____"
    menu :
        "what will i fill?"

        "Mom.":
            $post_affection= post_affection + 0
        "my dear brother.":
            $post_affection= post_affection + 0.5
        "Dad.":
            $post_affection= post_affection + 1

    "I want to bring the bad news that this whole time, nobody doesn't remember to untie the knots that wrapped up my body. That's why I'm still roaming this earth as a pocong until today. My spirit is still bound to my already-feeble body. So, please help me _____."
    menu :

        "what will i fill?"
            
        "free from this world.":
            $post_affection= post_affection + 1
            
        "die again.":
            $post_affection= post_affection + 0
            
        "rest eternally.":
            $post_affection= post_affection + 0.5
    
    "After she is finished writing the letter, she carefully prints a copy on the blank paper"

    e"Alright, sir. I'll send this tomorrow to your family. Please come back if you're still having the problem."
    show pendy fun
    b"Thank you so much, miss!"

label post_evaluation:
        if post_affection<1:
            jump bad_end
        if  1<=post_affection<3 :
            jump neutral_end
        else :
            jump good_end

label good_end:
    scene black with fade
    "Within the next few nights, the wrapped-up man isn't coming back to the office. She can finally assume that his problem was solved already."
    scene bg room with fade
    show rika normal with fade
    e"I guess we won't be seeing each other again for a while."
    e"I’m so glad you can depart from this world, sir."
    jump epilog

label neutral_end:
    scene black with fade
    "Within the next few nights, Pendy comes back to the office. As promised, Rika stays in the office after her work shift."
    scene bg room with fade
    show pendy normal at left
    e"Hello again, sir."
    b"Hello, miss. I appreciate your effort and help. But, I think I'm still bound here."
    show rika normal at right
    e"Ah, right. About that, your family didn't really believe my words. I guess the letter isn't convincing enough."
    show pendy sad
    b"It's fine. I guess I'll be on my way."

    "And so the wrapped-up man departs from the office, with the hint of sadness in the air."

    jump epilog

label bad_end:
    scene floor with fade
    "Within the next few nights, Pendy comes back to the office. As promised, Rika stays in the office after her work shift."
    show rika normal at right
    e"Hello again, sir."
    show pendy normal at left
    b "Hello, miss. I appreciate your effort and help. But, I think I'm still bound here."
    e"Ah, right. About that, your family didn't believe the letter at all. They said that I only made things up."
    b"Huh? Let me see the letter, then."

    "She opens the letter wide for Pendy to see. Just a few moments later, she can see a change in Pendy's clothing. It gradually turns red!"
    show pendy pink
    b"Did you not take this whole thing seriously?"
    show rika shock
    e"Well, I didn't mean to–"
    b"Enough! I'll come back to haunt you for the rest of your life!"
    scene black with fade
    "He jumps around and bumps into many things, making a scene. He leaves still with his anger that seeps through his clothing. Red … is he really going to haunt me as revenge?"

label epilog:
    scene bg floor with fade
    "That's how I get to know that I can see things that we humans could not normally see."
    "Also, that's how I know about a man who was once known as Pendy."

    "On a rainy night after a normal work shift ends, it is relatively quiet, only the sound of rain pouring outside. Rika is yet again doing overtime, but this time, she is intended to stay in the office. She patiently waits for another “customer” that will probably show up during the rainy night."
    show rangda
    a"~!!"
    "to be continue..."

label credit:
    scene black with fade

    "AfterlifePostalService-1.0"

    "Team Lead \n Ginanjar Maulana"
    "Producer \n -Hana "
    "programmer \n - Muhammad Rizal Fauzi"
    "artis \n - Ginanjar Maulana"
    "narrativedesigner \n
    - Fayden Daryn\n
    - Zayn Jayadisastra"
    
    
    return
