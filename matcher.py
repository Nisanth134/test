def calculate_match_score(student_skills, internship_skills):
    if not isinstance(student_skills, list) or not isinstance(internship_skills, list):
        raise TypeError("Skills must be provided as lists.")
    
    if not internship_skills:
        return 100.0  
        
    if not student_skills:
        return 0.0    


    student_set = set(skill.strip().lower() for skill in student_skills)
    internship_set = set(skill.strip().lower() for skill in internship_skills)

    matching_skills = student_set.intersection(internship_set)
    score = (len(matching_skills) / len(internship_set)) * 100
    
    return round(score, 2)

def get_best_matches(student, internships_db):

    if not isinstance(student, dict) or not isinstance(internships_db, list):
        raise ValueError("Invalid data format for student or internships database.")
        
    if 'skills' not in student:
        raise KeyError("Student data is missing the 'skills' key.")

    results = []
    for internship in internships_db:
        if 'required_skills' not in internship:
            continue 
            
        score = calculate_match_score(student['skills'], internship['required_skills'])
        
      
        match_result = internship.copy()
        match_result['match_score'] = score
        results.append(match_result)
        
    results.sort(key=lambda x: x['match_score'], reverse=True)
    return results
