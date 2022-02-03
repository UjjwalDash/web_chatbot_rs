import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import warnings
#kuchu voice

#tocknisition
#text=collect_data(url)
text='''The Robotics Club is an official technical club of VSSUT, Burla which encourages various technical activities
and projects in the field of amateur as well as advanced Robotics, in the University. The members are a bunch of
budding technocrats who are driven by an acute zest for learning technological advancements and
happenings in the modern world, and endeavour in applying the theoretical learning into realistic projects.
Aim :
Developing new ideas in the field of Robotics and Technology to enable students to learn new technologies, assimilate appropriate skills creating innovations which solve real world problems and improve the quality of life by training them with strength of character, leadership and self-attainment.

Mission :
The Society was created with the purpose of developing interest in the field of Robotics and STEM Education among the student community.
It would foster innovations solving Real world Problems and Challenges.
Encourage interaction between robotics researches in India (academic/R & D Labs/Industry)
Provide Workspace, Tools to the interested students for development of their projects and helping them to participate in various national and international Robotics competitions as well as.
Our UAV is a hexacopter and it has payload of 4kg along with flight time of 30min. The hexacopter can 
be waypoint navigated to provide fast relief at an urgent location. It uses GPS to keep a track of 
location and also navigates to the required location using the gps.
A drone is a flying robot that can be remotely controlled or fly 
autonomously through software-controlled flight plans in their 
embedded systems, working in conjunction with onboard sensors 
and GPS.
UAV stands for unmanned aerial vehicle. UAV is an aircraft 
without a human pilot on board and a type of unmanned vehicle. 
The sole moto for designing ROUV project is for surveillance of condition of Hirakud Dam and 
detection of the cracks. Due to high underwater pressure and turbulent flow of water, it has been 
proved really difficult and risky for the divers to investigate the current condition of the Dam.
ROUV stands for Remotely Operated Underwater Vehicle.
An ROUV can be deployed in underwater locations to gather remains and collect data. In 
situations where divers are needed, ROUVs can inspect critical areas, while the diver determines 
the safest possible route. ROUVs are robust and rugged in design, built to withstand harsh water
environments, and require minimal maintenance.
'''
#greeting input

gret_input=['hi','hellow','hola','greetings','wassup','hey']

#greeting response

gret_response=['howdy','hi','hey',"what's good",'hello','hey there']

#function to return a random greeting

sent_tokens=nltk.sent_tokenize(text)
#print(text)
#speak(text)
#create dictonary
remove_punc_dict=dict((punct,None) for punct in string.punctuation)
#print(remove_punc_dict)

#Create a function to return a list of lowercase words after remove punctuation
def remove_punc(text):
    return nltk.word_tokenize(text.lower().translate(remove_punc_dict))
remove_punc(text)
    
def user_in(qus):        
    #print(sent_tokens)
    #user
    user_response=qus
    user_response.lower()
    return user_response
def ai_ans(user_response):
    for word in user_response.split():
        if word in gret_input:
            return random.choice(gret_response)
    if "features of uav" in user_response:
        answer='''Features of UAV : 
        <br> Payload of 4 kg for Medical/ Relief supplies,
        <br> GPS Stabilization<br> Altitude and GPS hold
        <br> Real time mission planning and Waypoint navigation
        <br> Flight time of minimum 30 minutes
        <br> Low cost in comparison with commercially available drones with same specifications
        <br> People counting in disaster affected area.'''
        return answer
    elif "features of rouv" in user_response:
        answer='''Features of ROUV : <br>• Long range 3D environment
<br>• SONAR mapping
<br>• Way point navigation
<br>• Depth sensing and mapping
<br>• Advance Image Processing
<br>• Identification of biodiversity
<br>• hotspots
<br>• Dam crack detection
<br>• Position hold under 30m/s
<br>• turbulent flow
<br>• Neutrally buoyant in water
<br>• Run time of 3 hours
<br>• Automated mission planning
<br>• Live Video streaming
<br>• Oil leak detection'''
        return answer
    else:
        #kuchu response
        kuchu_response=''

        #append the user response to token list
        sent_tokens.append(user_response)
        #create Tfidf Vectorizer
        tf=TfidfVectorizer()

        #convert a text to matrix
        tfidf=tf.fit_transform(sent_tokens)

        #get the measure of similarity score
        vals=cosine_similarity(tfidf[-1],tfidf)

        #get the index
        idx=vals.argsort()[0][-2]

        #reduce the dictonar values
        flat=vals.flatten()

        #sort the list in asending order
        flat.sort()

        #get the most similar score
        score=flat[-2]

        #
        if score==0:
            kuchu_response=kuchu_response+'I cannot Understand'
        else:
            kuchu_response=kuchu_response+sent_tokens[idx]
        #print kuchu response
        kr=kuchu_response
        
        sent_tokens.remove(user_response)
        #speak(kuchu_response)
        
        return kr


    
