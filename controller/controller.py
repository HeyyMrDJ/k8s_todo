"""Custom kubernetes controller written in python that will 
extend kubernetes functionality to run a todo list engine"""
import kopf


@kopf.on.create('todoitems')
def create_fn(body, **kwargs):
    """Run this function when creating todoitem"""
    print(f"Creating todo item {body['metadata']['name']}")


@kopf.on.update('todoitems')
def update_fn(body, **kwargs):
    """Run this function when updating todoitem"""
    print(f"Updating todo item {body['metadata']['name']}")


@kopf.on.delete('todoitems')
def delete_fn(body, **kwargs):
    """Run this function when deleting todoitem"""
    print(f"Deleting todo item {body['metadata']['name']}")
