import streamlit as st
from modules import functions

todos = functions.get_data_from_todos_file()
st.title("Todo App")

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(f"{todo}\n")
    functions.write_todos(todos_args=todos)
    st.session_state["new_todo"] = ""



with st.expander(label="List of Todos", expanded=True):
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(label=todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos_args=todos)
            del st.session_state[todo]
            st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", key="new_todo", on_change=add_todo)

st.session_state
# with st.form(key="form"):
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         is_complete = st.form_submit_button("Complete")
#     with col2:
#         edit = st.form_submit_button("Edit")
# st.form_submit_button("Edit")


# if is_complete:
#     st.session_state[todos].remove(todo)
# elif is_submit:
#     pass