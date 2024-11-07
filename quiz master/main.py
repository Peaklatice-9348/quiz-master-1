import pgzrun

WIDTH = 870
HEIGHT = 650 
TITLE = 'quiz master!'

m_box = Rect(0,0,880,80)
q_box = Rect(0,0,650,150)
s_box = Rect(0,0,150,330)
t_box = Rect(0,0,150,150)
a_box1 = Rect(0,0,300,150)
a_box2 = Rect(0,0,300,150)
a_box3 = Rect(0,0,300,150)
a_box4 = Rect(0,0,300,150)
m_box.move_ip(0,0)
q_box.move_ip(20,100)
s_box.move_ip(700,270)
t_box.move_ip(700,100)
a_box1.move_ip(20,270)
a_box2.move_ip(370,270)
a_box3.move_ip(20,450)
a_box4.move_ip(370,450)

a_boxes = [a_box1,a_box2,a_box3,a_box4]
questions = []
question_count = 0
question_index = 0
q_file_name = 'questions.txt'
def draw():
    screen.clear()
    screen.fill('black')
    screen.draw.filled_rect(m_box,'black')
    screen.draw.filled_rect(q_box,'navy blue')
    screen.draw.filled_rect(s_box,'dark green')        
    screen.draw.filled_rect(t_box,'navy blue')
    for box in a_boxes:
        screen.draw.filled_rect(box,'orange')
    
    m_message = 'welcome to quiz master!'
    screen.draw.textbox(m_message,m_box,color ='white')
    screen.draw.textbox('skip',s_box,color = 'black',angle = -90)
    screen.draw.textbox(q[0],q_box,color = 'white',shadow = (0.5,0.5),scolor = 'dim grey')


def update():
    move_message()

def move_message():
    m_box.x = m_box.x - 5
    if m_box.right < 0:
        m_box.left = WIDTH

def read_question_file():
    global question_count,questions
    q_file = open(q_file_name,'r')
    for q in q_file:
        questions.append(q)
        question_count = question_count + 1
    q_file. close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0).split(',')
read_question_file()
q = read_next_question()
pgzrun.go()