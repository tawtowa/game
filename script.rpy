# Declare characters used by this game.
define D= Character ( 'Dave', color= "#0004e6")
define p= Character ( 'pokwang', color= "#ff0000")
define C= Character ( 'Creator', color= "#00f7ff")

label start1: 
# declare the video here : A
image launch = Movie(play="oa4_launch.mp4", pos=(10, 10), anchor=(0, 0))
 

 
label start: 
   
    scene start
    with fade

    voice "audio/creator.mp3"
    C"Choose your character"

    menu:

    
        "Girl":

            jump Girl
        "Boy":
            jump Boy
 
label Girl:
    default Location= "image"
    voice "audio/pokwang.mp3"
    "pokwang" "Hi! this is pokwang before we start
            I would like to introduce the name of the 3 guy who Created of this project"
    voice "audio/pokwang1.mp3"
    "pokwang" "Justin Montajes, Johnrey Gardoña and Roldan Montoya"
    
    voice "audio/pokwang2.mp3"
    "pokwang" "Thank you for being patient, And lets Start now our tour"
     
    

label sprites:
    scene front
    show pokwang animated:
   
            xalign 0.5
            yalign 1.1
            "pokwang talk" 
            pause .3
     
            "pokwang normal"
            pause .3
            repeat 6
    voice "audio/pokwang3.mp3"
    "Pokwang" "Good day, everyone! Welcome to ACLC College of Daet. "
 

    show pokwang animated:

            xalign 0.5
            yalign 1.1
            "pokwang happy"
            pause .2
     
            "pokwang thappy"
            pause .3
            repeat 12
    
   
 
    voice "audio/pokwang4.mp3"
    "Pokwang" "My name is Pokwang, and I'll be your guide today as we explore the fantastic 
                facilities of our campus."

    scene option
    show pokwang animated:
            xalign 0.5
            yalign 1.1
            "pokwang happy"
            pause .2
     
            "pokwang thappy"
            pause .3
            repeat 4
label choices:
    default learned = False
    voice "audio/pokwang5.mp3"
    "Pokwang" " Are you ready for an exciting journey?"
    
    menu:

        "Yes, I do.":
            jump choice1_yes
        "Skip Computer lab":
            jump flab3
        "Skip Registrar":
            jump reg
            
        "Skip Library":
            jump lib
        "Skip Admission office":
            jump admission
        "No, I don't.":
            jump  choice1_no

    $ menu_flag = True

    scene flab3 
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .4
        repeat 7

    voice "audio/pokwang14.mp3" 
   
    label choice1_yes:

    $ menu_flag = True
label background:
        scene hall1
        play sound "crowd.mp3"
        show pokwang animated:
            xalign 1.0
            yalign 1.0
            "pokwang talk"
            pause .2
     
            "pokwang normal"
            pause .2
            repeat 2
        
        voice "audio/pokwang6.mp3"
        "Pokwang" "We are now in Hallway"
     
        scene hall1
        show pokwang animated:
        
            xalign 0.5
            yalign 1.0
            "pokwang talk"
            pause .3
     
            "pokwang normal"
            pause .3
            repeat 15
        voice "audio/pokwang7.mp3"
        "Pokwang" " Before we proced to our first destination, I will going to show some of the photos of the activies and programs 
        that happen in this hallway "
        
        scene hall1:
            xalign 0.7
            yalign 1.0
            "h2"    with wiperight
            pause 2
     
            "h3"     with wiperight
            pause 2
    
            "h4"     with wiperight
            pause 2
       
            "h5"     with wiperight

            pause 2
            repeat 10
        play sound "creepy.mp3"
        define teleport = ImageDissolve("pokwang normal.png", 1.0, 0)   
        show pokwang normal:   
          
            xalign 0.9   
            yalign 1.0
       
            "pokwang h1"    with teleport 
            pause .3
     
            "pokwang h2"  with teleport 
            pause .3
            repeat 12
        
        
        voice "audio/pokwang8.mp3"
        "Pokwang" " The first one is Halloween party. all students, are required to wear customes, to be come the part of the celebration"
        show pokwang normal:   
          
            xalign 0.9   
            yalign 1.0
       
            "pokwang h1"    with teleport 
            pause .3
     
            "pokwang h2"  with teleport 
            pause .3
            repeat 11
        voice "audio/pokwang9.mp3"
        "Pokwang" " Every Strand from College to Senior High, have a candidates to participate for the best custome a ward and win the cash prizes."
        

        scene s1:
            xalign 0.9
            yalign 1.0
            "s2"    with wiperight
            pause 1.5
     
            "s3"     with wiperight
            pause 1.5
    
            "s4"     with wiperight
            pause 1.5
       
            "s5"     with wiperight
            pause 1.5
            repeat 1
        
        show pokwang animated:
        
            xalign 0.9
            yalign 1.0
            "pokwang talk"
            pause .3
     
            "pokwang normal"
            pause .4
            repeat 18
        
        voice "audio/ssc.mp3"
        "Pokwang" "And this is Supreme Student Council Election (SSC) election is a democrafic process where studentswithin a school or university
        vote to elect their peers to key positions in the student government."
        
        jump choice1_done

