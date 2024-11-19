import gradio as gr
import traceback


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"

def parse_html(username,html_str):
    html_str = html_str.lstrip().rstrip()
    arr = html_str.split("\n")
    flag = False
    content = ""
    match_str = ""
    match_end_str = ""

    for a in arr:
        a = a.lstrip().rstrip()
        if match_end_str:
            if match_end_str in a:
                match_end_str = ""
                continue
            else:
                continue
        if flag:
            if a == "</p>":
                flag = False
                continue
            else:
                if a.endswith("</p>"):
                    a = a[:-4]
                    a = re.sub(r"<[a-zA-Z]{,10}>.*</[a-zA-Z]{,10}>","",a)
                    content += a + "\n"
                else:
                    if not re.search("<[a-zA-Z]{,10}>",a):
                        content += a + "\n"
                    else:
                        match_str = re.search("<[a-zA-Z]{,10}>",a).group()
                        match_end_str = match_str[0] + "/" + match_str[1:]
                        if match_end_str in a:
                            match_end_str = ""
        if a.startswith("<p>"):
            if a == "<p>":
                flag = True
            else:
                if a.endswith("</p>"):
                    a = a[3:-4]
                    a = re.sub(r"<[a-zA-Z]{,10}>.*</[a-zA-Z]{,10}>","",a)
                    content += a + "\n"
                else:
                    if not re.search("<[a-zA-Z]{,10}>",a):
                        content += a + "\n"
                    else:
                        match_str = re.search("<[a-zA-Z]{,10}>",a).group()
                        match_end_str = match_str[0] + "/" + match_str[1:]
                        if match_end_str in a:
                            match_end_str = ""
    return content.rstrip() + "\n" + username.upper(),"SUCCESS"
def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 2"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=username,raw_input,
                outputs=[pack_output, status_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )


if __name__ == "__main__":
    main()

