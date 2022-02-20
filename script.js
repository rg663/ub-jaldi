function openingsequenceparking(){
  return vruna_code
}
function openingsequence()  { ajaxGetRequest("/opendisplay",openingsequenceparking)
}

function name(params){
  
}
function addnew(){
  let ubitname=document.getElementById("ubit") 
  let t1=document.getElementById("1") 
  let t2=document.getElementById("2") 
  let t3=document.getElementById("3") 
  let t4=document.getElementById("4") 
  let t5=document.getElementById("5")
  let t6=document.getElementById("6") 
  let t7=document.getElementById("7") 
  let t8=document.getElementById("8") 
  let t9=document.getElementById("9") 
  let t10=document.getElementById("10") 
  let t11=document.getElementById("11") 
  let t12=document.getElementById("12") 
  let t13=document.getElementById("13") 
  let t14=document.getElementById("14") 
  let t15=document.getElementById("15") 
  let t16=document.getElementById("16") 
  let t17=document.getElementById("17") 
  let t18=document.getElementById("18") 
  let t19=document.getElementById("19") 
  let t20=document.getElementById("20") 
  let t21=document.getElementById("21") 
  let t22=document.getElementById("22") 
  let t23=document.getElementById("23") 
  let t24=document.getElementById("24") 
  l=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24]
    timecount=[]
  for(let m of l){
    if(m.checked==true){
      timecount.append(m.innerHTML)
    }
  return timecount
  }
}

function run(){
	let p=document.querySelector("#spots").value
	document.querySelector('.output').textContent=p;
}

function makelist(){
  let l=[]
  let p=document.querySelector("#spots").value
  let ubitname=document.getElementById("ubit").value
  let time=addnew()
  l.append(p)
  l.append(ubitname)
  l.append(time)
  l=[{"parkingname":p,"ubitname":ubitname,"time":time}]
	document.querySelector('.output').textContent=p;
	return l
}

let pa = makelist()

function makedata(x){
  givenname=JSON.parse(x) 
  console.log(JSON.stringify(x))
}

function sendingdata(x) {
  return makelist()
}

function getreq1() {
  ajaxGetRequest("/opendisplay",makedata)
  ajaxGetRequest("/sendoverdata",sendingdata)
}



// const sqlite3 = require('sqlite3').verbose()
// let db = new sqlite3.Database('../db/sample.db')
// // construct the insert statement with multiple placeholders
// // based on the number of rows

// let sql = 'INSERT INTO PARKING VALUES' 
// let values=["1","a","b"]

// db.run(sql,function(err) {
//   if (err) {
//     return console.error(err.message);
//   }
//   console.log(`Rows inserted ${this.changes}`);
// });



// // close the database connection
// db.close();


function post(){
	let paa = JSON.stringify(pa)
  ajaxPostRequest("/newdata",pa,makedata)
}