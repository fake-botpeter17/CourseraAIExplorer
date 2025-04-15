# 🎓 Coursera AI Explorer (Terminal AI Assistant)

An AI-powered CLI tool that uses **Gemini API** to fetch Coursera course data, save it locally in **JSON** and **SQLite**, and allows **custom terminal querying** with clean, tabulated output.

---

## 🚀 Features

- 🔍 Ask for data on any course on Coursera (e.g., “Machine Learning”)
- 🤖 Uses **Gemini API** to fetch responses in structured JSON
- 💾 Saves responses as both `.json` files and in a local **SQLite database**
- 📋 Custom terminal querying with filters (by provider, difficulty, etc.)
- 📊 Outputs results in a pretty **tabular format** using `tabulate`
- 🧰 Reusable modular code (`SQLite`, `Enum`, etc.)

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/afa76d29-f3c2-4339-870b-9e7f57cb735e)

![image](https://github.com/user-attachments/assets/ceea034f-ddb6-4e2f-966f-55b9d7d3ac11)



---

## 🗂️ Project Structure

```bash
.
├── main.py               # CLI logic + while loop
├── utils.py              # Enum for abbreviations, etc.
├── db/
│   ├── SQLManager.py    # Custom SQLite manager with context support
│   └── courses.db       # Local database file
├── Course Details/
│   └── ai_courses.json   # JSON file exports
├── README.md
└── requirements.txt
```

---

## 🧑‍💻 How to Use

```bash
git clone https://github.com/fake-botpeter17/CourseraAIExplorer.git
cd CourseraAIExplorer
pip install -r requirements.txt
python main.py
```
Then type something like this:
```bash
> Machine Learning Specialization
```
and get
```
+---------+------------------+-----------------------+----------------+----------------------------------------------+----------------------------------------------+---------------------+
|  S.No.  |   Course Name    |    Course Provider    |  Course Type   |                 Sub-Courses                  |                 Description                  |  Certificate Value  |
+=========+==================+=======================+================+==============================================+==============================================+=====================+
|    1    | Machine Learning | Stanford University / | Specialization |     ["Machine Learning Specialization -      | This Specialization, taught by Andrew Ng, is |        High         |
|         |  Specialization  |    DeepLearning.AI    |                | Introduction to Machine Learning", "Machine  |  a foundational program that will teach you  |                     |
|         |                  |                       |                | Learning Specialization - Supervised Machine |    the fundamental principles of machine     |                     |
|         |                  |                       |                |  Learning: Regression and Classification",   |   learning.  You'll learn about supervised   |                     |
|         |                  |                       |                | "Machine Learning Specialization - Advanced  |  learning, unsupervised learning, and best   |                     |
|         |                  |                       |                |   Learning Algorithms", "Machine Learning    |     practices in machine learning. This      |                     |
|         |                  |                       |                |   Specialization - Machine Learning System   |       specialization provides a strong       |                     |
|         |                  |                       |                |                   Design"]                   |  understanding of machine learning, perfect  |                     |
|         |                  |                       |                |                                              |    for individuals seeking to start their    |                     |
|         |                  |                       |                |                                              |            journey in the field.             |                     |
+---------+------------------+-----------------------+----------------+----------------------------------------------+----------------------------------------------+---------------------+
```

---

## 🛠 Tech Stack

- 🐍 **Python 3.11+**
- 🧠 **Gemini API** (via [Google Generative AI](https://ai.google.dev))
- 🗃 **SQLite3** for persistent local storage
- 🧾 [`tabulate`](https://pypi.org/project/tabulate/) for clean CLI output
- 📁 **Custom Module**: `SQLite` manager with `createTable()`, `selectTable()`, etc.
- 📤 **Enum Utility**: `CourseType` and `CertificateValue` in `utils.py`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).



