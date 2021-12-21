let download_btn = document.querySelector("#downlaod_btn");
let err_msg = "ERR::503:NOT_IMPLEMENTED";
let root_code = document.querySelector("#code_1");
let win_object = document.querySelector("#code_2");
let loop_func = document.querySelector("#code_3");
let conf_func = document.querySelector("#code_4");
let errwarninfo_func = document.querySelector("#code_5");

download_btn.addEventListener('click', (e)=>{
    fetch("assets/others/Short_tk_requied_tools.zip")
    .then(
        window.open("assets/others/Short_tk_requied_tools.zip")
    )
    .catch(e.err, (e)=>{
        console.error(e.err);
    })
});

root_code.addEventListener('click', ()=>{
    navigator.clipboard.writeText("import short_tk\n\nshort_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)\n\nlabel = Label(short_tk.root, text='hello world!')\nlabel.pack()\n\nshort_tk.Loop(loop=True)");
});

win_object.addEventListener('click', ()=>{
    navigator.clipboard.writeText("import short_tk\n\nshort_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)");
});

loop_func.addEventListener('click', ()=>{
    navigator.clipboard.writeText("import short_tk\n\nshort_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)\n\n# tkinter code\n\nshort_tk.Loop(loop=true)");
});
conf_func.addEventListener('click', ()=>{
    navigator.clipboard.writeText("import short_tk\n\nshort_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)\n\n# Tkinter code\nshort_tk.Window.Conf(data)\nshort_tk.Window.Loop(loop=True)");
});
errwarninfo_func.addEventListener('click', (e)=>{
    navigator.clipboard.writeText(`import short_tk\n\nshort_tk.Window(root_title=data, root_size=data, root_bg=data, root_favicon=data)\n\nshort_tk.Window.Err("MyApp:", "A test Error!")\n\nshort_tk.Window.Warn("MyApp:", "A test Warning!")\nshort_tk.Window.Info("MyApp:", "A test Info.")\nshort_tk.Window.Loop(loop=True)`);
});
