# CycleCare - Architecture Documentation

## 1. Project Overview
CycleCare is a menstrual health education and awareness application. It provides basic educational content, menstrual hygiene guidance, and an estimated next-period date.

## 2. Technology Stack
- Python: Application programming
- Streamlit: User interface
- Datetime: Date calculations
- GitHub: Source code hosting

## 3. System Components

### User Interface
The Streamlit interface displays educational content and accepts the user's last period start date and usual cycle length.

### Period Estimator
Python date calculations estimate the next period start based on the entered date and cycle length.

### Educational Module
Provides general information about menstrual health, hygiene, and when to seek medical advice.

## 4. Data Flow
1. User opens the application.
2. User reads educational content.
3. User optionally enters cycle details.
4. The application calculates an estimated date.
5. The result is displayed to the user.

## 5. Privacy and Safety
- The prototype does not use a database.
- User-entered dates are not intentionally saved permanently.
- Estimates are not medical advice or contraception guidance.
- Users should consult qualified healthcare professionals for concerns.

## 6. Limitations
Cycle predictions are approximate and may not reflect individual variation. The educational content should be reviewed by healthcare professionals before wider deployment.

## 7. Future Improvements
- Support for regional languages
- Access to verified local menstrual health resources
- Improved accessibility
- Clinician-reviewed educational content