label choice1_no:

        $ menu_flag = False
      
        scene hall1
        show pokwang serious:
        
            xalign 0.5
            yalign 1.0
        "Pokwang" "ok go home." 
        scene hall1
        show pokwang lazy:
        
            xalign 0.5
            yalign 1.0
        "Pokwang" "Thank You!."

        jump _return

label choice1_done:
        
    if menu_flag: 
    
        scene p1:
        
            xalign 0.7
            yalign 1.0
            "p2"    with wiperight
            pause 1.5
            "p3"     with wiperight
            pause 1.5
            "p4"     with wiperight
            pause 1.5
            "p6"     with wiperight
            pause 1
            repeat 1
    
        show pokwang animated:
        
            xalign 0.5
            yalign 1.0
            "pokwang normal"
            pause .3
     
            "pokwang talk"
            pause .3
            repeat 15
        voice "audio/n1.mp3"
            
        "Pokwang" "National Crime Prevention Council delivers training and technical assistance tailored to meet the needs of agencies
                    communities, and others engaged in crime prevention"
        voice "audio/n2.mp3"
        "Pokwang" "Crime trends and effective prevention strategies are constantly evolving 
                    and leaders must have the tools to meet new challenges."
      
            
 
    else:

        "Pokwang" "you stupid madapaker."
        scene hall1
        show logo base:
        transform topright: 
            xalign 1.0 
            yalign 0.0
   

    scene hall1
    show pokwang happy:
        xalign 0.5
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .4
        repeat 7

    voice "audio/pokwang12.mp3"
    "Pokwang" "Lets now proceed to computer laboratory." 

