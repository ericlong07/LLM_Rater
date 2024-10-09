from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample categories and questions
categories = [
    {
        "category": "Science",
        "questions": [
            {"value": 100, "question": "What is the chemical symbol for water?", "answer": "H2O", "asked": False},
            {"value": 200, "question": "What planet is known as the Red Planet?", "answer": "Mars", "asked": False},
            {"value": 300, "question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide", "asked": False},
            {"value": 400, "question": "What is the speed of light?", "answer": "299,792 km/s", "asked": False},
            {"value": 500, "question": "What element has the chemical symbol Fe?", "answer": "Iron", "asked": False}
        ]
    },
    {
        "category": "History",
        "questions": [
            {"value": 100, "question": "Who was the first president of the United States?", "answer": "George Washington", "asked": False},
            {"value": 200, "question": "In what year did the Titanic sink?", "answer": "1912", "asked": False},
            {"value": 300, "question": "Which war was fought between the North and South regions in the US?", "answer": "The Civil War", "asked": False},
            {"value": 400, "question": "Who wrote the Declaration of Independence?", "answer": "Thomas Jefferson", "asked": False},
            {"value": 500, "question": "In which year did World War II end?", "answer": "1945", "asked": False}
        ]
    },
    {
        "category": "Math",
        "questions": [
            {"value": 100, "question": "What is the value of pi (π) to two decimal places?", "answer": "3.14", "asked": False},
            {"value": 200, "question": "What is 5 factorial (5!)?", "answer": "120", "asked": False},
            {"value": 300, "question": "What is the square root of 144?", "answer": "12", "asked": False},
            {"value": 400, "question": "What is the derivative of x^2?", "answer": "2x", "asked": False},
            {"value": 500, "question": "What is the sum of the first 100 natural numbers?", "answer": "5050", "asked": False}
        ]
    }
]

# Home route to display the Jeopardy board
@app.route('/')
def home():
    return render_template('index.html', categories=categories)

# Route to display a specific question
@app.route('/question/<int:cat_id>/<int:q_id>')
def show_question(cat_id, q_id):
    category = categories[cat_id]
    question = category['questions'][q_id]
    return render_template('question.html', category=category['category'], question=question['question'], value=question['value'], cat_id=cat_id, q_id=q_id)

# Route to handle the answer check
@app.route('/answer', methods=['POST'])
def check_answer():
    cat_id = int(request.form['cat_id'])
    q_id = int(request.form['q_id'])
    user_answer = request.form['answer']
    correct_answer = categories[cat_id]['questions'][q_id]['answer']
    
    # Mark the question as asked
    categories[cat_id]['questions'][q_id]['asked'] = True
    
    if user_answer.lower() == correct_answer.lower():
        return redirect(url_for('home', result="correct"))
    else:
        return redirect(url_for('home', result="wrong"))

if __name__ == '__main__':
    app.run(debug=True)
