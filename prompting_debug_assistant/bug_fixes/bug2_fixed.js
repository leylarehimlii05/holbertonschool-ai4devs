function calculateAverageGrade(students) {
    let totalScore = 0;
    // Fixed loop boundary condition and explicitly cast string score to Number
    for (let i = 0; i < students.length; i++) {
        totalScore += Number(students[i].score);
    }
    return totalScore / students.length;
}

const studentList = [
    { name: "Alice", score: "85" },
    { name: "Bob", score: "90" },
    { name: "Charlie", score: "78" }
];

console.log("Calculating student class average score...");
const average = calculateAverageGrade(studentList);
console.log("Average result:", average);