label flab3:
    scene flab2
    show pokwang happy:
        xalign 0.5
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .4
        repeat 7

    voice "audio/pokwang13.mp3"
    "Pokwang" "Let's begin our tour at the entrance " 
    scene flab3 
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .4
        repeat 7

    voice "audio/pokwang14.mp3"
    "Pokwang" "Sir Jherson Paguirigan, our Computer Laboratory Administrator, has played a pivotal role in ensuring that this space is optimized for both comfort and productivity." 

        

    scene lab2:
   
        "lab2"    with wiperight
        pause .5
        "lab5"    with wiperight
        pause .5
        "lab6"    with wiperight
        pause .5
        "lab7"     with wiperight
        pause .5

        repeat 1
   
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .3
        repeat 7
    voice "audio/pokwang15.mp3"
    "Pokwang" "Take a look at the workstations equipped with the latest hardware and software. "
    scene lab4  with fade
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .3
        repeat 7
    voice "audio/pokwang18.mp3"   
    "Pokwang" "Sir Jherson is committed to maintaining these computers at their peak performance, ." 
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .3
        repeat 10
    voice "audio/pokwang11.mp3"
    "Pokwang" "Whether you're into coding, graphic design, or multimedia, this space is designed to inspire and propel your learning to new heights."
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .3
        repeat 5
    voice "audio/pokwang16.mp3"
    "Pokwang" "ensuring that students have access to cutting-edge technology for their projects and assignments"
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "pokwang normal"
        pause .3
     
        "pokwang talk"
        pause .3
        repeat 10
    voice "audio/pokwang17.mp3"
    "pokwang" "If you ever need assistance, Sir Jherson and his team are readily available. They provide technical support, troubleshoot issues, and offer guidance on utilizing the resources in the lab effectively."
    label reg:

    scene registra
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 20
    voice "audio/pokwang28.mp3"
    "pokwang" "Lets now proceed to registrar"
    scene reg
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 20
    voice "audio/pokwang19.mp3"
    "pokwang" "Within the registrar's office at ACLC College, a range of transactions occur to handle student records and academic procedures. Admissions and enrollment involve the processing of new student applications, eligibility assessments, and the facilitation of course enrollments." 
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 25
    voice "audio/pokwang20.mp3"
    "pokwang" "Throughout each semester, the office oversees course registration, managing student requests for course changes, and ensuring a seamless registration process for current students. Academic records, including grade recording and transcript management, are carefully maintained, with the office addressing requests for grade adjustments and corrections." 
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 28
    voice "audio/pokwang21.mp3"
    "pokwang" "The office also manages student transfers, withdrawals, and degree audits to verify graduation requirements. Graduation ceremonies and diploma issuance are coordinated as well. Financial transactions, such as tuition payments and financial aid disbursements, fall under the registrar's responsibilities. Official document requests, like transcripts and verifications, are processed by the office."
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 15
    voice "audio/pokwang22.mp3"
    "pokwang" "Collaboration with academic advisors is crucial for providing students with guidance on course selection and academic progress. Special requests or exceptions, such as late registration or course substitutions, are handled case by case."
    show pokwang happy: 
                
        xalign 0.5
        yalign 1.0
        "pokwang talk"
        pause .3
     
        "pokwang normal"
        pause .4
        repeat 10
    voice "audio/pokwang23.mp3"
    "pokwang" "Ensuring adherence to college policies, managing academic integrity, and communication with faculty and administration are ongoing priorities. The registrar's office is also actively involved in leveraging technology, utilizing and maintaining student information systems for efficient processing."
    
   
label lib:

    scene flib
    show pokwang normal: 
        xalign 1.0
        yalign 1.0  
        "pokwang talk"  
        pause .3
     
        "pokwang normal"  
        pause .3
        repeat 12
    voice "audio/pokwang29.mp3"
    "pokwang" "Lets now proceed to library."
    scene library
    show pokwang normal: 
        xalign 1.0
        yalign 1.0  
        "pokwang talk"  
        pause .3
     
        "pokwang normal"  
        pause .3
        repeat 12
    voice "audio/pokwang24.mp3"
    "pokwang" "The ACLC College library is a central resource center for students and faculty, offering a varied collection of books and journals. It provides different study spaces, including individual carrels, group study rooms, and open reading areas, creating an environment conducive to learning. Equipped with modern technology, the library facilitates research with computer workstations, internet access, and online databases."
    voice "audio/pokwang25.mp3"
    "pokwang" "Librarians are available to assist students in navigating resources, offering guidance on research strategies, citation styles, and utilizing electronic databases. The library operates during extended hours to accommodate diverse student schedules, ensuring accessibility to its resources."
    voice "audio/pokwang26.mp3"
    "pokwang" "Beyond a repository of materials, the library may host events, workshops, and guest lectures to enhance information literacy skills and support academic endeavors. Interlibrary loan services may be available, enabling access to resources from other libraries."
    voice "audio/pokwang27.mp3"
    "pokwang" "The library's physical resources, including books and journals, cater to different learning preferences, providing quiet zones for individual study and collaborative spaces for group work. Engaging with the college community, the library may organize outreach programs, book clubs, and reading initiatives, fostering a culture of continuous learning. The ACLC College library serves as a dynamic space that actively contributes to the academic and intellectual growth of the college."
    
