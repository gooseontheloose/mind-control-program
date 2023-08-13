import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox, scrolledtext
import time
import datetime
from tkcalendar import DateEntry, Calendar
import openai
import random

class ScheduleGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Schedule Generator")

        self.intake_completed = False  # Check if intake form is completed
        self.daily_check_in_completed = False
        
        self.create_form()

    def create_form(self):
        self.tab_control = ttk.Notebook(self.root)

        # Tab 1: Initial Intake Form
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Initial Intake')

        # Tab 2: Daily Check-In Form (Will be created after intake completion)
        self.tab2 = None

        # Tabs 3-8: Other tabs (Will be created after daily check-in submission)
        self.tab3 = None
        self.tab4 = None
        self.tab5 = None
        self.tab6 = None
        self.tab7 = None
        self.tab8 = None

        self.tab_control.pack(expand=1, fill="both")

        self.create_widgets()
            
    def create_widgets(self):
        self.page_index = 0  # To keep track of the current page
        self.pages = [self.create_page1_widgets, self.create_page2_widgets, self.create_page3_widgets, self.create_page4_widgets, self.create_page5_widgets, self.create_page6_widgets]

        self.create_page1_widgets()  # Start with the first page

    def clear_current_page(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()

    def next_page(self):
        if self.page_index < len(self.pages) - 1:
            self.clear_current_page()  # Clear the current page's content
            self.page_index += 1
            self.pages[self.page_index]()  # Call the corresponding create_pageX_widgets method
        else:
            self.complete_intake()  # Complete intake on the last page

    def create_page1_widgets(self):
        # Tab 1: Initial Intake Form
        introduction = (
            "Welcome to the Gateway of Transformation.\n"
            "In this realm of possibilities, we embark on a journey to unlock your true potential.\n"
            "The Mind Control Program, a catalyst of change, is here to help you sculpt a better version of yourself.\n"
            "As the stars whisper secrets to the night sky, our program will guide you towards a path of self-improvement.\n"
            "Before we begin, let us delve into your unique story and aspirations.\n"
            "Share with us your background, for through understanding, we can empower the evolution within.\n"
            "Step forward and let the metamorphosis commence."
        )

        introduction_label = tk.Label(self.tab1, text=introduction, wraplength=400, justify="center", font=("Helvetica", 12, "italic"))
        introduction_label.pack(pady=20)

        tk.Button(self.tab1, text="Let's Begin", command=self.next_page).pack()

    def create_page2_widgets(self):
        # Tab 2: Initial Intake Form
        page2_group1 = [
            "What is your full name?",
            "When is your birth date?",
            "Where are you originally from?",
            "How old are you?",
            "Are you currently in school? If yes, what level of education are you pursuing?",
            "Have you completed your education? If yes, please provide details.",
            "What is/was your major or field of study?",
            "What kind of work or jobs have you done in the past?",
            "Do you have any hobbies or interests that you're particularly passionate about?",
            "Have you lived in different places? If yes, tell me about your experiences."
        ]

        self.page2_responses = []
        for question in page2_group1:
            tk.Label(self.tab1, text=question).pack()
            response_text = tk.Text(self.tab1, height=3, width=40)
            response_text.pack()
            self.page2_responses.append(response_text)

        tk.Button(self.tab1, text="Next", command=self.next_page).pack()

    def create_page3_widgets(self):
        # Tab 3: Initial Intake Form
        page3_questions = [
            "What are the tasks you typically do on a regular basis? Please list them, separated by commas.",
            "Tell me about your job. What do you do for work?",
            "When do your work hours typically start and end?",
            "Do you have any tasks that you can do at flexible times? If so, please list them, separated by commas.",
            "On average, how many hours do you sleep each night?",
            "What are your personal goals?",
            "When is your preferred leisure time?",
            "How long of a break duration do you prefer? (in minutes)",
            "Are there any commitments you already have in your schedule? Please let me know.",
            "What motivates you and gets you excited to take action?"
        ]

        self.page3_responses = []
        for question in page3_questions:
            tk.Label(self.tab1, text=question).pack()
            response_text = tk.Text(self.tab1, height=3, width=40)
            response_text.pack()
            self.page3_responses.append(response_text)

        tk.Button(self.tab1, text="Next", command=self.next_page).pack()
    
    def create_page4_widgets(self):
        # Page 4: Second Page
        page4_conversations = [
            "What do you consider as your top three strengths? These could be talents, qualities, or skills you're proud of.",
            "As we all have areas to grow, what aspects of yourself do you think you could work on or improve?",
            "Could you describe your personality in just a few words? What traits come to mind?",
            "When you have free time, what are the activities or hobbies that truly light you up?",
            "Life is driven by motivation. What sparks that fire within you? What truly inspires you?",
            "We all have our moments of triumph. Could you share a proud achievement from your journey?",
            "Short-term goals are the stepping stones to bigger dreams. What are some goals you're aiming for in the next 3-6 months?",
            "Long-term visions shape our path. Where do you see yourself in the next 1-5 years?",
            "Time management is key to progress. How do you usually stay organized and make the most of your days?",
            "Life can be a challenge, and we face them head-on. How do you handle stress or situations that test you?",
        ]

        self.page4_responses = []
        for conversation in page4_conversations:
            tk.Label(self.tab1, text=conversation).pack()
            response_text = tk.Text(self.tab1, height=3, width=40)
            response_text.pack()
            self.page4_responses.append(response_text)

        tk.Button(self.tab1, text="Next", command=self.next_page).pack()

    def create_page5_widgets(self):
        # Page 5: Third Page
        page5_conversations = [
            "When it comes to your work-life balance, what does the perfect harmony look like for you?",
            "We all strive for positive habits. Is there something specific you're working on building or leaving behind?",
            "Learning comes in different styles. How do you best absorb information and discover new things?",
            "Picture your ideal day from morning to night. What activities and moments would make it truly perfect?",
            "Books and media shape our understanding. What genres or content do you enjoy diving into?",
            "Life presents challenges, and decisions must be made. How do you approach finding solutions and making choices?",
            "Collaboration leads to innovation. Can you share an experience where you worked alongside others to achieve a common goal?",
            "Relationships enrich our lives. What qualities or aspects do you value most in your connections with others?",
            "Inspirations come from various sources. Are there any mentors or role models who have left a lasting impact on you?",
            "Growth is a journey. What are you hoping to achieve or transform through your dedication to self-improvement?",
        ]

        self.page5_responses = []
        for conversation in page5_conversations:
            tk.Label(self.tab1, text=conversation).pack()
            response_text = tk.Text(self.tab1, height=3, width=40)
            response_text.pack()
            self.page5_responses.append(response_text)

        tk.Button(self.tab1, text="Next", command=self.next_page).pack()

    def create_page6_widgets(self):
        # Page 6: Fourth Page
        page6_conversations = [
            "Personal growth is a journey we all embark on. What's your perspective on how we can best evolve and develop?",
            "Life often brings challenges. How do you approach setbacks and the valuable lessons they offer?",
            "Creativity is a powerful outlet. Do you have a creative pursuit that fuels your imagination? What is it?",
            "Inspiration can come from unexpected places. How do you replenish your energy and seek new ideas?",
            "Dreams shape our aspirations. What steps are you taking to turn those dreams into your reality?",
            "Achievements deserve recognition. What's your preferred way to mark milestones and victories?",
            "Every day has its own fulfillment. What aspects of your current routines bring you the most joy and satisfaction?",
            "Stepping outside our comfort zone leads to growth. Can you share an experience where you embraced the unfamiliar?",
            "Success takes different forms for everyone. How do you personally define success and measure your progress?",
            "Balance is a goal for many. What does leading a balanced life mean to you and how do you achieve it?",
        ]

        self.page6_responses = []
        for conversation in page6_conversations:
            tk.Label(self.tab1, text=conversation).pack()
            response_text = tk.Text(self.tab1, height=3, width=40)
            response_text.pack()
            self.page6_responses.append(response_text)

        tk.Button(self.tab1, text="Complete Intake", command=self.complete_intake).pack()

    def complete_intake(self):
        self.clear_current_page()  # Clear the current page's content
        # Process and store intake data
        self.intake_completed = True
        self.tab_control.forget(self.tab1)  # Remove intake tab

        # Create Tab 2: Daily Check-In Form
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Daily Check-In')
        self.create_daily_check_in_form()

        self.tab_control.pack(expand=1, fill="both")

        self.create_tabs()  # Create tabs after daily form is completed
        
    def create_tabs(self):
        # Dictionary to map tab names to their respective classes
        tab_mapping = {
            'Daily Tasks': ScheduleTab,
            'Week At A Glance': WeeklyScheduleTab,
            'Master Vision': MasterVisionTab,
            'Progress': ProgressTab,
            'Goals': GoalsTab,
            'Workout': WorkoutTab,  # Include your newly created WorkoutTab here
            'Affirmations': AffirmationsTab,
            'Robot Therapist': RobotTherapistTab,
            'Settings': SettingsTab,
        }

        for tab_name in tab_mapping:
            tab_class = tab_mapping[tab_name]
            tab_frame = ttk.Frame(self.tab_control)  # Create a new frame for each tab
            self.tab_control.add(tab_frame)

            if tab_class in [ScheduleTab, WeeklyScheduleTab, WorkoutTab, AffirmationsTab]:
                # Create an instance of ScheduleTab or WeeklyScheduleTab within the respective tab
                tab_instance = tab_class(tab_frame)
                tab_instance.create_widgets()  # Call the create_widgets method of the tab instance
            else:
                placeholder_label = ttk.Label(tab_frame, text=f"{tab_name}\nComing Soon", font=("Helvetica", 16))
                placeholder_label.pack(padx=20, pady=20, fill="both", expand=True)

            setattr(self, tab_name.lower().replace(' ', '_').replace('-', '_'), tab_frame)
            self.tab_control.tab(tab_frame, state="disabled")

            # Add labels to the tab headers
            self.tab_control.tab(tab_frame, text=tab_name)
        
    def create_daily_check_in_form(self):
        tk.Label(self.tab2, text="Daily Check-In", font=("Helvetica", 20, "bold")).pack()

        # Create a main frame to hold the left and right sections
        main_frame = tk.Frame(self.tab2)
        main_frame.pack()

        # Left section (text inputs and labels)
        left_frame = tk.Frame(main_frame)
        
        text_input_labels = [
            "Tell me about your day before today:",
            "Were there any tasks you didn't manage to complete?",
            "Share your thoughts, notes, and reflections:",
            "How did today contribute to your short-term and long-term goals?",
            "What goals did you achieve today?",
            "What are your plans for tomorrow?",
            "Do you have any feedback for adapting your routine?"
            "What were the highlights and low points of your day?",

        ]

        text_input_widgets = [
            tk.Text(left_frame, height=3, width=60) for _ in range(len(text_input_labels))
        ]

        for label, widget in zip(text_input_labels, text_input_widgets):
            tk.Label(left_frame, text=label).pack()
            widget.pack()

        left_frame.pack(side="left", padx=20)

        # Center section (reflection questions)
        center_frame = tk.Frame(main_frame)
        
        reflection_questions = [
            "What are some small wins or positive moments from today that made you smile?",
            "Describe a challenge you faced today and how you navigated through it.",
            "Recall a moment when you were fully present and mindful today. What was happening around you?",
            "How did you prioritize your well-being today? Did you engage in any self-care activities?",
            "Who did you interact with today, and how did those interactions make you feel?",
            "Did you engage in any creative activities today, or did you have an idea that sparked your imagination?",
            "Reflect on how you managed your time today. Were there any time-wasting habits you noticed?"
        ]

        reflection_responses = []

        for question in reflection_questions:
            response_label = tk.Label(center_frame, text=question)
            response_label.pack(anchor="w")
            response_text = tk.Text(center_frame, height=3, width=60)
            response_text.pack(anchor="w")
            reflection_responses.append(response_text)

        center_frame.pack(side="left", padx=20)

        # Right section (mood slider and checkboxes)
        right_frame = tk.Frame(main_frame)
        
        tk.Label(right_frame, text="Mood Rating (1-10):").pack()
        self.mood_rating = tk.Scale(right_frame, from_=1, to=10, orient="horizontal")
        self.mood_rating.pack()

        checkbox_questions = [
            "Did you exercise today?",
            "Did you meditate or practice mindfulness today?",
            "Did you read or learn something new today?",
            "Did you eat healthy meals today?",
            "Did you achieve your main goal for the day?",
            "Did you perform any random acts of kindness?",
            "Did you engage in creative activities?",
            "Did you feel connected with others?",
            "Did you prioritize self-care today?"
        ]

        checkbox_widgets = []

        for question in checkbox_questions:
            checkbox = tk.Checkbutton(right_frame, text=question)
            checkbox.pack(anchor="w")
            checkbox_widgets.append(checkbox)

        right_frame.pack(side="right", padx=20)

        # Button to submit daily check-in
        submit_button = tk.Button(self.tab2, text="Submit Daily Check-In", command=self.submit_daily_check_in)
        submit_button.pack(pady=20)

    def submit_daily_check_in(self):
        # Process and store daily check-in data
        self.daily_check_in_completed = True  # Mark daily check-in as completed
        self.show_daily_tasks_tab()  # Show the "Daily Tasks" tab
        self.lock_check_in_tab()  # Lock the daily check-in tab until the next day
        self.enable_other_tabs()  # Enable other tabs
        # Placeholder message for demonstration
        messagebox.showinfo("Daily Check-In Submitted", "Thanks for submitting! Come back tomorrow for your tasks.")

    def enable_other_tabs(self):
        # Enable the tabs created in the create_tabs() method
        for tab_name in ['Daily Tasks', 'Week At A Glance', 'Master Vision', 'Progress', 'Goals', 'Workout', 'Affirmations', 'Robot Therapist', 'Settings']:
            tab_frame = getattr(self, tab_name.lower().replace(' ', '_'))
            self.tab_control.tab(tab_frame, state="normal")
            
    def show_daily_tasks_tab(self):
        self.tab_control.tab(self.daily_tasks, state="normal")  # Updated attribute name

    def lock_check_in_tab(self):
        # Calculate the time until the next day's midnight
        current_time = datetime.datetime.now()
        next_midnight = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        time_until_midnight = (next_midnight - current_time).seconds

        # Lock the daily check-in tab and schedule its unlocking for the next day
        self.tab_control.tab(self.tab2, state="disabled")
        self.root.after(time_until_midnight * 1000, self.unlock_check_in_tab)  # Schedule the unlock

    def unlock_check_in_tab(self):
        self.tab_control.tab(self.tab2, state="normal")  # Unlock the daily check-in tab

    def start(self):
        self.root.mainloop()

class ScheduleTab:
    def __init__(self, parent_frame):
        self.frame = parent_frame

    def create_widgets(self):
        title_label = ttk.Label(self.frame, text="Daily Tasks", font=("Helvetica", 20, "bold"))
        title_label.pack(side="top", pady=20)

        # Placeholder for daily inspirational message
        tk.Label(self.frame, text="Your daily inspirational message:").pack()
        self.daily_inspiration_label = ttk.Label(self.frame, text="Placeholder for personalized daily message")
        self.daily_inspiration_label.pack()

        # Display a famous quote related to the master vision
        tk.Label(self.frame, text="Famous Quote Related to Master Vision:").pack()
        self.famous_quote_label = ttk.Label(self.frame, text="Placeholder for famous quote")
        self.famous_quote_label.pack()

        # Table to display conversation with ChatGPT
        self.conversation_table = tk.Text(self.frame, height=10, width=60)
        self.conversation_table.pack()

        # Placeholder button to simulate interaction with ChatGPT
        tk.Button(self.frame, text="Get ChatGPT Response", command=self.get_chat_gpt_response).pack()

    def get_chat_gpt_response(self):
        # Placeholder: Simulate getting response from ChatGPT
        user_input = "User: " + self.daily_inspiration_entry.get()
        chat_gpt_response = "ChatGPT: Placeholder response from ChatGPT"

        # Update conversation table with user input and ChatGPT response
        current_conversation = self.conversation_table.get("1.0", "end-1c")
        new_conversation = current_conversation + "\n" + user_input + "\n" + chat_gpt_response + "\n"
        self.conversation_table.delete("1.0", tk.END)
        self.conversation_table.insert("1.0", new_conversation)

class WeeklyScheduleTab:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.task_entries = []
        self.task_treeviews = {}
        self.chatgpt_tasks = {}  # Store ChatGPT-generated tasks for each day

    def create_widgets(self):
        title_label = ttk.Label(self.frame, text="Week at a Glance", font=("Helvetica", 20, "bold"))
        title_label.pack(side="top", pady=20)

        # Button to get tasks from ChatGPT
        button_frame = ttk.Frame(self.frame)
        button_frame.pack()

        get_week_button = tk.Button(button_frame, text="Get Week", command=self.get_week_tasks)
        get_week_button.grid(row=0, column=0, padx=10, pady=10)

        refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_tasks)
        refresh_button.grid(row=0, column=1, padx=10, pady=10)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_tasks)
        clear_button.grid(row=0, column=2, padx=10, pady=10)

        view_previous_button = tk.Button(button_frame, text="View Previous Weeks", command=self.view_previous_weeks)
        view_previous_button.grid(row=0, column=3, padx=10, pady=10)


        # Create a Calendar widget for the weekly view
        self.calendar = Calendar(self.frame, selectmode="day", date_pattern="yyyy-mm-dd", showweeknumbers=False)
        self.calendar.pack(padx=10, pady=10)

        # Create a frame for task entries and task treeviews
        tasks_frame = ttk.Frame(self.frame)
        tasks_frame.pack()

        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        for day_index, day_name in enumerate(days_of_week):
            day_label = ttk.Label(tasks_frame, text=day_name, font=("Helvetica", 12, "bold"))
            day_label.grid(row=0, column=day_index * 2, padx=10, pady=5, columnspan=2)

            task_entry = tk.Entry(tasks_frame, width=30)
            task_entry.grid(row=1, column=day_index * 2, padx=10, pady=5, columnspan=2)

            add_button = tk.Button(tasks_frame, text="Add", command=lambda entry=task_entry, day=day_name: self.add_task(entry, day))
            add_button.grid(row=2, column=day_index * 2, padx=5, pady=5, columnspan=2)

            self.task_entries.append(task_entry)

            # Create a treeview for displaying added tasks
            task_treeview = ttk.Treeview(tasks_frame, columns=("Task"), show="headings", height=5)
            task_treeview.heading("Task", text="Tasks for " + day_name)
            task_treeview.grid(row=3, column=day_index * 2, padx=10, pady=5, columnspan=2)
            self.task_treeviews[day_name] = task_treeview

            expand_button = tk.Button(tasks_frame, text="Expand", command=lambda day=day_name: self.expand_tasks(day))
            expand_button.grid(row=4, column=day_index * 2, padx=(5, 2), pady=5)

            delete_button = tk.Button(tasks_frame, text="Delete", command=lambda day=day_name: self.delete_tasks(day))
            delete_button.grid(row=4, column=day_index * 2 + 1, padx=(2, 5), pady=5)

    def add_task(self, task_entry, day_name):
        task_text = task_entry.get()
        if task_text:
            selected_day = self.calendar.get_date()
            day = datetime.datetime.strptime(selected_day, "%Y-%m-%d").strftime("%A")
            self.task_treeviews[day_name].insert("", "end", values=(task_text,))
            task_entry.delete(0, tk.END)
            print(f"Adding task '{task_text}' to {day_name}")

    def expand_tasks(self, day_name):
        expanded_window = tk.Toplevel(self.frame)
        expanded_window.title(f"Expanded Tasks for {day_name}")

        expanded_treeview = ttk.Treeview(expanded_window, columns=("Task"), show="headings", height=10)
        expanded_treeview.heading("Task", text="Tasks for " + day_name)
        expanded_treeview.pack(padx=10, pady=10)

        tasks = self.task_treeviews[day_name].get_children()
        for task in tasks:
            values = self.task_treeviews[day_name].item(task, "values")
            expanded_treeview.insert("", "end", values=values)

    def delete_tasks(self, day_name):
        selected_items = self.task_treeviews[day_name].selection()
        for item in selected_items:
            self.task_treeviews[day_name].delete(item)
            print(f"Deleting task from {day_name}")

    def get_week_tasks(self):
        # Placeholder: Get tasks from ChatGPT for the entire week
        # You would need to implement the logic to retrieve tasks from ChatGPT
        # and update the self.chatgpt_tasks dictionary accordingly.
        pass

    def refresh_tasks(self):
        # Refresh the display to show the latest tasks
        self.update_treeviews()

    def clear_tasks(self):
        # Clear the tasks from all treeviews
        for day_name in self.task_treeviews:
            self.task_treeviews[day_name].delete(*self.task_treeviews[day_name].get_children())
        self.chatgpt_tasks.clear()

    def view_previous_weeks(self):
        # Placeholder: Implement logic to view tasks from previous weeks
        pass

    def update_treeviews(self):
        # Update the treeviews with the stored tasks
        for day_name in self.task_treeviews:
            self.task_treeviews[day_name].delete(*self.task_treeviews[day_name].get_children())
            tasks = self.chatgpt_tasks.get(day_name, [])
            for task in tasks:
                self.task_treeviews[day_name].insert("", "end", values=(task,))
    
