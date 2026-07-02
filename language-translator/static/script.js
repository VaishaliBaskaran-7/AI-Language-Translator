document.getElementById("translate-btn")
.addEventListener("click", async function () {
    const text =
        document.getElementById("input-text").value;
    const sourceLang =
        document.getElementById("source-language").value;
    const targetLang =
        document.getElementById("target-language").value;

    const response = await fetch("/translate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text,
            source_lang: sourceLang,
            target_lang: targetLang
        })
    });

    const data = await response.json();
    document.getElementById("output-text").value =
        data.translated_text;
});