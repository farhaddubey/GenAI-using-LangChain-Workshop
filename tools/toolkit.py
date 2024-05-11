# Init a toolkit
tookit = ExampleToolkit(...)
tools = toolkit.get_tools()
agent = create_agent_method(llm, tools, prompt)