let board = ["-","-","-","-","-","-","-","-","-"];

const boardDiv = document.getElementById("board");

function renderBoard() {
    boardDiv.innerHTML = "";
    board.forEach((v, i) => {
        let cell = document.createElement("div");
        cell.className = "cell";
        cell.innerText = v === "-" ? "" : v;

        cell.onclick = () => userMove(i);
        boardDiv.appendChild(cell);
    });
}

async function userMove(i) {
    if (board[i] !== "-") return;
    board[i] = "X";

    let difficulty = document.getElementById("difficulty").value;

    let response = await fetch("/move", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({board, difficulty})
    });

    let data = await response.json();

    board[data.move] = "O";

    renderBoard();

    if (data.winner) alert(data.winner + " wins!");
    if (data.draw) alert("Draw!");
}

renderBoard();
