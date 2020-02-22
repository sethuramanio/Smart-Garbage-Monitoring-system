
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify
import json
import boto3
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

s3=boto3.resource('s3')
dynamodb=boto3.resource('dynamodb')
rek = boto3.client('rekognition')
@app.route("/")
@cross_origin()
def hello_world():
    return 'Hello from Flask!'

@app.route('/front', methods=['POST','GET'])
@cross_origin()
def front():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set dir = :r",
    ExpressionAttributeValues={
        ':r': v,
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"
@app.route('/back', methods=['POST','GET'])
@cross_origin()
def back():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set dir = :r",
    ExpressionAttributeValues={
        ':r': v,
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"	
@app.route('/left', methods=['POST','GET'])
@cross_origin()
def left():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set dir = :r",
    ExpressionAttributeValues={
        ':r': v,
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"	
@app.route('/right', methods=['POST','GET'])
@cross_origin()
def right():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set dir = :r",
    ExpressionAttributeValues={
        ':r': v,
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"
@app.route('/stop', methods=['POST','GET'])
@cross_origin()
def stop():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set dir = :r",
    ExpressionAttributeValues={
        ':r': v,
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"

@app.route('/pick', methods=['POST','GET'])
@cross_origin()
def pick():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set stat = :r,flag=:f",
    ExpressionAttributeValues={
        ':r': 'p',':f':'0',
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"

@app.route('/drop', methods=['POST','GET'])
@cross_origin()
def drop():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set stat = :r,flag=:f",
    ExpressionAttributeValues={
        ':r': 'd',':f':'1',
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"

@app.route('/stat', methods=['POST','GET'])
@cross_origin()
def stat():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    #v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set stat = :r",
    ExpressionAttributeValues={
        ':r': 's',
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"
	
@app.route('/read', methods=['GET','POST'])
@cross_origin()
def userdetails():
    dynamodbTable=dynamodb.Table('makeathon_control')
    response=dynamodbTable.get_item(
            Key={
	        'val': "1"
	        }
        
        )
    item=response['Item']
    return (json.dumps(item))
    return (item)

@app.route('/gps', methods=['GET','POST'])
@cross_origin()
def gps():
    dynamodbTable=dynamodb.Table('hackhub_gps')
    response = dynamodbTable.scan()
    item=response
    print(item)
    return (json.dumps(item))

@app.route('/flag0', methods=['POST','GET'])
@cross_origin()
def flag0():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    #v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set flag = :r",
    ExpressionAttributeValues={
        ':r': '1',
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done" 
@app.route('/flag1', methods=['POST','GET'])
@cross_origin()
def flag1():
    print(request.data)
    table=dynamodb.Table('makeathon_control')
    #v = request.form['a']
    table.update_item(
    Key={
        'val': '1'
    },
    UpdateExpression="set flag = :r",
    ExpressionAttributeValues={
        ':r': '0',
    },
    ReturnValues="UPDATED_NEW"
    )
    return"done"

if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0',port=5000,threaded=True)
