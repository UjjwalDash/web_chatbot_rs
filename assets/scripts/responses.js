function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }
    else if(input=="tell me about robotics society"){
        return "The Robotics Society is an official technical club of VSSUT, Burla which encourages various technical activities and projects in the field of amateur as well as advanced Robotics, in the University. The members are a bunch of budding technocrats who are driven by an acute zest for learning technological advancements and happenings in the modern world, and endeavour in applying the theoretical learning into realistic projects.";
    }
    else if(input="aim of robotics society")
    {
        return "Developing new ideas in the field of Robotics and Technology to enable students to learn new technologies, assimilate appropriate skills creating innovations which solve real world problems and improve the quality of life by training them with strength of character, leadership and self-attainment."
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}