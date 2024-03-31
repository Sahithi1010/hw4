# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Since a person can be covered by more than one rule, they are not mutually exclusive. "
    answers["(b) explain"] = "While the existing rule set does not cover every circumstance, an exhaustive rule set would cover every possible combination of attribute values and provide a prediction for each."
    answers["(c) explain"] = "The result could be decided by the rule that was applied first."
    answers["(d) explain"] = "Default class make sure that every instance is classified even if it does not meet any conditions."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "yes"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Animal cant be satisfied with 3 requirements and fit into R4."
    answers["(b) example"] = "Covers all possible combinations"
    answers["(c) example"] = "each rule applies to different set, so order doesn't effect."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm uses the chain rule to propagate mistakes back through the network and iteratively compute the gradients of weights at each layer."
    answers["(b) explain"] = "The kth and k+1th layers' weights and biases related to the nodes' connections are applied, and the outcome is then run through an activation function."
    answers["(c) explain"] = "This happens when the neural network's gradient shrinks to such a small size during training that the weights are unable to update correctly, causing learning to proceed very slowly or to stop entirely."
    answers["(d) explain"] = "This is so even if the model performs flawlessly on the training set, the weights will still be adjusted depending on the error that is estimated during backpropagation, and this error will usually not be exactly 0."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "Data points are seperated by class, so k=1 or 5 will perform well."
    answers["(b) explain"] = "There is plenty of overlap between the data points, so selecting a modest K value could result in noise-induced misclassification."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.6
    answers["(a) P(A=1|-)"] = 0.2
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "As the class is positive, P(A=1) = 0.4"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.096
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = '+'
  
    # float
    answers["(c) P(A=1)"] = 0.3
    answers["(c) P(B=1)"] = 0.2
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'no'
  
    # type: float
    answers["(d) P(A=1)"] = 0.3
    answers["(d) P(B=0)"] = 0.8
    answers["(d) P(A=1,B=0)"] = 0.2

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'no'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.4
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] = None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