class MasterVisionTab:
    pass


class ProgressTab:
    pass

class GoalsTab:
    pass

class WorkoutTab:
    def __init__(self, parent):
        self.parent = parent

        # Intensity level names for the slider
        self.intensity_levels = {
            1: "Recovery",
            2: "Beginner",
            3: "Light",
            4: "Moderate",
            5: "Intermediate",
            6: "Challenging",
            7: "Advanced",
            8: "Hardcore",
            9: "Extreme",
            10: "Maximum"
        }

    def create_widgets(self):
        self.frame = ttk.Frame(self.parent)
        self.frame.pack(fill="both", expand=True)

        # Create a frame for the form on the left
        form_frame = tk.Frame(self.frame)
        form_frame.pack(side="left", padx=20, pady=20)

        # Create a frame for the output on the right
        output_frame = tk.Frame(self.frame)
        output_frame.pack(side="right", padx=20, pady=20)

        # Column 1 - Height, Current Weight, Desired Weight, Intensity Slider
        column1_frame = tk.Frame(form_frame)
        column1_frame.grid(row=0, column=0, padx=10)
        tk.Label(column1_frame, text="Personal Details").pack()

        tk.Label(column1_frame, text="Height:").pack(anchor="w")
        self.height_entry = ttk.Entry(column1_frame)
        self.height_entry.pack(anchor="w")

        tk.Label(column1_frame, text="Current Weight:").pack(anchor="w")
        self.current_weight_entry = ttk.Entry(column1_frame)
        self.current_weight_entry.pack(anchor="w")

        tk.Label(column1_frame, text="Desired Weight:").pack(anchor="w")
        self.desired_weight_entry = ttk.Entry(column1_frame)
        self.desired_weight_entry.pack(anchor="w")

        tk.Label(column1_frame, text="Workout Intensity:").pack(anchor="w")
        self.intensity_scale = ttk.Scale(column1_frame, from_=1, to=10, orient="horizontal", command=self.update_intensity_label)
        self.intensity_scale.set(5)  # Set default value to 5 (Intermediate)
        self.intensity_scale.pack(anchor="w")

        self.intensity_scale_label = tk.Label(column1_frame, text="")
        self.intensity_scale_label.pack(anchor="w")

        self.gym_membership_var = tk.IntVar(value=0)
        gym_membership_checkbox = tk.Checkbutton(column1_frame, text="I have a gym membership", variable=self.gym_membership_var)
        gym_membership_checkbox.pack(anchor="w")

        # Column 2 - Indoor, Outdoor, Main Focus Areas, Select All
        column2_frame = tk.Frame(form_frame)
        column2_frame.grid(row=0, column=1, padx=10)
        tk.Label(column2_frame, text="Workout Location").pack()

        self.indoor_var = tk.IntVar(value=0)
        indoor_checkbox = tk.Checkbutton(column2_frame, text="Indoor", variable=self.indoor_var)
        indoor_checkbox.pack(anchor="w")

        self.outdoor_var = tk.IntVar(value=0)
        outdoor_checkbox = tk.Checkbutton(column2_frame, text="Outdoor", variable=self.outdoor_var)
        outdoor_checkbox.pack(anchor="w")

        tk.Label(column2_frame, text="Focus Areas").pack()

        self.focus_vars = {}
        self.focus_checkboxes = []
        focus_areas = ["Strength", "Cardio", "Flexibility", "Endurance"]
        for area in focus_areas:
            var = tk.IntVar(value=0)
            checkbox = tk.Checkbutton(column2_frame, text=area, variable=var)
            checkbox.pack(anchor="w")
            self.focus_vars[area] = var
            self.focus_checkboxes.append(checkbox)

        select_all_focus_button = ttk.Button(column2_frame, text="Select All", command=lambda: self.toggle_select_all(self.focus_vars))
        select_all_focus_button.pack(anchor="w")

        # Column 3 - Desired Body Parts, Select All
        column3_frame = tk.Frame(form_frame)
        column3_frame.grid(row=0, column=2, padx=10)
        tk.Label(column3_frame, text="Desired Body Parts").pack()

        self.body_parts_vars = {}
        self.body_parts_checkboxes = []
        body_parts = ["Arms", "Legs", "Abs", "Back", "Chest", "Shoulders", "Knees"]
        for part in body_parts:
            var = tk.IntVar(value=0)
            checkbox = tk.Checkbutton(column3_frame, text=part, variable=var)
            checkbox.pack(anchor="w")
            self.body_parts_vars[part] = var
            self.body_parts_checkboxes.append(checkbox)

        select_all_parts_button = ttk.Button(column3_frame, text="Select All", command=lambda: self.toggle_select_all(self.body_parts_vars))
        select_all_parts_button.pack(anchor="w")

        # Column 4 - Select Days of the Week, Select All
        column4_frame = tk.Frame(form_frame)
        column4_frame.grid(row=0, column=3, padx=10)
        tk.Label(column4_frame, text="Days of the Week").pack()

        self.day_vars = {}
        self.day_checkboxes = []
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            var = tk.IntVar(value=0)
            checkbox = tk.Checkbutton(column4_frame, text=day, variable=var)
            checkbox.pack(anchor="w")
            self.day_vars[day] = var
            self.day_checkboxes.append(checkbox)

        select_all_days_button = ttk.Button(column4_frame, text="Select All", command=lambda: self.toggle_select_all(self.day_vars))
        select_all_days_button.pack(anchor="w")

        # Submit button
        submit_button = ttk.Button(form_frame, text="Submit", command=self.submit_workout_form)
        submit_button.grid(row=1, columnspan=4, pady=10)
        
        # Text widget to display workout routine
        self.workout_output = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=40, height=15, state="disabled")
        self.workout_output.pack(fill="both", expand=True)

        # Save button
        self.save_button = tk.Button(output_frame, text="Save Routine", command=self.save_workout_routine, state="disabled")
        self.save_button.pack(pady=5)

        # Export to PDF button
        self.export_pdf_button = tk.Button(output_frame, text="Export to PDF", command=self.export_to_pdf, state="disabled")
        self.export_pdf_button.pack(pady=5)

        # Export to TXT button
        self.export_txt_button = tk.Button(output_frame, text="Export to TXT", command=self.export_to_txt, state="disabled")
        self.export_txt_button.pack(pady=5)

    def submit_workout_form(self):
        # Gather input values from the form
        height = self.height_entry.get()
        current_weight = self.current_weight_entry.get()
        desired_weight = self.desired_weight_entry.get()
        workout_intensity = self.intensity_scale.get()  # Use intensity_scale directly
        focus_areas = [area for area, var in self.focus_vars.items() if var.get() == 1]
        desired_body_parts = [part for part, var in self.body_parts_vars.items() if var.get() == 1]
        selected_days = [day for day, var in self.day_vars.items() if var.get() == 1]

        # Structure the input data for generating the workout routine
        workout_data = {
            "height": height,
            "current_weight": current_weight,
            "desired_weight": desired_weight,
            "workout_intensity": workout_intensity,
            "desired_body_parts": desired_body_parts,
            "selected_days": selected_days
        }

        # Generate workout routine using ChatGPT (placeholder)
        workout_routine = self.generate_workout_routine(workout_data)

        # Display the workout routine
        self.workout_output.config(state="normal")
        self.workout_output.delete(1.0, tk.END)
        self.workout_output.insert(tk.END, workout_routine)
        self.workout_output.config(state="disabled")

        # Enable the save and export buttons
        self.save_button.config(state="normal")
        self.export_pdf_button.config(state="normal")
        self.export_txt_button.config(state="normal")

    def update_intensity_label(self, value):
        intensity_level = self.intensity_levels[int(float(value))]
        self.intensity_scale_label.config(text=intensity_level)
        
    def generate_workout_routine(self, workout_data):
        # Placeholder: Generate workout routine based on input data
        routine = "Here's your 7-day workout routine:\n"
        routine += f"Day 1: Upper Body\n"
        routine += f"Day 2: Lower Body\n"
        routine += f"Day 3: Cardio\n"
        routine += f"Day 4: Rest\n"
        routine += f"Day 5: Core\n"
        routine += f"Day 6: Full Body\n"
        routine += f"Day 7: Rest\n"
        routine += "Placeholder routine\n"
        return routine

    def toggle_select_all(self, var_dict):
        all_selected = all(var.get() == 1 for var in var_dict.values())
        for var in var_dict.values():
            var.set(not all_selected)

    def save_workout_routine(self):
        # Placeholder: Save workout routine to a file
        pass

    def export_to_pdf(self):
        # Placeholder: Export workout routine to PDF
        pass

    def export_to_txt(self):
        # Placeholder: Export workout routine to TXT
        pass

