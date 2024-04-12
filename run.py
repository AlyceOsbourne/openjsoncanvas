from openjsoncanvas import Canvas

path = "test.canvas"
canvas = Canvas()
canvas.create_text_node(text="Hello, World!", x=100, y=100, id="1", width=100, height=100)
canvas.create_file_node(file="test.txt", x=200, y=200, id="2", width=100, height=100)
canvas.create_link_node(url="https://example.com", x=300, y=300, id="3", width=100, height=100)
canvas.create_group_node(x=400, y=400, id="4", width=100, height=100)
canvas.create_edge(id="1-2", fromNode="1", toNode="2")
canvas.create_edge(id="2-3", fromNode="2", toNode="3")
canvas.create_edge(id="3-4", fromNode="3", toNode="4")

canvas.to_file(path)
canvas = Canvas.from_file(path)
print(canvas.model_dump_json())
