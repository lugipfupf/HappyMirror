(function () {
    function startTime() {
        const d = new Date()

        formattedDateTime = [
            (d.getMonth() + 1).padLeft(),
            d.getDate().padLeft(),
            d.getFullYear()
        ].join('.') + ' ' + [
            d.getHours().padLeft(),
            d.getMinutes().padLeft(),
            d.getSeconds().padLeft()
        ].join(':')

        document.getElementById('fulldate').innerHTML = formattedDateTime
        setTimeout(startTime, 1000)
    }

    window.addEventListener('load', () => {
        startTime()
    })


})()

Number.prototype.padLeft = function (base, chr) {
    var len = (String(base || 10).length - String(this).length) + 1;
    return len > 0 ? new Array(len).join(chr || '0') + this : this;
}
