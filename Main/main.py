import streamlit as st
from docxtpl import DocxTemplate


def generate_specification_with_template():
    template_path = r'D:\Work\Work\07_02_2026_packed_exe\Main\template3.docx'
    doc = DocxTemplate(template_path)

    batch = st.session_state.batch
    boxes = st.session_state.lots.get(batch, [])

    total_weight = sum(box["box_weight"] for box in boxes)

    context = {
        "number_order": st.session_state.number_order,
        "material": st.session_state.material,
        "batch": batch,
        "leight": st.session_state.leight,
        "width": st.session_state.width,
        "density": st.session_state.density,
        "name_product": st.session_state.name_product,
        "customer": st.session_state.customer,
        "count_box": st.session_state.count_box,
        "boxes": boxes,
        "total_weight": round(total_weight, 2),
    }

    doc.render(context)
    doc.save("generated_specification.docx")



def main():
    st.set_page_config(page_title="Упаковка", page_icon="📦", layout="wide")

  
    if "lots" not in st.session_state:
        st.session_state.lots = {}   

    if "current_lot" not in st.session_state:
        st.session_state.current_lot = None

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Номер замовлення", key="number_order")
        st.text_input("Матеріал упаковки", key="material")
        st.text_input("Лот", key="batch")

    with col2:
        st.text_input("Довжина", key="leight")
        st.text_input("Ширина", key="width")
        st.text_input("Щільність", key="density")

    with col3:
        st.number_input("Кількість коробок", key="count_box", min_value=1, step=1)
        st.number_input("Вага (з вагів / вручну)", key="weight", step=0.01)

    with col4:
        st.text_input("Назва товару", key="name_product")
        st.text_input("Замовник", key="customer")

  
    batch = st.session_state.batch

    if batch:
        if batch != st.session_state.current_lot:
            st.session_state.current_lot = batch

            if batch not in st.session_state.lots:
                st.session_state.lots[batch] = []   

        active_boxes = st.session_state.lots[batch]
    else:
        active_boxes = []

    st.divider()

    col_btn1, col_btn2, col_btn3 = st.columns(3)

    with col_btn1:
        if st.button("⚖️ Зважити коробку"):
            if not batch:
                st.warning("Введіть лот")
            elif len(active_boxes) < st.session_state.count_box:
                active_boxes.append({
                    "box_no": len(active_boxes) + 1,
                    "box_weight": st.session_state.weight
                })
            else:
                st.warning("Досягнуто заявлену кількість коробок")

    with col_btn2:
        if st.button("❌ Видалити останню"):
            if active_boxes:
                active_boxes.pop()

    with col_btn3:
        if st.button("📄 Специфікація"):
            if batch:
                generate_specification_with_template()
                with open("generated_specification.docx", "rb") as f:
                    st.download_button(
                        "⬇️ Завантажити Word",
                        f,
                        file_name=f"specification_{batch}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

    st.divider()

    st.subheader("📦 Коробки")

    if active_boxes:
        for i, box in enumerate(active_boxes):
            col_a, col_b, col_c = st.columns([1, 2, 1])

            with col_a:
                st.write(f"№ {box['box_no']}")

            with col_b:
                new_weight = st.number_input(
                    "Вага, кг",
                    value=box["box_weight"],
                    step=0.01,
                    key=f"{batch}_box_{i}"
                )
                active_boxes[i]["box_weight"] = new_weight

            with col_c:
                st.write("кг")

        total_weight = sum(box["box_weight"] for box in active_boxes)
        st.success(f"🔢 Загальна вага лоту: **{round(total_weight, 2)} кг**")

        st.info(f"Зважено: {len(active_boxes)} / {st.session_state.count_box} коробок")

    else:
        st.info("Для цього лоту ще немає коробок")


if __name__ == "__main__":
    main()
