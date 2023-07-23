let current_GPA, current_hours, new_courses, old_courses;
let new_hours_sum = 0, old_hours_sum = 0, new_sum_GPA = 0, old_sum_GPA = 0, old_before_GPA = 0;
const gradePoints = {
    'A+': 12/3,
    'A': 11.5/3,
    'A-': 11/3,
    'B+': 10/3,
    'B': 9/3,
    'B-': 8/3,
    'C+': 7/3,
    'C': 6/3,
    'C-': 5/3,
    'D+': 4/3,
    'D': 3/3,
    'F': 0
};

function addNewCourseField(index) {
    let newCoursesFieldsDiv = document.getElementById('divnewCoursesFields');
    let div = document.createElement('div');
    div.innerHTML = `<label for="newCourseHours${index}">Credit Hours for New Course ${index}:</label>
                     <input type="number" id="newCourseHours${index}" name="newCourse${index}Hours" min="0"><br>
                     <label for="newCourseGrade${index}">Expected Grade for New Course ${index}:</label>
                     <input type="text" id="newCourseGrade${index}" name="newCourse${index}Grade"><br>`;
    newCoursesFieldsDiv.appendChild(div);
}

function addOldCourseField(index) {
    let oldCoursesFieldsDiv = document.getElementById('divoldCoursesFields');
    let div = document.createElement('div');
    div.innerHTML = `<label for="oldCourseHours${index}">Credit Hours for Old Course ${index}:</label>
                     <input type="number" id="oldCourseHours${index}" name="oldCourse${index}Hours" min="0"><br>
                     <label for="oldCourseCurrentGrade${index}">Current Grade for Old Course ${index}:</label>
                     <input type="text" id="oldCourseCurrentGrade${index}" name="oldCourse${index}CurrentGrade"><br>
                     <label for="oldCourseExpectedGrade${index}">Expected Grade for Old Course ${index}:</label>
                     <input type="text" id="oldCourseExpectedGrade${index}" name="oldCourse${index}ExpectedGrade"><br>`;
    oldCoursesFieldsDiv.appendChild(div);
}

function readNew(){
    let theData = document.getElementById('inpnewCourses');
    let newCoursesFieldsDiv = document.getElementById('divnewCoursesFields');
    newCoursesFieldsDiv.innerHTML = '';
    newCourses = Number(theData.value);
    for (let i = 1; i <= newCourses; i++) {
        addNewCourseField(i);
    }
}

function readOld(){

    let theData = document.getElementById('inpoldCourses');
    let oldCoursesFieldsDiv = document.getElementById('divoldCoursesFields');
    oldCoursesFieldsDiv.innerHTML = '';
    oldCourses = Number(theData.value);
    for (let i = 1; i <= oldCourses; i++) {
       addOldCourseField(i);
    }
}


function calculateGPA() {
    current_GPA = Number(document.getElementById('currentGPA').value);
    current_hours = Number(document.getElementById('currentHours').value);

    let new_courses_fields = document.querySelectorAll('[id^="newCourse"]');
    for (let field of new_courses_fields) {
	    if (field.id.includes("newCourseHour")){
        	let hours = Number(field.value);
        	let grade = document.getElementById(field.id.replace('Hours', 'Grade')).value;
		if (grade!="W"){
        	  new_hours_sum += hours;
        	  new_sum_GPA += gradePoints[grade] * hours;
		}
	    }
    }

    let old_courses_fields = document.querySelectorAll('[id^="oldCourse"]');
    for (let field of old_courses_fields) {
	    if (field.id.includes("oldCourseHour")){
        	let hours = Number(field.value);
        	let currentGrade = document.getElementById(field.id.replace('Hours', 'CurrentGrade')).value;
        	let expectedGrade = document.getElementById(field.id.replace('Hours', 'ExpectedGrade')).value;
		if (expectedGrade!="W"){ 
        	  old_hours_sum += hours;
        	  old_sum_GPA += gradePoints[expectedGrade] * hours;
		  if (currentGrade!="W") { 
        		old_before_GPA += gradePoints[currentGrade] * hours;
		  }
		}	
	    }
    }

    let newGPA = (current_hours * current_GPA + new_sum_GPA + old_sum_GPA - old_before_GPA) / (current_hours + new_hours_sum);
    document.getElementById("newGPA").innerHTML = "Your new GPA would be: " + newGPA.toFixed(2);

    // Reset sums for next calculation
    new_hours_sum = 0;
    old_hours_sum = 0;
    new_sum_GPA = 0;
    old_sum_GPA = 0;
    old_before_GPA = 0;
}

