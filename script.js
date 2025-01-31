function translateText() {
    const textInput = document.getElementById("text-input").value;
    const srcLang = document.getElementById("src-lang").value;
    const tgtLang = document.getElementById("tgt-lang").value;

    fetch("/translate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textInput, src_lang: srcLang, tgt_lang: tgtLang })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `<p><strong>Translated Text:</strong> ${data.translated_text}</p>`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}