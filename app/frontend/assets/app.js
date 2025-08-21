async function apiCall(path, method = 'GET', body) {
    const opts = {method, headers: {'Content-Type': 'application/json'}};
    if (body) opts.body = JSON.stringify(body);
    const res = await fetch('/api/' + path, opts);
    return res.json();
}

async function loadItems() {
    const res = await fetch('assets/data.json');
    const data = await res.json();
    const container = document.getElementById('content');
    container.innerHTML = '';
    data.items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'card';
        div.textContent = item.title;
        container.appendChild(div);
    });
}

document.getElementById('btn-home').onclick = () => {
    const container = document.getElementById('content');
    container.innerHTML = '<div id="log"></div>'+
        '<button id="scan-cr">Scan Crunchyroll</button>'+ 
        '<button id="scan-both">Scan Both</button>'+ 
        '<button id="enrich">Enrich</button>'+ 
        '<button id="export-excel">Export Excel</button>'+ 
        '<button id="export-sheets">Export Google Sheet</button>'+ 
        '<button id="create-mega">Create MEGA Folders</button>';
    document.getElementById('scan-cr').onclick = async ()=>appendLog(await apiCall('scan/crunchyroll','POST'));
    document.getElementById('scan-both').onclick = async ()=>appendLog(await apiCall('scan/both','POST'));
    document.getElementById('enrich').onclick = async ()=>appendLog(await apiCall('enrich','POST'));
    document.getElementById('export-excel').onclick = async ()=>appendLog(await apiCall('export/excel','POST'));
    document.getElementById('export-sheets').onclick = async ()=>appendLog(await apiCall('export/sheets','POST'));
    document.getElementById('create-mega').onclick = async ()=>appendLog(await apiCall('mega/create-folders','POST'));
};

document.getElementById('btn-master').onclick = loadItems;

function appendLog(msg){
    const log = document.getElementById('log');
    if (log) log.textContent += JSON.stringify(msg)+"\n";
}

// load home by default
window.onload = () => document.getElementById('btn-home').click();
