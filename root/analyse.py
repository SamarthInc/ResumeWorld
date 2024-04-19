from analysis.scripts.keyWordScorer import *
from dataExtractor.candidate.views import *
from dataExtractor.education.views import *
from dataExtractor.experience.views import *
from dataExtractor.keyWords.views import *
from dataExtractor.jobDescription.views import *
from dataExtractor.resume.views import *
from dataExtractor.candidate.models import Candidate
from analysis.scripts.extractsections import *
from analysis.scripts.profileExtraction import *
from analysis.scripts.textCleaner import *
from analysis.scripts.scorer import *
from reportExtractor.views import *


def getResume(processId):
    return resumeData(processId)

def getJd(processId):
    return jdData(processId)

def getProfile(processId):
    return candidateData(processId)

def getEducation(processId):
    return educationData(processId)

def getExperience(processId):
    return experienceData(processId)

def getKeywords(processId):
    return keywordsData(processId)

def getReport(processId):
    return scoreData(processId)

def getReportV2(processId):
    return scoreDataV2(processId)

def getReportConfig(configId):
    return scoreConfigData(configId)

def calculateFinalscore(configId: int, keywordsScorePercentage:float, experienceScorePercentage : float, educationScorePercentage : float ):
    config = scoreConfigDataDto(configId)
    keywordsScorePercentagePerConfig = 0
    experienceScorePercentagePerConfig = 0
    educationScorePercentagePerConfig = 0  
    if keywordsScorePercentage > 0:
        keywordsScorePercentagePerConfig =  config.keywordsConfig/100 * keywordsScorePercentage
    if experienceScorePercentage > 0:    
        experienceScorePercentagePerConfig =  config.experienceConfig/100 * experienceScorePercentage
    if educationScorePercentage > 0:    
        educationScorePercentagePerConfig =  config.educationConfig/100 * educationScorePercentage
    return keywordsScorePercentagePerConfig + experienceScorePercentagePerConfig + educationScorePercentagePerConfig

def extractAndSaveData(processId: int, configId: int, resumeText : str, jdText : str):
    # extract and save profile
    try :
        profile = Candidate()
        profile.id = processId
        profile.fullName = extractNameFromResume(resumeText)
        profile.email= extractEmailFromResume(resumeText)
        profile.phoneNumber = extractContactNumberFromResume(resumeText)
        profile.linkedinUrl  = extractLinkedinUrlsFromResume(resumeText)
        profile.githubUrl = extractGithubFromResume(resumeText)
        saveCandidateData(profile)
    except :
        print("error occured while extracting profile")    

    #clean resume and save the text
    cleanResume = resumeText
    try :
        cleanResume = TextCleaner(resumeText).clean_text()
    except :
        print("error cleaning Resume")    
    
    #clean jd and save the text
    cleanJd = jdText
    try :
        cleanJd = TextCleaner(jdText).clean_text()
    except :
        print("error cleaning JD")    

    # extract, analyse and save keyWords
    keywordsScorePercentage = 0
    try :
        extractedResumeSkills = extractSkills(cleanResume)
        extractedJdSkills = extractSkills(cleanJd)
        (keywordsScorePercentage, skillsPresent, skillsAbsent) = extractSkillsScorePercentage(extractedResumeSkills, extractedJdSkills)
        saveKeywordsData(processId,'|'.join(extractedResumeSkills),'|'.join(extractedJdSkills),'|'.join(skillsPresent),'|'.join(skillsAbsent))
    except :
        print("error occured while extracting keywords")    
    print("------------------done extracting keywords---------------------")
    
    # extract, analyse and save Experience
    experienceScorePercentage = 0
    try :
        extractExperience =  extractSection(resumeText,"experience")
        saveExperienceData(processId, extractExperience)
        cleanExperienceText=TextCleaner(extractExperience).clean_text()
        experienceScore=scoreV2(cleanExperienceText,cleanJd)
        experienceScorePercentage = scoreToPercentage(experienceScore)
    except :
        print("error occured while extracting experience")
    print("------------------done extracting experience---------------------")
    
    # extract, analyse and save Education
    educationScorePercentage = 0 
    try :
        extractEducation =  extractSection(resumeText,"education")
        saveEducationData(processId, extractEducation)
        cleanEducationText=TextCleaner(extractEducation).clean_text()
        educationScore=scoreV2(cleanEducationText,cleanJd)
        educationScorePercentage = scoreToPercentage(educationScore)
    except :
        print("error occured while extracting education")
    print("------------------done extracting education---------------------")
    
    # saving the scores into database
    print(keywordsScorePercentage)
    print(experienceScorePercentage)
    print(educationScorePercentage)
    finalScorePercentage = calculateFinalscore(configId, keywordsScorePercentage , experienceScorePercentage, educationScorePercentage)
    saveScoreData(processId, configId, keywordsScorePercentage , experienceScorePercentage, educationScorePercentage, finalScorePercentage)