label admission:
    scene admission
    show pokwang animated:
        xalign 1.0
        yalign 1.0  
        "pokwang talk"  
        pause .3
     
        "pokwang normal"  
        pause .3
        repeat 12
    "pokwang" "Lets proceed to Admission office"
    scene add
    show pokwang animated:
        xalign 1.0
        yalign 1.0  
        "pokwang talk"  
        pause .3
     
        "pokwang normal"  
        pause .3
        repeat 12
    "pokwang" "The ACLC College Admission Office facilitates seamless enrollment processes for prospective students. This dynamic office manages all transactions related to admissions, ensuring efficient handling of applications, document submissions, and fee payments. Staffed by dedicated professionals, the office provides essential "
    "pokwang" "guidance to applicants, ensuring they meet requirements and deadlines. From initial inquiries to the finalization of enrollment" 
    "pokwang"  "the Admission Office plays a pivotal role in creating a smooth and accessible pathway for students to join ACLC College. Through transparent and organized transactions, the office fosters a positive experience for aspiring students as they embark on their academic journey at ACLC College."
 
    jump _return
label Boy:
  
    scene start
    voice "audio/dave1.mp3"
    D "Hi! this is pokwang before we start
            I would like to introduce the name of the 3 guy who Created of this project" 
    voice "audio/dave2.mp3"
    D "Mr Justin Montajes, Johnrey Gardoña and Roldan Montoya"
    
    voice "audio/dave3.mp3"
    D "Thank you for being patient, And lets Start now our tour"
     
    scene front 
    show d animated:
            xalign 0.5
            yalign 1.1
            "d smile" 
            pause .3
     
            "d angry"
            pause .3
            repeat 6
    voice "audio/dave4.mp3"
    D "Good day, everyone! Welcome to ACLC College of Daet. "
  
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 7
    voice "audio/dave5.mp3"
    D "My name is Dave, and I'll be your guide today as we explore the fantastic 
                facilities of our campus."

    label choice:
    default learnede = False
    scene option 
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 7
    voice "audio/dave6.mp3"
    D " Are you ready for an exciting journey?"
    
    menu:

        "Yes, I do.":
            jump choice_yes

        "Skip Computer lab":
            jump lab3
        "Skip Registrar":
            jump Registrar
        "Skip Library":
            jump Library
        "Skip Admission office":
            jump admissionn
        "No, I don't.":
            jump  choice_no
    
label computer:
    $ menu_flag = True

    scene flab3 
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "d normal"
        pause .3
     
        "talk"
        pause .4
        repeat 7

    voice "audio/pokwang14.mp3" 
    jump _flab3
    label choice_yes:

        $ menu_flag = True
        
        label background1:
        scene hall1
        play sound "crowd.mp3"
        show d animated:
            xalign 1.0
            yalign 1.0
            "talk"
            pause .2
     
            "d normal"
            pause .2
            repeat 2
        
        voice "audio/dave7.mp3"
        D "We are now in Hallway"
     
        scene hall1
        show d animated:
        
            xalign 0.5
            yalign 1.0
            "talk"
            pause .3
     
            "d normal"
            pause .3
            repeat 15
        voice "audio/dave8.mp3"
        D " Before we proceed to our first destination, I will going to show some of the photos of the activies and programs 
        that happen in this hallway "
        
        scene hall1:
            xalign 0.7
            yalign 1.0
            "h2"    with wiperight
            pause 2
     
            "h3"     with wiperight
            pause 2
    
            "h4"     with wiperight
            pause 2
       
            "h5"     with wiperight

            pause 2
            repeat 10
        play sound "creepy.mp3"
        define teleport = ImageDissolve("d normal.png", 1.0, 0)   
        show d normal:   
          
            xalign 1.1   
            yalign 1.0
       
            "talk"    with teleport 
            pause .3
     
            "d normal"  with teleport 
            pause .3
            repeat 12
        
        
        voice "audio/dave9.mp3"
        D " The first one is Halloween party. all students, are required to wear costumes, to be come the part of the celebration"
        show d normal:   
          
            xalign 1.0   
            yalign 1.0
       
            "talk"    with teleport 
            pause .3
     
            "d normal"  with teleport 
            pause .3
            repeat 11
        voice "audio/dave10.mp3"
        D " Every Strand from College to Senior High, have a candidates to participate for the best custome a ward and win the cash prizes."
        

        scene s1:
            xalign 0.9
            yalign 1.0
            "s2"    with wiperight
            pause 1.5
     
            "s3"     with wiperight
            pause 1.5
    
            "s4"     with wiperight
            pause 1.5
       
            "s5"     with wiperight
            pause 1.5
            repeat 1
        
        show d animated:
        
            xalign 0.9
            yalign 1.0
            "talk"
            pause .3
     
            "d normal"
            pause .4
            repeat 18
        
        voice "audio/dave11.mp3"
        D "And this is Supreme Student Council Election (SSC) election is a democrafic process where studentswithin a school or university
        vote to elect their peers to key positions in the student government."
        
        jump choice_done

    label choice_no:

        $ menu_flag = False
      
        scene bg hallway with fade
        show d normal:
        
            xalign 0.5
            yalign 1.0
        D "ok go home." 
        scene hall1
        show d angry:
        
            xalign 0.5
            yalign 1.0
        D "Thank You!."

        jump _return

    label choice_done:
        
    if menu_flag: 
    
        scene p1: 
        
            xalign 0.7
            yalign 1.0
            "p2"    with wiperight
            pause 1.5
            "p3"     with wiperight
            pause 1.5
            "p4"     with wiperight
            pause 1.5
            "p6"     with wiperight
            pause 1
            repeat 1
    
        show d animated:
        
            xalign 0.5
            yalign 1.0
            "d normal"
            pause .3
     
            "talk"
            pause .3
            repeat 15
        voice "audio/dave12.mp3"
            
        D "National Crime Prevention Council delivers training and technical assistance tailored to meet the needs of agencies
                    communities, and others engaged in crime prevention"
        voice "audio/dave13.mp3"
        D "Crime trends and effective prevention strategies are constantly evolving 
                    and leaders must have the tools to meet new challenges."
      
            
 
    else:

        D "you stupid madapaker."
        scene hall1
        show logo base:
        transform topright: 
            xalign 1.0 
            yalign 0.0
   

    
