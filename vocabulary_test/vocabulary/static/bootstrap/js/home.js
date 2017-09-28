var problem ;   
var answer ;
var word_id ;
var correct_bar, wrong_bar, answer_bar;
var prob_node ;
var next_state = { change:false } ;
var problem_set = require('database/problem_set.json')


var headers = new Headers();
headers.append('X-CSRFToken', getCookie('csrftoken'));
headers.append('Accept', "application/json");
headers.append('Content-Type', "application/json");
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

$(function () {
	document.body.style.setProperty("--button-green", "rgb(177,216,161)") ;
	document.body.style.setProperty("--button-red", "#eca5a5") ;

	correct_bar = $("#correct_bar") ;
	wrong_bar = $("#wrong_bar") ;
	answer_bar = $("#answer_bar") ;
	prob_node = document.querySelector("#prob") ;

	ChangeQuestion() ;
	
	$("#next").on('click', function() { Next(next_state); }) ;
	$("#show_answer").on('click', ShowAnswer) ;
}) ;

function SubmitAnswerByEnter(e) {
//	console.log(e) ;
//	console.log(e.target.childNodes[3].value) ;
	var usr_ans = e.target.childNodes[3].value ;
	SubmitAnswer(usr_ans) ;
	next_state.change = true ;
	return ;
}

function SubmitAnswer(usr_ans) {
	HideBars() ;
//	console.log(usr_ans + " vs. " + answer) ;
	if (usr_ans === answer) {
		correct_bar.show() ;
		document.querySelector("#next").style.background="var(--button-green)" ;
		fetch('', {
			method: 'post', 
			body: JSON.stringify({'word_id': word_id}),
			headers: headers,
			credentials: 'include'
		}).then(function(res) {
			if (!res.ok) 
				alert('increase correct times error!')
		}).catch(function(err) {
			alert("Error!") ;
		})
//		console.log("correct") ;
	}
	else {
		wrong_bar.show() ;
		document.querySelector("#next").style.background="var(--button-red)" ;
//		console.log("wrong") ;
	}
}

function Next(state) {
	if (state.change) {
		ChangeQuestion() ;
	}
	else {
		SubmitAnswer(document.querySelector("#input_answer").value) ;
	}
	state.change = !state.change ;
}

function ShowAnswer() {
	HideBars() ;
	document.querySelector("#answer_bar").childNodes[2].textContent = "The answer is " + answer ;
	answer_bar.show() ;
}

function HideBars() {
	$("#correct_bar").hide();
	$("#wrong_bar").hide();
	$("#answer_bar").hide();
}

function ChangeQuestion() {
/* init status */
	HideBars() ;
	document.querySelector("#next").style.background="" ;
	document.querySelector("#input_answer").value = "" ;
	$("#input_answer").focus();

  console.log(problem_set) ;

/* fetch to get new problem and answer and wor_id */
	var new_request = new Request('new/', {
		method: "get"
	})
	fetch(new_request).then(function(res) {
//		console.log(res) ;
		if (res.ok) {
			res.json().then(function(data) {
				problem = data.prob ;
				answer = data.ans ;
				word_id = data.word_id ;
//				console.log(problem) ;
//				console.log(answer) ;
				prob.innerHTML = problem ;
			}) ;
		}
		else {
			console.log("Response error when changing question.")
		}
	}).catch(function(err) {
		alert("Error!") ;
	})
	return ;
}
