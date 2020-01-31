import edgeiq


def main():
    semantic_segmentation = edgeiq.SemanticSegmentation(
            "alwaysai/enet")
    semantic_segmentation.load(engine=edgeiq.Engine.DNN)

    print("Engine: {}".format(semantic_segmentation.engine))
    print("Accelerator: {}\n".format(semantic_segmentation.accelerator))
    print("Model:\n{}\n".format(semantic_segmentation.model_id))
    print("Labels:\n{}\n".format(semantic_segmentation.labels))

    with edgeiq.FileVideoStream('Use Case - Clip 3.mp4') as video_stream, \
            edgeiq.Streamer() as streamer:

        while True:
            frame = video_stream.read()

            results = semantic_segmentation.segment_image(frame)

            # Generate text to display on streamer
            text = ["Model: {}".format(semantic_segmentation.model_id)]
            text.append("Inference time: {:1.3f} s".format(results.duration))
            text.append("Legend:")
            text.append(semantic_segmentation.build_legend())

            mask = semantic_segmentation.build_image_mask(results.class_map)
            blended = edgeiq.blend_images(frame, mask, alpha=0.5)

            streamer.send_data(blended, text)
            if streamer.check_exit():
                break

        print("Program Ending")


if __name__ == "__main__":
    main()
