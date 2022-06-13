from this import s
from cpr.MLCodes.ApplicationAnalyst import ApplicationAnalystFunc
from cpr.MLCodes.ApplicationDeveloper import ApplicationDeveloperFunct
from cpr.MLCodes.BackendDeveloper import BackendDeveloperFunc
from cpr.MLCodes.BigData import BigDataFunc
from cpr.MLCodes.Blockchain import BlockchainFunc
from cpr.MLCodes.CloudComputing import CloudComputingFunc
from cpr.MLCodes.ComputerHardwareEngineering import computerHardwareEngineeringFunc
from cpr.MLCodes.CyberSecurity import CybersecurityFunc
from cpr.MLCodes.DataAnalysisEngineering import DataAnalysisEngineeringFunc
from cpr.MLCodes.DataScientist import DataScientistFunc
from cpr.MLCodes.DevOps import DevOpsFunc
from cpr.MLCodes.EdgeComputing import EdgeComputingFunc
from cpr.MLCodes.FrontendDevelopment import FrontendDevelopmentFunc
from cpr.MLCodes.FullStackDevelopment import FullStackDevelopmentFunc
from cpr.MLCodes.GameDesigner import GameDesignerFunc
from cpr.MLCodes.GameDeveloper import GameDeveloperFunc
from cpr.MLCodes.HyperAutomation import HyperautomationFunc
from cpr.MLCodes.ITProjectManager import ITProjectManagerFunc
from cpr.MLCodes.InformationSecurityAnalyst import InformationSecurityAnalystFunc
from cpr.MLCodes.InternetOfBehaviour import InternetOfBehaviourFunc
from cpr.MLCodes.InternetOfThings import internetOfThingsFunc
from cpr.MLCodes.PredictiveAnalyst import PredictiveAnalystFunc
from cpr.MLCodes.Snowflake import SnowflakeFunc
from cpr.MLCodes.SoftwareEngineer import SoftwareEngineerFunc
from cpr.MLCodes.UXDesigner import UserExperienceDesignerFunc
from cpr.MLCodes.VRandAR import VRandARFunc
from cpr.MLCodes.WebDesigner import WebDesignerFunc
from cpr.MLCodes.WebDeveloper import WebDeveloperFunc
from cpr.MLCodes.ArtificialIntelligence import ArtificialIntelligenceFunc


