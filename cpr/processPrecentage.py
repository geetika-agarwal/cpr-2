def processPer(allSkills, dictTech, itech):

    # ApplicationAnalyst
    ApplicationAnalyst = ["data visualization tools", "data cleaning", "matlab", "r", "python", "sql", "nosql", "machine learning", "linear algebra", "calculus", "excel", "oracle",
                          "data analysis", "database", "microsoft administration", "microsoft access", "spss", "sas", "c++", "java", "uml", "sap", "html5", "css3", "javascript", "visual studio"]

    # Application Developer
    ApplicationDeveloper = ["c++", "c#", "javascript", "database", "ui/ ux design", "cyber security", "iot", "agile development", "java", "kotlin", "react.js", "swift", "angular.js", "android studio", "application development", "xml", "html5", "apis", "css3", "ios", "software development", "testing", "networking", "apple xcode ide", "spatial reasoning", "git", "c", "r", "python", "sql", "powerbi", "machine learning",
                            "data analysis", "statistics", "big data", "data wrangling", "sas", "perl", "oracle", "uml", "sap", "visual studio", "microsoft access", "excel", "nosql", "wireframing", "prototyping", "ui toolkits and frameworks", "information architecture", "graphic design", "vue.js", "github", "web development", "system development", "search engine optimization (seo)"]

    # Artificial Intelligence
    ArtificialIntelligence = ["data visualization tools", "matlab", "r", "python", "sql", "nosql", "machine learning", "linear algebra", "excel", "calculus", "artificial intelligence", "hadoop ecosystem", "java", "scala", "kafka", "apache spark", "data mining", "cloud computing", "statistics", "continuous monitoring", "continuous integration",
                              "syntactic & semantic parsing", "nltk", "neural networks", "c++", "natural language processing (nlp)", "probability", "data structures and algorithms", "tensorflow", "data modeling", "alteryx", "improvado", "powerbi", "saas", "hive hql", "descriptive analyis", "lisp", "prolog", "analytics", "data science"]

    # Back-end Developer
    BackendDeveloper = ["python", "java", "php", "sql", "git", "html5", "css3", "javascript", "ruby", "django", "go lang", "perl", "apache", "mongodb", "kubernetes", "net",
                        "database", "sas", "c#", "sql server", "sap", "couchdb", "software development life cycle (sdlc)", "data analysis", "etl", "json", "postgis", "c++", "tcl"]

    # Big Data
    BigData = ["sql", "java", "software testing", "python", "nosql", "hadoop", "pig", "apache spark", "hive hql", "data warehousing", "data mining", "etl", "big data",
               "scala", "kafka", "mysql", "javascript", "oracle", "data analysis", "perl", "data structures and algorithms", "docker", "linux", "git", "google cloud", "kubernetes"]

    # Blockchain
    Blockchain = ["blockchain", "blockchain architecture", "c++", "go lang", "c#", "javascript", "python", "ruby", "java", "cryptography", "security principles", "distributed systems", "peer to peer network security", "data structures and algorithms",
                  "networking", "user interface", "apis", "solidity", "smart contracts", "problem solving", "web development", "truffle", "user experience", "html5", "css3", "database", "analytics", "software development", "testing"]

    # Cloud Computing
    CloudComputing = ['networking', 'operating system', 'java', 'virtualization', 'database', 'google cloud', 'continuous monitoring', 'ansible', 'nosql', 'mysql', 'c#', 'flume', 'powershell', 'disaster recovery', 'powerbi', 'web services', 'php', 'tableau', 'docker', 'hive hql', 'r', 'linux', 'source code management', 'amazon redshift', 'network security', 'python', 'cloud computing',
                      'openstack', 'ruby', 'devops', 'machine learning', 'sql', 'information security', 'hadoop', 'network infrastructure', 'problem solving', 'excel', 'continuous integration', 'database architecture', 'oracle', 'azure', 'visualization', 'kubernetes', 'aws', 'sql server', 'cyber security', 'apache spark', 'deep learning', 'perl', 'relational databases', 'analytics', 'troubleshooting']

    # Computer Hardware Engineering
    ComputerHardwareEngineering = ["signal integrity", "soc", "spi", "verilog", "matlab", "circuit board design", "cadence",
                                   "cad", "firmware development", "analog design and analysis", "computer hardware knowledge", "networking", "pcb designing", "rf development"]

    # Cybersecurity
    Cybersecurity = ['linux', 'wireless security', 'cyber security', 'java', 'virtualization', 'c++', 'python', 'system design', 'vpn', 'security automation', 'network analyzers', 'php', 'risk management', 'computer forsenic skills', 'unix', 'testing', 'network switches',
                     'go lang', 'hacking', 'identity and access management', 'secure sdlc', 'information security', 'data science', 'computer protocols', 'networking', 'cloud security', 'operating system', 'network protocols', 'switching and routing', 'firewall', 'data structures and algorithms']

    # Data Analysis Engineering
    DataAnalysisEngineering = ['matlab', 'calculus', 'linear algebra', 'nosql', 'machine learning', 'apache spark', 'python', 'sql', 'analytics',
                               'etl', 'r', 'amazon redshift', 'data visualization tools', 'elk stack', 'excel', 'hadoop ecosystem', 'kafka', 'apache', 'scala']

    # Data Science
    DataScience = ['javascript', 'hdfs', 'hadoop', 'data visualization', 'java', 'hbase', 'matlab', 'azure', 'python', 'hive hql', 'sql', 'data science', 'kafka', 'nosql',
                   'r', 'flume', 'database', 'big data', 'sas', 'machine learning', 'linear algebra', 'calculus', 'pig', 'c++', 'linux', 'etl', 'apache', 'sql server', 'statistics']

    # DevOps
    DevOps = ['software development life cycle (sdlc)', 'linux', 'version control systems', 'javascript', 'php', 'operating system', 'bash', 'continuous monitoring', 'project management skills', 'visual studio',
              'analytics', 'cloud computing', 'devops', 'c++', 'ruby', 'continuous integration', 'system architecture', 'software development', 'debugging', 'java', 'python', 'problem solving', 'agile development']

    # Edge Computing
    EdgeComputing = ['cyber security', 'agile development', 'system design', 'ansible', 'aws', 'devops',
                     'networking', 'python', 'linux', 'database', 'communication protocols', 'cloud computing']

    # Frontend Developer
    FrontendDeveloper = ['swift', 'git', 'bootstrap', 'kotlin', 'flutter', 'graphic design', 'jquery', 'react.js', 'html5', 'ui toolkits and frameworks', 'java',
                         'javascript', 'testing', 'search engine optimization (seo)', 'ui/ ux design', 'ajax', 'css3', 'typescript', 'web performance optimization (wpo)', 'angular.js']

    # Full Stack Development
    FullStackDevelopment = ['php', 'visual studio', 'unix', 'oracle', 'switching and routing', 'javascript', 'version control systems', 'source code management', 'html5', 'sql server', 'computer hardware knowledge', 'cloud computing', 'data structures and algorithms', 'cryptography', 'analytics', 'uml', 'web development', 'testing', 'operating system', 'problem solving', 'css3',
                            'integrated development environment (ide)', 'c++', 'perl', 'relational databases', 'excel', 'sql', 'computer servers', 'python', 'sap', 'database architecture', 'c#', 'troubleshooting', 'security principles', 'debugging', 'networking', 'nosql', 'express.js', 'linux', 'ui toolkits and frameworks', 'database', 'disaster recovery', 'github', 'mysql', 'node.js', 'java', 'mongodb', 'operating system', 'system development']

    # Game Designer
    GameDesigner = ["c", "c++", "game development", "adobe xd", "3d modelling", "visual studio",
                    "graphic design", "artificial intelligence", "software engineering", "lead designer"]

    # Game Developer
    GameDeveloper = ['halo', 'nuke', 'maya', 'bugfixes', 'c#', 'game engine', 'linux', 'cad', 'unreal engine', 'unity',
                     'javascript', 'quixel', 'zbrush', 'c', 'java', 'python', 'c++', 'ios', 'vfx', 'adobe photoshop', 'graphic design']

    # Hyperautomation
    Hyperautomation = ['rpa', 'python', 'user experience', 'database', 'project management skills', 'analytics', 'vb script', 'web development', 'machine learning', 'c', 'process design', 'javascript',
                       'asp.net', 'intelligent business process management suites (ibpms)', 'digitalops', 'troubleshooting', 'artificial intelligence', 'data science', 'java', 'natural language processing (nlp)']

    # Information Security Architect
    InformationSecurityArchitect = [
        "python", "powershell", "devops", "cloud computing", "cyber security", "operating system"]

    # Internet of Behaviour
    InternetOfBehaviour = ['software engineering', 'sql server', 'saas', 'data warehousing', 'networking', 'windows', 'human psychology', 'cdps', 'sql',
                           'search experience optimization (sxo)', 'user experience', 'computer hardware knowledge', 'analytics', 'customer relationship management', 'troubleshooting', 'big data']

    # Internet of Things
    InternetOfThings = ['artificial intelligence', 'software testing', 'adobe xd', 'python', 'css3', 'software development', 'perl', 'information security', 'product enhancement', 'java', 'azure', 'software development life cycle (sdlc)', 'component architectures', 'customer relationship management', 'oject-oriented design', 'graphic design', 'linux', 'iot', 'service-oriented architectures',
                        'analytics', 'sensors', 'agile development', 'machine learning', 'network infrastructure', 'javascript', 'firmware development', 'ruby', 'ansible', 'mpls', 'project management skills', 'c', 'html5', 'c++', 'infrastructure security', 'figma', 'big data', 'cad', 'ui/ ux design', 'network security', 'cloud computing', 'node.js', 'aws', 'virtualization']

    # IT Project Management
    ITProjectManager = ['google cloud', 'scala', 'azure', 'c', 'sql', 'python', 'powershell', 'c++', 'node.js', 'statistics', 'oracle', '.net',
                        'nosql', 'machine learning', 'ruby', 'javascript', 'relational databases', 'c#', 'aws', 'devops', 'php', 'apis', 'deep learning', 'java']

    # Predictive Analyst
    PredictiveAnalyst = ['data analysis', 'data science', 'c', 'relational databases', 'flume', 'r', 'data visualization tools', 'perl', 'analytics', 'java', 'python', 'apache',
                         'data structures and algorithms', 'big data', 'sql', 'apache spark', 'data warehousing', 'data modeling', 'deep learning', 'machine learning', 'data mining', 'c++', 'nosql', 'hadoop', 'statistics']

    # Snowflake
    Snowflake = ["snowsql", "snowpipe", "unix", "python", "streams", "etl", "data warehousing",
                 "data modeling", "powerbi", "cross team's environment", "aws", "azure data ecosystem"]

    # Software Engineering
    SoftwareEngineering = ["python", "java", "c", "c++", "object-oriented design",
                           "software testing", "software development", "software development life cycle (sdlc)"]

    # Ux Designer
    UXDesigner = ['prototyping', 'problem solving', 'user experience', 'html5', 'ui prototyping', 'agile development', 'statistics', 'jquery',
                  'wireframing', 'css3', 'graphic design', 'java', 'typography', 'javascript', 'analytics', 'ux writing', 'sql', 'user testing', 'visual design']

    # VR and AR
    VRandAR = ['c#', 'c++', 'testing', 'ruby', 'ui toolkits and frameworks', 'nosql', 'java', '3d modelling', 'software development', 'source code management', 'xr sdks', 'c', 'php', 'javascript', 'devops', 'python', 'relational databases',
               'data structures and algorithms', 'node.js', 'debugging', 'ar/vr', 'computer vision', 'web development', 'graphic design', 'swift', 'ux design', 'operating system', 'machine learning', 'scala', 'cryptography', 'database']

    # Web Designer
    WebDesigner = ['interaction design', 'video editing', 'agile development', 'graphic design', 'css3', 'python', 'adobe photoshop', 'analytics',
                   'user interface design', 'problem solving', 'visual communication', 'c++', 'java', 'javascript', 'typography', 'wireframing', 'prototyping', 'php', 'html5']

    # Web Developer
    WebDeveloper = ['php', 'apis', 'ui/ ux design', 'ruby', 'mysql', 'relational databases', 'git', 'html5', 'software development', 'json', 'c', 'go lang', 'vue.js', 'react.js', 'flask', 'swagger', 'selenium', 'ember.js',
                    'search experience optimization (sxo)', 'nosql', 'microsoft excel', 'soap', 'postman', 'django', 'testing', 'adobe xd', 'github', 'uml', 'devops', 'agile development', 'node.js', 'figma', 'perl', 'cad', 'jquery', 'junit', 'c#', '.net', 'java', 'sql', 'css3', 'angular.js', 'cobol', 'appium', 'operating system', 'vb script', 'graphic design', 'javascript', 'python']

    skills = allSkills
    technologies = list(dictTech.keys())

    percentage = dict()

    for tech in technologies:
        if(tech == "Application Analyst"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in ApplicationAnalyst):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Application Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in ApplicationDeveloper):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Artificial Intelligence"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in ArtificialIntelligence):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Back-end Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in BackendDeveloper):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "BigData"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in BigData):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Blockchain"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in Blockchain):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Cloud Computing"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in CloudComputing):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Computer Hardware Engineering"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in ComputerHardwareEngineering):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Cybersecurity"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in Cybersecurity):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Data Analysis Engineering"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in DataAnalysisEngineering):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Data Scientist"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in DataScience):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "DevOps"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in DevOps):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Edge Computing"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in EdgeComputing):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Frontend Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in FrontendDeveloper):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Full Stack Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in FullStackDevelopment):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Game Designer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in GameDesigner):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Game Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in GameDeveloper):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Hyperautomation"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in Hyperautomation):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Information Security Architect"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in InformationSecurityArchitect):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Internet of Behaviour"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in InternetOfBehaviour):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Internet of Things"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in InternetOfThings):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "IT Project Manager"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in ITProjectManager):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Predictive Analyst"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in PredictiveAnalyst):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Snowflake"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in Snowflake):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Software Engineering"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in SoftwareEngineering):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "UX Designer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in UXDesigner):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Virtual Reality and Augmented Reality"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in VRandAR):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Web Designer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in WebDesigner):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

        if(tech == "Web Developer"):
            count = 0
            flag = 0
            percen = 0
            for skill in skills:
                if(skill.lower() in WebDeveloper):
                    count = count + 1
            if(tech in itech):
                flag = 1
            tempPer = (count / 15) * 100
            if(flag == 0):
                percen = (tempPer * 0.85)
            else:
                percen = (tempPer * 0.75) + 25
            percentage[tech] = percen

    return percentage
