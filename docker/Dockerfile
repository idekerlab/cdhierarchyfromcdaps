FROM continuumio/miniconda3

RUN mkdir /tmp/cdhierarchyfromcdaps
COPY dist/*.whl /tmp/cdhierarchyfromcdaps

RUN /opt/conda/bin/pip install /tmp/cdhierarchyfromcdaps/cdhierarchyfromcdaps*whl

RUN rm -rf /tmp/cdhierarchyfromcdaps

ENTRYPOINT ["/opt/conda/bin/cdhierarchyfromcdapscmd.py"]
CMD ["--help"]