def processSkillsFunct(allSkills):
    skills = allSkills
    technologies = {"ApplicationAnalyst": 0, "ApplicationDeveloper": 0, "ArtificialIntelligence": 0,
                    "BackendDeveloper": 0, "BigData": 0, "Blockchain": 0, "CloudComputing": 0,
                    "ComputerHardwareEngineering": 0, "Cybersecurity": 0, "DataAnalysisEngineering": 0,
                    "DataScientist": 0, "DevOps": 0, "EdgeComputing": 0, "FrontendDevelopment": 0,
                    "FullStackDevelopment": 0, "GameDesigner": 0, "GameDeveloper": 0,
                    "Hyperautomation": 0, "InformationSecurityAnalyst": 0, "InternetOfBehaviour": 0,
                    "InternetOfThings": 0, "ITProjectManager": 0, "PredictiveAnalyst": 0,
                    "Snowflake": 0, "SoftwareEngineer": 0, "UXDesigner": 0, "VRandAR": 0,
                    "WebDesigner": 0, "WebDeveloper": 0}

    resultTech = {}

    for skill in allSkills:

        # Application Analyst
        if((skill.lower() == "excel") and technologies["ApplicationAnalyst"] == 0):
            result = ApplicationAnalystFunc(skills)
            resultTech["Application Analyst"] = result
            technologies["ApplicationAnalyst"] = 1

        # Application Developer
        if((skill.lower() == "kotlin" or skill.lower() == "ios" or skill.lower() == "java" or skill.lower() == "javascript" or skill.lower() == "application development" or skill.lower() == "software development") and technologies["ApplicationDeveloper"] == 0):
            result = ApplicationDeveloperFunct(skills)
            resultTech["Application Developer"] = result
            technologies["ApplicationDeveloper"] = 1

        # Artificial Intelligence
        if((skill.lower() == "artificial intelligence" or skill.lower() == "neural networks" or skill.lower() == "natural language processing (nlp)" or skill.lower() == "tensorflow") and technologies["ArtificialIntelligence"] == 0):
            result = ArtificialIntelligenceFunc(skills)
            resultTech["Artificial Intelligence"] = result
            technologies["ArtificialIntelligence"] = 1

        # Backend Developer
        if((skill.lower() == "sql" or skill.lower() == "nosql" or skill.lower() == "database") and technologies["BackendDeveloper"] == 0):
            result = BackendDeveloperFunc(skills)
            resultTech["Back-end Developer"] = result
            technologies["BackendDeveloper"] = 1

        # Big Data
        if((skill.lower() == "big data" or skill.lower() == "hivehql") and technologies["BigData"] == 0):
            result = BigDataFunc(skills)
            resultTech["BigData"] = result
            technologies["BigData"] = 1

        # Blockchain
        if((skill.lower() == "blockchain" or skill.lower() == "blockchain architecture" or skill.lower() == "cryptography") and technologies["Blockchain"] == 0):
            result = BlockchainFunc(skills)
            resultTech["Blockchain"] = result
            technologies["Blockchain"] = 1

        # Cloud Computing
        if((skill.lower() == "cloud computing" or skill.lower() == "google cloud" or skill.lower() == "azure" or skill.lower() == "aws") and technologies["CloudComputing"] == 0):
            result = CloudComputingFunc(skills)
            resultTech["Cloud Computing"] = result
            technologies["Cloud Computing"] = 1

        # Computer Hardware Engineering
        if((skill.lower() == "computer hardware knowledge" or skill.lower() == "pcb designing" or skill.lower() == "cad" or skill.lower == "circuit board design" or skill.lower() == "verilog") and technologies["ComputerHardwareEngineering"] == 0):
            result = computerHardwareEngineeringFunc(skills)
            resultTech["Computer Hardware Engineering"] = result
            technologies["ComputerHardwareEngineering"] = 1

        # Cybersecurity
        if((skill.lower() == "networking" or skill.lower() == "wireless security" or skill.lower() == "cyber security" or skill.lower() == "information security" or skill.lower() == "computer forsenic skills") and technologies["Cybersecurity"] == 0):
            result = CybersecurityFunc(skills)
            resultTech["Cybersecurity"] = result
            technologies["Cybersecurity"] = 1

        # Data Analysis Engineering
        if((skill.lower() == "scala" or skill.lower() == "analytics" or skill.lower() == "python" or skill.lower() == "r" or skill.lower() == "data visualization tools") and technologies["DataAnalysisEngineering"] == 0):
            result = DataAnalysisEngineeringFunc(skills)
            resultTech["Data Analysis Engineering"] = result
            technologies["DataAnalysisEngineering"] = 1

        # Data Scientist
        if((skill.lower() == "data science" or skill.lower() == "python") and technologies["DataScientist"] == 0):
            result = DataScientistFunc(skills)
            resultTech["Data Scientist"] = result
            technologies["DataScientist"] = 1

        # DevOps
        if((skill.lower() == "devops" or skill.lower() == "version control systems") and technologies["DevOps"] == 0):
            result = DevOpsFunc(skills)
            resultTech["DevOps"] = result
            technologies["DevOps"] = 1

        # Edge Computing
        if(skill.lower() == "ansible" and technologies["EdgeComputing"] == 0):
            result = EdgeComputingFunc(skills)
            resultTech["Edge Computing"] = result
            technologies["EdgeComputing"] = 1

        # Frontend Developer
        if((skill.lower() == "html5" or skill.lower() == "css3" or skill.lower() == "javascript" or skill.lower() == "kotlin" or skill.lower() == "bootstrap" or skill.lower() == "flutter" or skill.lower() == "react.js" or skill.lower() == "angular.js") and technologies["FrontendDevelopment"] == 0):
            result = FrontendDevelopmentFunc(skills)
            resultTech["Frontend Developer"] = result
            technologies["FrontendDevelopment"] = 1

        # Full Stack Development
        if((skill.lower() == "java" or skill.lower() == "database" or skill.lower() == "data structures and algorithms") and technologies["FullStackDevelopment"] == 0):
            result = FullStackDevelopmentFunc(skills)
            resultTech["Full Stack Developer"] = result
            technologies["FullStackDevelopment"] = 1

        # Game Designer
        if((skill.lower() == "adobe xd" or skill.lower() == "3d modelling" or skill.lower() == "graphic design") and technologies["GameDesigner"] == 0):
            result = GameDesignerFunc(skills)
            resultTech["Game Designer"] = result
            technologies["GameDesigner"] = 1

        # Game Developer
        if((skill.lower() == "c#" or skill.lower() == "unity" or skill.lower() == "maya" or skill.lower() == "quixel" or skill.lower() == "zbrush") and technologies["GameDeveloper"] == 0):
            result = GameDeveloperFunc(skills)
            resultTech["Game Developer"] = result
            technologies["GameDeveloper"] = 1

        # Hyperautomation
        if((skill.lower() == "rpa" or skill.lower() == "vb script" or skill.lower() == "c") or skill.lower() == "intelligent business process management suites (ibpms)" and technologies["Hyperautomation"] == 0):
            result = HyperautomationFunc(skills)
            resultTech["Hyperautomation"] = result
            technologies["Hyperautomation"] = 1

        # Information Security Architect
        if(skill.lower() == "cyber security" and technologies["InformationSecurityAnalyst"] == 0):
            result = InformationSecurityAnalystFunc(skills)
            resultTech["Information Security Architect"] = result
            technologies["InformationSecurityAnalyst"] = 1

        # Internet Of Behaviour
        if(skill.lower() == "customer relationship management" and technologies["InternetOfBehaviour"] == 0):
            result = InternetOfBehaviourFunc(skills)
            resultTech["Internet of Behaviour"] = result
            technologies["InternetOfBehaviour"] = 1

        # Internet Of things
        if(skill.lower() == "iot" and technologies["InternetOfThings"] == 0):
            result = internetOfThingsFunc(skills)
            resultTech["Internet of Things"] = result
            technologies["InternetOfThings"] = 1

        # IT Project Manager
        if((skill.lower() == "c++" or skill.lower() == "javascript" or skill.lower() == "project management skills") and technologies["ITProjectManager"] == 0):
            result = ITProjectManagerFunc(skills)
            resultTech["IT Project Manager"] = result
            technologies["ITProjectManager"] = 1

        # Predictive Analyst
        if(skill.lower() == "statistics" and technologies["PredictiveAnalyst"] == 0):
            result = PredictiveAnalystFunc(skills)
            resultTech["Predictive Analyst"] = result
            technologies["PredictiveAnalyst"] = 1

        # Snowflake
        if((skill.lower() == "snowsql" or skill.lower() == "snowpipe") and technologies["Snowflake"] == 0):
            result = SnowflakeFunc(skills)
            resultTech["Snowflake"] = result
            technologies["Snowflake"] = 1

        # Software Engineering
        if((skill.lower() == "software development" or skill.lower() == "data structures and algorithms") and technologies["SoftwareEngineer"] == 0):
            result = SoftwareEngineerFunc(skills)
            resultTech["Software Engineering"] = result
            technologies["SoftwareEngineer"] = 1

        # UX Designer
        if(skill.lower() == "user experience" and technologies["UXDesigner"] == 0):
            result = UserExperienceDesignerFunc(skills)
            resultTech["UX Designer"] = result
            technologies["UXDesigner"] = 1

        #VR and AR
        if((skill.lower() == "xr sdks" or skill.lower() == "ar/vr") and technologies["VRandAR"] == 0):
            result = VRandARFunc(skills)
            resultTech["Virtual Reality and Augmented Reality"] = result
            technologies["VRandAR"] = 1

        # Web Designer
        if(skill.lower() == "user interface design" and technologies["WebDesigner"] == 0):
            result = WebDesignerFunc(skills)
            resultTech["Web Designer"] = result
            technologies["WebDesigner"] = 1

        # Web Developer
        if((skill.lower() == "html5" or skill.lower() == "css3" or skill.lower() == "javascript") and technologies["WebDeveloper"] == 0):
            result = WebDeveloperFunc(skills)
            resultTech["Web Developer"] = result
            technologies["WebDeveloper"] = 1

    return resultTech