class AffirmationsTab:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.affirmations = []  # Store received affirmations
        self.current_affirmation_index = -1  # Index of the currently displayed affirmation


    def create_widgets(self):
        # Create UI elements for affirmations tab
        title_label = ttk.Label(self.frame, text="Affirmations", font=("Helvetica", 20, "bold"))
        title_label.pack(side="top", pady=20)

        # Button to get affirmation from ChatGPT
        get_affirmation_button = tk.Button(self.frame, text="Get Affirmation", command=self.get_affirmation)
        get_affirmation_button.pack()

        # Display area for received affirmations
        self.affirmations_display = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=40, height=10)
        self.affirmations_display.pack(fill="both", expand=True)

        # Save, Clear, Refresh, and View Previous buttons
        save_button = tk.Button(self.frame, text="Save", command=self.save_affirmation)
        clear_button = tk.Button(self.frame, text="Clear", command=self.clear_affirmations)
        refresh_button = tk.Button(self.frame, text="Refresh", command=self.refresh_affirmations)
        view_previous_button = tk.Button(self.frame, text="View Previous", command=self.view_previous_affirmations)

        save_button.pack(side="left", padx=10, pady=10)
        clear_button.pack(side="left", padx=10, pady=10)
        refresh_button.pack(side="left", padx=10, pady=10)
        view_previous_button.pack(side="left", padx=10, pady=10)

    def get_affirmation(self):
        # Placeholder: Get affirmation from ChatGPT
        affirmation = "You are capable of achieving great things. Believe in yourself!"
        self.affirmations.append(affirmation)
        self.update_affirmations_display()

    def update_affirmations_display(self):
        # Update the text display with the received affirmations
        self.affirmations_display.config(state="normal")
        self.affirmations_display.delete(1.0, tk.END)
        for idx, affirmation in enumerate(self.affirmations, start=1):
            self.affirmations_display.insert(tk.END, f"{idx}. {affirmation}\n")
        self.affirmations_display.config(state="disabled")

    def save_affirmation(self):
        # Placeholder: Save the current affirmation to a file
        pass

    def clear_affirmations(self):
        # Clear the received affirmations
        self.affirmations = []
        self.update_affirmations_display()

    def refresh_affirmations(self):
        # Refresh the display to show the latest affirmations
        self.update_affirmations_display()

    def view_previous_affirmations(self):
        if not self.affirmations:
            return

        previous_window = tk.Toplevel(self.frame)
        previous_window.title("Previous Affirmations")

        affirmation_label = ttk.Label(previous_window, text="", font=("Helvetica", 12))
        affirmation_label.pack(padx=20, pady=10)

        def show_affirmation(index):
            if 0 <= index < len(self.affirmations):
                affirmation_label.config(text=self.affirmations[index])
                self.current_affirmation_index = index

        def show_next_affirmation():
            show_affirmation(self.current_affirmation_index + 1)

        def show_previous_affirmation():
            show_affirmation(self.current_affirmation_index - 1)

        previous_button = tk.Button(previous_window, text="Previous", command=show_previous_affirmation)
        next_button = tk.Button(previous_window, text="Next", command=show_next_affirmation)

        previous_button.pack(side="left", padx=10, pady=10)
        next_button.pack(side="right", padx=10, pady=10)

        show_affirmation(0)  # Display the first affirmation initially

class RobotTherapistTab:
    pass

class SettingsTab:
    pass

def main():
    root = tk.Tk()
    app = ScheduleGeneratorApp(root)
    app.start()

if __name__ == "__main__":
    main()
