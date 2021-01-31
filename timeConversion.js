/*
convert AM/PM time to 
military time
*/

let time = '06:40:03 AM'


function timeConversion(time) {
    let timeList = time.split(':')
    let hour = parseInt(timeList[0])
    if (hour >= 1 && hour <= 11 && time.includes("P")) {
        let milHour = hour + 12
        let milTime = milHour
        return (`${milTime}${time.substr(2, 6)}`)
    }
    else if (hour === 12 && time.includes("A")) {
        let midnight = '00'
        let milTime = midnight
        return (`${milTime}${time.substr(2, 6)}`)
    }
    else {
        return (time.substr(0, 8))
    }
}

console.log(timeConversion(time))


