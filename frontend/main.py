import streamlit as st

# Определяем меню для переключения между страницами
page = st.sidebar.selectbox(
    "Выберите страницу",
    ["Индексация документов", "Поиск информации"]
)

# --------------------------------
# Страница 1: Индексация документов
# --------------------------------
if page == "Индексация документов":
    st.title("Индексация документов")

    # Загрузка документа
    uploaded_file = st.file_uploader("Загрузите документ (.txt)", type="txt")

    # Поле для ввода тега
    tag_option = st.selectbox(
        "Выберите тег из существующих или введите новый",
        options=["ТЕГ_1", "ТЕГ_2", "ТЕГ_3"],  # Пример существующих тегов
        help="Вы можете выбрать один из существующих тегов или ввести новый ниже."
    )
    custom_tag = st.text_input("Введите новый тег (если необходимо)")

    # Объединение выбора и пользовательского ввода тега
    selected_tag = custom_tag if custom_tag else tag_option

    # Кнопка для загрузки документа
    if st.button("Загрузить документ"):
        if uploaded_file and selected_tag:
            document_text = uploaded_file.read().decode("utf-8")
            st.success("Документ успешно загружен!")
            st.write(f"Содержимое документа:\n{document_text}")
            st.write(f"Применённый тег: {selected_tag}")
        else:
            st.error("Пожалуйста, загрузите файл и укажите тег.")

# -------------------------------
# Страница 2: Поиск информации
# -------------------------------
elif page == "Поиск информации":
    st.title("Поиск информации")

    # Поле для ввода текста запроса
    query_text = st.text_input("Введите текст запроса", help="Введите текст запроса для поиска информации.")
    if not query_text:
        st.warning("Поле запроса обязательно для заполнения.")

    # Поле для фильтрации по тегу
    st.subheader("Фильтрация по тегам")
    available_tags = ["ТЕГ_1", "ТЕГ_2", "ТЕГ_3"]  # Пример существующих тегов
    selected_tags = st.multiselect(
        "Выберите один или несколько тегов из списка (опционально):",
        options=available_tags,
        help="Выберите теги для фильтрации результатов."
    )

    # Поле выбора количества результатов
    top_k = st.number_input(
        "Количество результатов (Top-K):",
        min_value=1,
        max_value=100,
        value=5,
        step=1,
        help="Укажите количество результатов, которые нужно вернуть."
    )

    # Кнопка поиска
    if st.button("Найти"):
        if query_text:
            # Пример: Заглушка для результатов
            st.success("Поиск выполнен успешно!")
            st.subheader("Результаты:")
            results = [
                {"content": "Пример параграфа 1", "tag": "ТЕГ_1"},
                {"content": "Пример параграфа 2", "tag": "ТЕГ_2"},
                {"content": "Пример параграфа 3", "tag": "ТЕГ_3"},
            ]
            for idx, result in enumerate(results[:top_k], start=1):
                st.write(f"**Результат {idx}:**")
                st.write(f"Текст: {result['content']}")
                st.write(f"Тег: {result['tag']}")
        else:
            st.error("Поле запроса обязательно для выполнения поиска.")