from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.http import HttpResponse
import random


#Frontend
def index(request):  
   template = loader.get_template('timetable.html') # getting our template  
   return HttpResponse(template.render())


def game(request):  
   template = loader.get_template('game.html') # getting our template  
   return HttpResponse(template.render())



# Generate Multiplication Table
def generate_table(request):
    number = int(request.GET.get('number', 0))
    table = {i: number * i for i in range(1, 13)}
    return JsonResponse(table)

# Quiz API
@csrf_exempt
def quiz(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        number = body.get('number')
        question = body.get('question')
        user_answer = body.get('user_answer')

        correct_answer = number * question
        is_correct = (user_answer == correct_answer)
        return JsonResponse({
            'correct': is_correct,
            'correct_answer': correct_answer
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Puzzle Generator
def puzzle(request):
    # Generates a puzzle: fill in the blanks
    number = int(request.GET.get('number', 0))
    missing_factor = random.randint(1, 12)
    correct_answer = number * missing_factor
    return JsonResponse({
        'puzzle': f"{number} x __ = {correct_answer}",
        'missing_factor': missing_factor
    })

# Feedback API
@csrf_exempt
def feedback(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        correct = body.get('correct', False)
        if correct:
            return JsonResponse({'feedback': 'Great job! Keep practicing to master multiplication.'})
        return JsonResponse({'feedback': 'Don\'t worry! Practice makes perfect. Try again!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Generate data for Matching Game
def get_matching_game(request):
    # Create a pool of multiplication problems
    problems = []
    for i in range(1, 13):
        for j in range(1, 13):
            problems.append({"question": f"{i} x {j}", "answer": i * j})

    # Randomly select 5 unique problems
    selected_problems = random.sample(problems, 5)

    # Shuffle the answers for the matching part
    shuffled_answers = [problem["answer"] for problem in selected_problems]
    random.shuffle(shuffled_answers)

    return JsonResponse({
        "problems": selected_problems,
        "shuffled_answers": shuffled_answers
    })


# Generate data for Timed Challenge
def get_timed_challenge(request):
    # Create a pool of multiplication problems
    problems = []
    for i in range(1, 13):
        for j in range(1, 13):
            problems.append({"question": f"{i} x {j}", "answer": i * j})

    # Randomly select 5 problems for the challenge
    selected_problems = random.sample(problems, 5)

    return JsonResponse({
        "problems": selected_problems
    })

# Generate data for Puzzle Game
def get_puzzle_game(request):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    result = num1 * num2
    return JsonResponse({"puzzle": f"{num1} x ___ = {result}", "missing_factor": num2})
