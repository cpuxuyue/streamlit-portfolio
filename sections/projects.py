import streamlit as st
from annotated_text import annotated_text, parameters

def get_projects_section():
    parameters.SHOW_LABEL_SEPARATOR = True
    parameters.BORDER_RADIUS = "0.25rem"
    parameters.PADDING = "0.5rem"
    parameters.LABEL_SPACING = "0.5rem"
    PYTHON_COLOR_CODE = "#a17e00"

    st.header("Stream DaQ")
    stream_daq_logo, stream_daq_description = st.columns(2)
    with stream_daq_logo:
        st.image("assets/images/Stream DaQ logo.png")
    with stream_daq_description:
        st.write("Real-time data quality monitoring tailored to data streams. 60+ metrics to cherry-pick the ones that make the difference in your use-case!")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/stream-DaQ",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Python", "core", PYTHON_COLOR_CODE),
        "\t",
        ("Pathway", "stream processing", "#162ceb"),
        "\t",
        ("Redis", "stateful operations", "#D82C20"),
        "\t",
        ("PostgreSQL", "source/sink", "#356790"),
    )
    st.divider()

    st.header("Cluster them out!")
    cluster_them_out_logo, cluster_them_out_description = st.columns(2)
    with cluster_them_out_logo:
        st.image("assets/images/Cluster them out logo.png")
    with cluster_them_out_description:
        st.write(
            "Scalable outlier detection workflow for spatial 2-dimensional data, leveraging clustering techniques. Part of University project co-developed with my esteemed friend and colleague, Lazaros.")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/cluster-them-out",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Scala", "core", "#d73937"),
        "\t",
        ("R", "core", "#2366b5"),
        "\t",
        ("Apache Spark", "computing framework", "#dc5b19"),
    )
    st.divider()

    import base64
    st.header("SimpleSim")
    cluster_them_out_logo, cluster_them_out_description = st.columns(2)
    with cluster_them_out_logo:
        file_ = open("assets/images/SimpleSim animation.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
    with cluster_them_out_description:
        st.write(
            "A UAV and a ground target moving around in 3D space. All in one place, built from scratch and visualized! ")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/SimpleSim",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Python", "core", PYTHON_COLOR_CODE),
        "\t",
        ("Matplotlib", "3D visualizations", "#d6854f"),
    )
    st.divider()

    st.write("It seems you have reached the end of this page! Luckily, my projects do not end here! Should you wish to see more, feel free to visit my GitHub profile, where 12+ past and current projects of mine have been made publicly available.")
    st.link_button("See GitHub profile",
                   url="https://github.com/Bilpapster/SimpleSim",
                   icon=":material/terminal:")


