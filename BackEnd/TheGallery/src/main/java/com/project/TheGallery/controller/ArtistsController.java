package com.project.TheGallery.controller;

import com.project.TheGallery.entity.Artist;
import com.project.TheGallery.service.GalleryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ArtistsController {

    @Autowired
    private GalleryService galleryService;

    @GetMapping(value = "/artists")
    public List<Artist> fetchAllArtists(){
        return galleryService.fetchArtistList();
    }

    @GetMapping(value = "/artists/{id}")
    public Artist fetchArtistById(@PathVariable("id") Integer artistId) {
        return galleryService.fetchArtistId(artistId);
    }

    @GetMapping(value = "/artists/random")
    public Artist fetchArtistRandom() {
        return galleryService.fetchArtistRandom();
    }

    @GetMapping(value = "/artists/random10")
    public List<Artist> fetchArtistRandom10() {
        return galleryService.fetchArtistRandom10();
    }

    @GetMapping(value = "/artists/random/{id}")
    public List<Artist> fetchArtistRandomList(@PathVariable("id") Integer artistCount) {
        return galleryService.fetchArtistRandomList(artistCount);
    }

    @GetMapping(value = "/artists/name/{name}")
    public Artist fetchArtistName(@PathVariable("name") String artistName) {
        return galleryService.fetchArtistByName(artistName);
    }

//    @GetMapping(value = "/artists/name/{name}/{id}",produces = MediaType.IMAGE_JPEG_VALUE)
//    public @ResponseBody byte[] fetchArtistPicture(@PathVariable("name") String artistName,
//                                                   @PathVariable("id") Integer pictureId)
//    throws IOException {
//
//        InputStream in = getClass()
//                .getResourceAsStream("/TheGalleryDB/images/"+artistName+"/"+artistName+pictureId);
//
//
//        return IOUtils.toByteArray(in);
//    }

}
