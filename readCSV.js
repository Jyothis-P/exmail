const csv = require('csv-parser');
const fs = require('fs');
var write = require('./writeObjCsv.js')

const admin = require('firebase-admin');

//The spreadsheet should be named file.csv

//Provide the path to your service account json file.
// let serviceAccount = require('D:\\Keys\\Firebase\\blahblah.json');


admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

let db = admin.firestore();

seats = []
var c = 0;
fs.createReadStream('file.csv')
    .pipe(csv())
    .on('data', (row) => {
        // console.log(row);
        seat = {};

        seats.push(row);
    })
    .on('end', () => {
        var promises = []
        seats.forEach(seat => {
            if (seat.Email) {
                if (seat.Email.includes('@')) {
                    c++;
                    var promise = db.collection('users').where('email', '==', seat.Email).where('seat', '==', seat.Seat).limit(1).get()
                        .then(snapshot => {
                            snapshot.forEach(doc => {
                                seat.Name = doc.data().name;
                                seat.Phone = doc.data().phone;
                                seat.Type = doc.data().type;
                                seat.Food = doc.data().food;
                            });
                        })
                    promises.push(promise);
                }
            }
        });
        Promise.all(promises).then(values => {
            console.log('All values filled successully');
            write(seats);
            console.log(c)
        }).catch(err => {
            console.log(err)
        });
        console.log('CSV file successfully processed');
    });