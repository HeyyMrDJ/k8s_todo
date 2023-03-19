"""Python Flask app that will query the kubernetes API for the todoitems 
and display on a kanban according to their lane annotation"""

from flask import Flask, render_template
from kubernetes import client, config


app = Flask(__name__)


# Load configuration from your kubeconfig file for auth
config.load_kube_config()


def return_items():
    """Query kubernetes API for todoitems and return dictionary of items and their lanes"""
    todo_list = []
    items = client.CustomObjectsApi().list_namespaced_custom_object(
            group="kopf.dev",
            version="v1", 
            namespace="default", 
            plural="todoitems")

    for item in items['items']:
        todo_list.append((item['metadata']['name'], item['metadata']['annotations']['lane']))

    return {k: v for k, v in todo_list}


@app.route("/")
def hello_world():
    todo_dict = return_items()
    return render_template('index.html', items=todo_dict)
