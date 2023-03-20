var myInterval = setInterval(get_tasks, 5000);

function get_tasks() {
    const tasks = document.querySelectorAll(".task");
    tasks.forEach(each_task)

}
function each_task(item) {
    send_update(item.id, item.parentElement.id);

}

function send_update(name, lane) {
    fetch('/update', {
    headers: {
        'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify({ "name": name, "lane": lane })
    })
}