label lab3:

    scene flab2 
    show d happy: 
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d happy"
        pause .4
        repeat 7
    D "Lets proceed to Computer Laboratory"


    scene flab3  with fade
    show d happy: 
        xalign 0.5
        yalign 1.0
        "d smile"
        pause .3
     
        "d angry" 
        pause .4
        repeat 7

    voice "audio/dave14.mp3"
    D "Sir Jherson Paguirigan, our Computer Laboratory Administrator, has played a pivotal role in ensuring that this space is optimized for both comfort and productivity." 
    scene lab2:
   
        "lab2"    with wiperight
        pause .5
        "lab5"    with wiperight
        pause .5
        "lab6"    with wiperight
        pause .5
        "lab7"     with wiperight
        pause .5

        repeat 1
    show d happy:
        xalign 0.9
        yalign 1.0
        "d normal"
        pause .3
     
        "talk"
        pause .3
        repeat 7
    voice "audio/pokwang15.mp3"
    "Pokwang" "Take a look at the workstations equipped with the latest hardware and software. "
    scene lab4  with fade
    show d happy:
        xalign 0.9
        yalign 1.0
        "d normal"
        pause .3
     
        "talk"
        pause .3
        repeat 7
    voice "audio/pokwang18.mp3"   
    D "Sir Jherson is committed to maintaining these computers at their peak performance, ." 
    show d happy:
        xalign 0.9
        yalign 1.0
        "d normal"
        pause .3
     
        "talk"
        pause .3
        repeat 10
    voice "audio/pokwang11.mp3"
    D "Whether you're into coding, graphic design, or multimedia, this space is designed to inspire and propel your learning to new heights."
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "d normal"
        pause .3
     
        " talk"
        pause .3
        repeat 5
    voice "audio/pokwang16.mp3"
    D "ensuring that students have access to cutting-edge technology for their projects and assignments"
    show pokwang happy:
        xalign 0.9
        yalign 1.0
        "d normal"
        pause .3
     
        "talk"
        pause .3
        repeat 10
    voice "audio/pokwang17.mp3"
    D "If you ever need assistance, Sir Jherson and his team are readily available. They provide technical support, troubleshoot issues, and offer guidance on utilizing the resources in the lab effectively."
