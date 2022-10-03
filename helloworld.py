'''
Created on 04-Sep-2019

@author: bkadambi
'''

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/hello')   # URL '/' to be handled by main() route handler
def main():

    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: "my-hello-service"})
        )
    )

    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",
        agent_port=6831,
    )

    trace.get_tracer_provider().add_span_processor(
       BatchSpanProcessor(jaeger_exporter)
    )
     
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("rootSpan"):
        with tracer.start_as_current_span("childSpan"):
            print("Hello world!")

    """Say hello"""
    return 'Hello, world 4!'

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
