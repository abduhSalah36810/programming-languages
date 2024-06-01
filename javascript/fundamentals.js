



 // Let , Const , Var 
{
     var num= 44 ;
}
{
     let numb = 11
}
{
     const number = 112
}

console.log('var '+ num)
/*
(let) and (cosnt)  have Bloc scope :

console.log('let '+numb)
console.log("const" + number) 

(let) and (const) can not be redeclared: 
let numb = 12 
const number = 111
(let) and (const) must be declared before use. 
*/


 

function add(a, b)  {
    return a+b 
}

const sub = function add(a, b)  {
    return a-b 
 }

function higherOrder(fun) { 
    sum = fun
    result = sum / 2 
    return result 
} 

console.log(higherOrder(add(1, 2)))

function WtfIsThis(){
    console.log(this);
}

const fuv = {
    WtfIsThis:function(){
        console.log(this);
    }
}



// Numbers:
let length = 16;
let weight = 7.5;

// Strings:
let color = "Yellow";
let lastName = "Johnson";

// Booleans
let x = true;
let y = false;

// Object:
const person = {firstName:"John", lastName:"Doe"};

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

// Date object:
const date = new Date("2022-03-25");