label Registrar:

    scene registra
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 20
    D "Lets proceed to Registrar office"
    scene reg
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 20
    voice "audio/dave15.mp3"
    D "Within the registrar's office at ACLC College, a range of transactions occur to handle student records and academic procedures. Admissions and enrollment involve the processing of new student applications, eligibility assessments, and the facilitation of course enrollments." 
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        " talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 25
    voice "audio/dave16.mp3"
    D "Throughout each semester, the office oversees course registration, managing student requests for course changes, and ensuring a seamless registration process for current students. Academic records, including grade recording and transcript management, are carefully maintained, with the office addressing requests for grade adjustments and corrections." 
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        " talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 28
    voice "audio/dave17.mp3"
    D "The office also manages student transfers, withdrawals, and degree audits to verify graduation requirements. Graduation ceremonies and diploma issuance are coordinated as well. Financial transactions, such as tuition payments and financial aid disbursements, fall under the registrar's responsibilities. Official document requests, like transcripts and verifications, are processed by the office."
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        " talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 15
    voice "audio/dave18.mp3"
    D "Collaboration with academic advisors is crucial for providing students with guidance on course selection and academic progress. Special requests or exceptions, such as late registration or course substitutions, are handled case by case."
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 10
    voice "audio/dave19.mp3"
    D "Ensuring adherence to college policies, managing academic integrity, and communication with faculty and administration are ongoing priorities. The registrar's office is also actively involved in leveraging technology, utilizing and maintaining student information systems for efficient processing."
    
   
label Library:
    scene flib
    show d happy: 
                
        xalign 0.5
        yalign 1.0
        "talk"
        pause .3
     
        "d normal"
        pause .4
        repeat 20
    D "Lets proceed to Library"
    scene library
    show d normal: 
        xalign 1.0
        yalign 1.0  
        "talk"  
        pause .3
     
        "d normal"  
        pause .3
        repeat 12
    voice "audio/dave20.mp3"
    D "The ACLC College library is a central resource center for students and faculty, offering a varied collection of books and journals. It provides different study spaces, including individual carrels, group study rooms, and open reading areas, creating an environment conducive to learning. Equipped with modern technology, the library facilitates research with computer workstations, internet access, and online databases."
    voice "audio/dave21.mp3"
    D "Librarians are available to assist students in navigating resources, offering guidance on research strategies, citation styles, and utilizing electronic databases. The library operates during extended hours to accommodate diverse student schedules, ensuring accessibility to its resources."
    voice "audio/dave22.mp3"
    D"Beyond a repository of materials, the library may host events, workshops, and guest lectures to enhance information literacy skills and support academic endeavors. Interlibrary loan services may be available, enabling access to resources from other libraries."
    voice "audio/dave23.mp3"
    D "The library's physical resources, including books and journals, cater to different learning preferences, providing quiet zones for individual study and collaborative spaces for group work. Engaging with the college community, the library may organize outreach programs, book clubs, and reading initiatives, fostering a culture of continuous learning. The ACLC College library serves as a dynamic space that actively contributes to the academic and intellectual growth of the college."
   
label admissionn:
    scene admission
    show d animated:
        xalign 1.0
        yalign 1.0  
        "talk"  
        pause .3
     
        "d normal"  
        pause .3
        repeat 12
    D "Lets proceed to Admission office"
    scene add
    show pokwang animated:
        xalign 1.0
        yalign 1.0  
        "talk"  
        pause .3
     
        "d normal"  
        pause .3
        repeat 12
    D "The ACLC College Admission Office facilitates seamless enrollment processes for prospective students. This dynamic office manages all transactions related to admissions, ensuring efficient handling of applications, document submissions, and fee payments. Staffed by dedicated professionals, the office provides essential "
    D "guidance to applicants, ensuring they meet requirements and deadlines. From initial inquiries to the finalization of enrollment" 
    D  "the Admission Office plays a pivotal role in creating a smooth and accessible pathway for students to join ACLC College. Through transparent and organized transactions, the office fosters a positive experience for aspiring students as they embark on their academic journey at ACLC College."
 
    jump _return
